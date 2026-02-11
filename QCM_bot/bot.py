"""
English Grammar & Vocabulary Practice Bot for Telegram
A beginner-friendly bot for students to practice English with QCM quizzes
"""

import os
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from io import BytesIO

# Import question banks
from grammar_questions import GRAMMAR_QUESTIONS
from vocabulary_questions import VOCABULARY_QUESTIONS

# Import database functions
from database import (
    init_db,
    save_quiz_result,
    get_user_stats,
    get_user_history,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Quiz state management (stored per user)
user_quiz_state = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message and main menu"""
    user = update.effective_user
    
    keyboard = [
        [InlineKeyboardButton("📘 Grammar", callback_data="topic_grammar")],
        [InlineKeyboardButton("📗 Vocabulary", callback_data="topic_vocabulary")],
        [InlineKeyboardButton("📊 My Score", callback_data="my_score")],
        [InlineKeyboardButton("📈 My Performance", callback_data="my_performance")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = f"""
Welcome {user.first_name}!

I'm your English practice bot! 🎓

Choose what you want to practice:
• Grammar - Tenses, structures, rules
• Vocabulary - Words, phrases, expressions

Track your progress with:
• My Score - See your latest results
• My Performance - View your improvement chart

Let's start learning!
    """
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all button clicks"""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    data = query.data
    
    # Topic selection (Grammar/Vocabulary)
    if data.startswith("topic_"):
        topic = data.split("_")[1]
        await show_level_selection(query, topic)
    
    # Level selection (A1-C2)
    elif data.startswith("level_"):
        parts = data.split("_")
        topic = parts[1]
        level = parts[2]
        await start_quiz(query, user_id, topic, level)
    
    # Answer selection
    elif data.startswith("answer_"):
        parts = data.split("_")
        question_index = int(parts[1])
        selected_option = int(parts[2])
        await process_answer(query, user_id, question_index, selected_option)
    
    # My Score
    elif data == "my_score":
        await show_score(query, user_id)
    
    # My Performance
    elif data == "my_performance":
        await show_performance(query, user_id)
    
    # Back to menu
    elif data == "back_to_menu":
        await show_main_menu(query)


async def show_level_selection(query, topic):
    """Show level selection buttons"""
    keyboard = [
        [
            InlineKeyboardButton("A1", callback_data=f"level_{topic}_A1"),
            InlineKeyboardButton("A2", callback_data=f"level_{topic}_A2"),
        ],
        [
            InlineKeyboardButton("B1", callback_data=f"level_{topic}_B1"),
            InlineKeyboardButton("B2", callback_data=f"level_{topic}_B2"),
        ],
        [
            InlineKeyboardButton("C1", callback_data=f"level_{topic}_C1"),
            InlineKeyboardButton("C2", callback_data=f"level_{topic}_C2"),
        ],
        [InlineKeyboardButton("⬅️ Back to Menu", callback_data="back_to_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    topic_name = "Grammar" if topic == "grammar" else "Vocabulary"
    text = f"""
{topic_name} Practice

Select your level:
• A1 - Beginner
• A2 - Elementary
• B1 - Intermediate
• B2 - Upper Intermediate
• C1 - Advanced
• C2 - Proficient
    """
    
    await query.edit_message_text(text, reply_markup=reply_markup)


async def start_quiz(query, user_id, topic, level):
    """Initialize and start a new quiz session"""
    # Get questions based on topic
    if topic == "grammar":
        questions = GRAMMAR_QUESTIONS.get(level, [])
    else:
        questions = VOCABULARY_QUESTIONS.get(level, [])
    
    if not questions:
        await query.edit_message_text(
            f"Sorry, no questions available for {level} level yet.\n"
            "Please try another level."
        )
        return
    
    # Take only 10 questions (or less if not enough available)
    import random
    quiz_questions = random.sample(questions, min(10, len(questions)))
    
    # Initialize quiz state for this user
    user_quiz_state[user_id] = {
        "topic": topic,
        "level": level,
        "questions": quiz_questions,
        "current_index": 0,
        "answers": [],  # Store user's selected answers
        "correct_count": 0,
        "start_time": datetime.now(),  # Track quiz start time
    }
    
    # Show first question
    await show_question(query, user_id, 0)


async def show_question(query, user_id, question_index):
    """Display a single question with options"""
    logger.info(f"show_question called - User: {user_id}, Index: {question_index}")
    
    state = user_quiz_state.get(user_id)
    if not state:
        logger.error(f"No quiz state for user {user_id}")
        await query.message.reply_text("Quiz session expired. Please start a new quiz with /start")
        return
    
    questions = state["questions"]
    
    if question_index >= len(questions):
        # Quiz finished
        logger.info(f"Quiz finished for user {user_id}. Showing final review.")
        await show_final_review(query, user_id)
        return
    
    question_data = questions[question_index]
    question_text = question_data["q"]
    options = question_data["options"]
    
    # Create option buttons
    keyboard = []
    for i, option in enumerate(options):
        keyboard.append([
            InlineKeyboardButton(
                f"{chr(65+i)}. {option}",
                callback_data=f"answer_{question_index}_{i}"
            )
        ])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    topic_name = "Grammar" if state["topic"] == "grammar" else "Vocabulary"
    text = f"""
{topic_name} - Level {state['level']}

Question {question_index + 1}/10

{question_text}

Choose your answer:
    """
    
    try:
        await query.edit_message_text(text, reply_markup=reply_markup)
        logger.info(f"Question {question_index + 1} displayed successfully")
    except Exception as e:
        logger.error(f"Error displaying question: {e}")
        # Try sending as new message if edit fails
        await query.message.reply_text(text, reply_markup=reply_markup)


async def process_answer(query, user_id, question_index, selected_option):
    """Process user's answer and move to next question"""
    logger.info(f"Processing answer - User: {user_id}, Question: {question_index}, Option: {selected_option}")
    
    state = user_quiz_state.get(user_id)
    if not state:
        logger.error(f"No quiz state for user {user_id}")
        await query.message.reply_text("Quiz session expired. Please start a new quiz with /start")
        return
    
    questions = state["questions"]
    
    if question_index >= len(questions):
        logger.error(f"Invalid question index: {question_index}, total: {len(questions)}")
        return
    
    question_data = questions[question_index]
    
    correct_answer = question_data["answer"]
    is_correct = selected_option == correct_answer
    
    # Store the answer
    state["answers"].append({
        "selected": selected_option,
        "correct": correct_answer,
        "is_correct": is_correct,
    })
    
    if is_correct:
        state["correct_count"] += 1
    
    # Move to next question
    state["current_index"] += 1
    logger.info(f"Moving to question {state['current_index']}, total questions: {len(questions)}")
    
    await show_question(query, user_id, state["current_index"])


async def show_final_review(query, user_id):
    """Show final score and complete review of all questions"""
    try:
        state = user_quiz_state.get(user_id)
        if not state:
            logger.error(f"No quiz state found for user {user_id}")
            await query.message.reply_text("Quiz session expired. Please start a new quiz with /start")
            return
        
        questions = state["questions"]
        answers = state["answers"]
        correct_count = state["correct_count"]
        total_questions = len(questions)
        
        percentage = (correct_count / total_questions) * 100
        
        # Calculate time taken
        start_time = state["start_time"]
        end_time = datetime.now()
        time_taken = end_time - start_time
        
        # Format time taken
        total_seconds = int(time_taken.total_seconds())
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        
        if minutes > 0:
            time_display = f"{minutes} min {seconds} sec"
        else:
            time_display = f"{seconds} sec"
        
        # Save results to database
        try:
            save_quiz_result(
                user_id=user_id,
                topic=state["topic"],
                level=state["level"],
                score=correct_count,
                total=total_questions,
                percentage=percentage,
                time_seconds=total_seconds,
            )
        except Exception as db_error:
            logger.error(f"Database save error: {db_error}")
            # Continue anyway - user should still see results
        
        # Build review message header
        topic_name = "Grammar" if state["topic"] == "grammar" else "Vocabulary"
        review_header = f""" Quiz Complete!

📊 Final Score: {correct_count}/{total_questions} ({percentage:.1f}%)
⏱️ Time Taken: {time_display}

{'🎉 Excellent!' if percentage >= 80 else '👍 Good job!' if percentage >= 60 else '💪 Keep practicing!'}

═══════════════════════
   COMPLETE REVIEW
═══════════════════════

"""
        
        # Build review for each question - simpler format to avoid length issues
        review_questions = []
        
        for i, (question_data, answer_data) in enumerate(zip(questions, answers)):
            question_text = question_data["q"]
            options = question_data["options"]
            selected_idx = answer_data["selected"]
            correct_idx = answer_data["correct"]
            is_correct = answer_data["is_correct"]
            
            status = "✅" if is_correct else "❌"
            
            # Shortened format to fit more in one message
            q_review = f"{status} Q{i+1}. {question_text}\n"
            q_review += f"   You: {chr(65+selected_idx)}. {options[selected_idx]}\n"
            if not is_correct:
                q_review += f"   ✓ {chr(65+correct_idx)}. {options[correct_idx]}\n"
            q_review += "\n"
            
            review_questions.append(q_review)
        
        # Combine all reviews
        full_review = review_header + "".join(review_questions)
        
        # Add footer
        full_review += "═══════════════════════\n\nWant to practice more? Use /start"
        
        # Clear quiz state before sending
        del user_quiz_state[user_id]
        
        # Prepare keyboard
        keyboard = [[InlineKeyboardButton("<= Main Menu", callback_data="back_to_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Try to send as single message first
        try:
            await query.edit_message_text(full_review, reply_markup=reply_markup)
            logger.info(f"Review sent successfully for user {user_id}")
        except Exception as telegram_error:
            logger.error(f"Telegram edit error: {telegram_error}")
            # If edit fails, send as new message
            try:
                await query.message.reply_text(full_review, reply_markup=reply_markup)
                logger.info(f"Review sent as new message for user {user_id}")
            except Exception as reply_error:
                logger.error(f"Failed to send review: {reply_error}")
                # Last resort - send simple summary
                simple_message = f""" Quiz Complete!

📊 Score: {correct_count}/{total_questions} ({percentage:.1f}%)
⏱️ Time: {time_display}

Use /start to practice more!"""
                await query.message.reply_text(simple_message, reply_markup=reply_markup)
                
    except Exception as e:
        logger.error(f"Critical error in show_final_review: {e}")
        # Make sure user can continue even if review fails
        keyboard = [[InlineKeyboardButton("<= Main Menu", callback_data="back_to_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        try:
            await query.message.reply_text(
                "Quiz completed! There was an issue showing the review. Use /start to try again.",
                reply_markup=reply_markup
            )
        except:
            pass  # If even this fails, user will need to use /start manually


async def show_score(query, user_id):
    """Show user's latest scores and statistics"""
    stats = get_user_stats(user_id)
    
    if not stats:
        text = """
📊 Your Scores

You haven't taken any quizzes yet!
Start practicing with /start
        """
    else:
        # Format average times
        def format_time(seconds):
            if seconds == 0:
                return "N/A"
            minutes = int(seconds // 60)
            secs = int(seconds % 60)
            if minutes > 0:
                return f"{minutes}m {secs}s"
            return f"{secs}s"
        
        overall_time = format_time(stats['overall_time'])
        grammar_time = format_time(stats['grammar_time'])
        vocab_time = format_time(stats['vocabulary_time'])
        
        text = f"""
📊 Your Performance Statistics

🎯 Total Quizzes: {stats['total_quizzes']}
⏱️ Average Time: {overall_time}

+ Grammar:
   • Quizzes: {stats['grammar_count']}
   • Avg Score: {stats['grammar_avg']:.1f}%
   • Avg Time: {grammar_time}

+ Vocabulary:
   • Quizzes: {stats['vocabulary_count']}
   • Avg Score: {stats['vocabulary_avg']:.1f}%
   • Avg Time: {vocab_time}

Overall Accuracy: {stats['overall_avg']:.1f}%

Keep practicing to improve! 💪
        """
    
    keyboard = [[InlineKeyboardButton("⬅️ Back to Menu", callback_data="back_to_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text, reply_markup=reply_markup)


async def show_performance(query, user_id):
    """Generate and send performance chart"""
    history = get_user_history(user_id)
    
    if not history or len(history) < 2:
        text = """
📈 Performance Chart

You need at least 2 quiz attempts to see your progress chart.
Keep practicing!
        """
        keyboard = [[InlineKeyboardButton("<= Back to Menu", callback_data="back_to_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text, reply_markup=reply_markup)
        return
    
    # Generate chart
    chart_buffer = generate_performance_chart(history)
    
    # Send chart as photo
    await query.message.reply_photo(
        photo=chart_buffer,
        caption=f"Your Progress Chart\n\nTotal Quizzes: {len(history)}\nKeep up the great work! 🎓"
    )
    
    # Show menu again
    await show_main_menu_after_chart(query)


def generate_performance_chart(history):
    """Create a line chart showing score progression over time"""
    dates = [datetime.fromisoformat(h['date']) for h in history]
    scores = [h['percentage'] for h in history]
    
    plt.figure(figsize=(10, 6))
    plt.plot(dates, scores, marker='o', linewidth=2, markersize=8, color='#2E86AB')
    
    # Formatting
    plt.title('Your English Practice Progress', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Score (%)', fontsize=12)
    plt.ylim(0, 105)
    plt.grid(True, alpha=0.3)
    
    # Format x-axis dates
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    plt.gcf().autofmt_xdate()
    
    # Add a horizontal line at 80% (good performance)
    plt.axhline(y=80, color='green', linestyle='--', alpha=0.5, label='Target (80%)')
    plt.legend()
    
    # Save to buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    plt.close()
    
    return buffer


async def show_main_menu(query):
    """Show main menu"""
    keyboard = [
        [InlineKeyboardButton("📘 Grammar", callback_data="topic_grammar")],
        [InlineKeyboardButton("📗 Vocabulary", callback_data="topic_vocabulary")],
        [InlineKeyboardButton("📊 My Score", callback_data="my_score")],
        [InlineKeyboardButton("📈 My Performance", callback_data="my_performance")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = """
Main Menu

Choose what you want to do:
• Practice Grammar or Vocabulary
• Check your scores
• View your progress chart
    """
    
    await query.edit_message_text(text, reply_markup=reply_markup)


async def show_main_menu_after_chart(query):
    """Show main menu after sending chart"""
    keyboard = [
        [InlineKeyboardButton("📘 Grammar", callback_data="topic_grammar")],
        [InlineKeyboardButton("📗 Vocabulary", callback_data="topic_vocabulary")],
        [InlineKeyboardButton("📊 My Score", callback_data="my_score")],
        [InlineKeyboardButton("📈 My Performance", callback_data="my_performance")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = "What would you like to do next?"
    
    await query.message.reply_text(text, reply_markup=reply_markup)


async def score_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /score command"""
    user_id = update.effective_user.id
    stats = get_user_stats(user_id)
    
    if not stats:
        text = "You haven't taken any quizzes yet! Use /start to begin."
    else:
        # Format average times
        def format_time(seconds):
            if seconds == 0:
                return "N/A"
            minutes = int(seconds // 60)
            secs = int(seconds % 60)
            if minutes > 0:
                return f"{minutes}m {secs}s"
            return f"{secs}s"
        
        overall_time = format_time(stats['overall_time'])
        
        text = f"""
📊 Your Statistics

Total Quizzes: {stats['total_quizzes']}
Overall Accuracy: {stats['overall_avg']:.1f}%
Average Time: {overall_time}

Grammar: {stats['grammar_avg']:.1f}%
Vocabulary: {stats['vocabulary_avg']:.1f}%
        """
    
    await update.message.reply_text(text)


async def performance_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /performance command"""
    user_id = update.effective_user.id
    history = get_user_history(user_id)
    
    if not history or len(history) < 2:
        await update.message.reply_text(
            "You need at least 2 quiz attempts to see your progress chart.\n"
            "Keep practicing!"
        )
        return
    
    chart_buffer = generate_performance_chart(history)
    await update.message.reply_photo(
        photo=chart_buffer,
        caption=f"📈 Your Progress Chart\n\nTotal Quizzes: {len(history)}"
    )


def main():
    """Start the bot"""
    # Initialize database
    init_db()
    
    # Get bot token from environment variable
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not token:
        raise ValueError(
            "No TELEGRAM_BOT_TOKEN found in environment variables!\n"
            "Please set it in Render dashboard."
        )
    
    # Create application
    application = Application.builder().token(token).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("score", score_command))
    application.add_handler(CommandHandler("performance", performance_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Check if running on Render (webhook mode) or locally (polling mode)
    port = os.environ.get("PORT")
    
    if port:
        # Render Web Service mode with webhook
        webhook_url = os.environ.get("RENDER_EXTERNAL_URL")
        if not webhook_url:
            raise ValueError(
                "RENDER_EXTERNAL_URL not found! This should be auto-set by Render.\n"
                "Format: https://your-service.onrender.com"
            )
        
        logger.info(f"Starting bot in WEBHOOK mode on port {port}")
        logger.info(f"Webhook URL: {webhook_url}")
        
        # Start webhook
        application.run_webhook(
            listen="0.0.0.0",
            port=int(port),
            url_path=token,  # Use token as secret path
            webhook_url=f"{webhook_url}/{token}",
        )
    else:
        # Local development mode with polling
        logger.info("Starting bot in POLLING mode (local development)")
        application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
