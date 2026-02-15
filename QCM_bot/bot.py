#!/usr/bin/env python3
# bot.py
# 🤖 English Learning Telegram Bot
# Uses long polling (perfect for PythonAnywhere free hosting)

import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Import our questions database
from questions import QUESTIONS

# ============================================
# 🔐 CONFIGURATION
# ============================================
# IMPORTANT: Put your Telegram bot token here
# Get it from @BotFather on Telegram
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

# Enable logging to see what's happening
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ============================================
# 💾 SIMPLE USER DATA STORAGE
# ============================================
# Stores user scores in memory (resets when bot restarts)
# For permanent storage, you can use SQLite later
user_data = {}

def get_user_score(user_id):
    """Get or create user score data"""
    if user_id not in user_data:
        user_data[user_id] = {
            'grammar_correct': 0,
            'grammar_total': 0,
            'vocabulary_correct': 0,
            'vocabulary_total': 0,
            'current_category': None,
            'current_level': None,
            'current_question_index': 0,
            'quiz_start_correct': 0,  # Score when quiz started
            'quiz_start_total': 0      # Total when quiz started
        }
    return user_data[user_id]

# ============================================
# 📱 COMMAND HANDLERS
# ============================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command - Show main menu"""
    user = update.effective_user
    
    # Create main menu keyboard
    keyboard = [
        [InlineKeyboardButton("📘 Grammar", callback_data='category_grammar')],
        [InlineKeyboardButton("📗 Vocabulary", callback_data='category_vocabulary')],
        [InlineKeyboardButton("📊 My Score", callback_data='show_score')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_message = f"""
👋 Welcome {user.first_name}!

I'm your English Learning Bot! 🎓

Practice grammar and vocabulary with multiple-choice questions.

Choose a category to start:
    """
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# ============================================
# 🎯 CALLBACK HANDLERS (Button Clicks)
# ============================================

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all button clicks"""
    query = update.callback_query
    await query.answer()  # Acknowledge the button click
    
    user_id = query.from_user.id
    data = query.data
    
    # ---- CATEGORY SELECTION (Grammar or Vocabulary) ----
    if data.startswith('category_'):
        category = data.replace('category_', '')
        await show_level_menu(query, user_id, category)
    
    # ---- LEVEL SELECTION (A1, A2, B1, etc.) ----
    elif data.startswith('level_'):
        level = data.replace('level_', '')
        await start_quiz(query, user_id, level)
    
    # ---- ANSWER SELECTION ----
    elif data.startswith('answer_'):
        answer_index = int(data.replace('answer_', ''))
        await check_answer(query, user_id, answer_index)
    
    # ---- NEXT QUESTION ----
    elif data == 'next_question':
        await show_question(query, user_id)
    
    # ---- QUIZ RESULTS ----
    elif data == 'quiz_results':
        await show_quiz_results(query, user_id)
    
    # ---- SHOW SCORE ----
    elif data == 'show_score':
        await show_score(query, user_id)
    
    # ---- BACK TO MAIN MENU ----
    elif data == 'main_menu':
        await show_main_menu(query)

# ============================================
# 📋 MENU FUNCTIONS
# ============================================

async def show_level_menu(query, user_id, category):
    """Show level selection (A1-C2)"""
    user_score = get_user_score(user_id)
    user_score['current_category'] = category
    
    # Create level buttons
    keyboard = [
        [InlineKeyboardButton("A1 (Beginner)", callback_data='level_A1'),
         InlineKeyboardButton("A2 (Elementary)", callback_data='level_A2')],
        [InlineKeyboardButton("B1 (Intermediate)", callback_data='level_B1'),
         InlineKeyboardButton("B2 (Upper-Intermediate)", callback_data='level_B2')],
        [InlineKeyboardButton("C1 (Advanced)", callback_data='level_C1'),
         InlineKeyboardButton("C2 (Proficiency)", callback_data='level_C2')],
        [InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    category_emoji = "📘" if category == "grammar" else "📗"
    message = f"{category_emoji} Choose your level for {category.upper()}:"
    
    await query.edit_message_text(message, reply_markup=reply_markup)

async def show_main_menu(query):
    """Show main menu"""
    keyboard = [
        [InlineKeyboardButton("📘 Grammar", callback_data='category_grammar')],
        [InlineKeyboardButton("📗 Vocabulary", callback_data='category_vocabulary')],
        [InlineKeyboardButton("📊 My Score", callback_data='show_score')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text("Choose a category:", reply_markup=reply_markup)

# ============================================
# ❓ QUIZ FUNCTIONS
# ============================================

async def start_quiz(query, user_id, level):
    """Start a quiz session"""
    user_score = get_user_score(user_id)
    category = user_score['current_category']
    
    # Save current level and reset question index
    user_score['current_level'] = level
    user_score['current_question_index'] = 0
    
    # Save score at start of quiz (for calculating quiz-specific results)
    if category == 'grammar':
        user_score['quiz_start_correct'] = user_score['grammar_correct']
        user_score['quiz_start_total'] = user_score['grammar_total']
    else:
        user_score['quiz_start_correct'] = user_score['vocabulary_correct']
        user_score['quiz_start_total'] = user_score['vocabulary_total']
    
    # Check if questions exist for this level
    if level not in QUESTIONS[category] or len(QUESTIONS[category][level]) == 0:
        await query.edit_message_text(
            f"❌ No questions available for {category.upper()} - {level} yet.\n\n"
            "The teacher will add them soon!",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')
            ]])
        )
        return
    
    # Show first question
    await show_question(query, user_id)

async def show_question(query, user_id):
    """Display current question with answer options"""
    user_score = get_user_score(user_id)
    category = user_score['current_category']
    level = user_score['current_level']
    q_index = user_score['current_question_index']
    
    questions = QUESTIONS[category][level]
    
    # Check if quiz is finished
    if q_index >= len(questions):
        await show_quiz_results(query, user_id)
        return
    
    # Get current question
    question = questions[q_index]
    
    # Create answer buttons (2 per row)
    keyboard = []
    for i, option in enumerate(question['options']):
        if i % 2 == 0:
            keyboard.append([InlineKeyboardButton(option, callback_data=f'answer_{i}')])
        else:
            keyboard[-1].append(InlineKeyboardButton(option, callback_data=f'answer_{i}'))
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    category_emoji = "📘" if category == "grammar" else "📗"
    message = f"""
{category_emoji} {category.upper()} - Level {level}

Question {q_index + 1}/{len(questions)}:

{question['q']}
    """
    
    await query.edit_message_text(message, reply_markup=reply_markup)

async def check_answer(query, user_id, answer_index):
    """Check if the selected answer is correct"""
    user_score = get_user_score(user_id)
    category = user_score['current_category']
    level = user_score['current_level']
    q_index = user_score['current_question_index']
    
    questions = QUESTIONS[category][level]
    question = questions[q_index]
    
    # Check if answer is correct
    is_correct = (answer_index == question['answer'])
    
    # Update score
    if category == 'grammar':
        user_score['grammar_total'] += 1
        if is_correct:
            user_score['grammar_correct'] += 1
    else:
        user_score['vocabulary_total'] += 1
        if is_correct:
            user_score['vocabulary_correct'] += 1
    
    # Show feedback
    correct_answer = question['options'][question['answer']]
    selected_answer = question['options'][answer_index]
    
    if is_correct:
        feedback = f"✅ Correct!\n\n'{selected_answer}' is the right answer!"
    else:
        feedback = f"❌ Wrong!\n\nYou selected: '{selected_answer}'\nCorrect answer: '{correct_answer}'"
    
    # Move to next question index
    user_score['current_question_index'] += 1
    
    # Check if there are more questions
    if user_score['current_question_index'] >= len(questions):
        # Quiz finished - show results
        keyboard = [[InlineKeyboardButton("📊 See Results", callback_data='quiz_results')]]
    else:
        # More questions available
        keyboard = [[InlineKeyboardButton("➡️ Next Question", callback_data='next_question')]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(feedback, reply_markup=reply_markup)

async def show_quiz_results(query, user_id):
    """Show results after completing all questions"""
    user_score = get_user_score(user_id)
    category = user_score['current_category']
    level = user_score['current_level']
    
    questions = QUESTIONS[category][level]
    quiz_total = len(questions)
    
    # Get current totals
    if category == 'grammar':
        current_correct = user_score['grammar_correct']
    else:
        current_correct = user_score['vocabulary_correct']
    
    # Calculate this quiz's score using saved start values
    quiz_correct = current_correct - user_score['quiz_start_correct']
    percentage = (quiz_correct / quiz_total * 100) if quiz_total > 0 else 0
    
    category_emoji = "📘" if category == "grammar" else "📗"
    
    message = f"""
🎉 Quiz Complete!

{category_emoji} {category.upper()} - Level {level}

Your Score: {quiz_correct}/{quiz_total}
Percentage: {percentage:.1f}%

{'🌟 Perfect!' if percentage == 100 else '💪 Keep practicing!'}
    """
    
    keyboard = [
        [InlineKeyboardButton("📊 My Total Score", callback_data='show_score')],
        [InlineKeyboardButton("🔄 Try Again", callback_data=f'level_{level}')],
        [InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(message, reply_markup=reply_markup)

async def show_score(query, user_id):
    """Show user's total score"""
    user_score = get_user_score(user_id)
    
    # Grammar stats
    g_correct = user_score['grammar_correct']
    g_total = user_score['grammar_total']
    g_percentage = (g_correct / g_total * 100) if g_total > 0 else 0
    
    # Vocabulary stats
    v_correct = user_score['vocabulary_correct']
    v_total = user_score['vocabulary_total']
    v_percentage = (v_correct / v_total * 100) if v_total > 0 else 0
    
    message = f"""
📊 YOUR TOTAL SCORE

📘 GRAMMAR:
✅ Correct: {g_correct}/{g_total}
📈 Success Rate: {g_percentage:.1f}%

📗 VOCABULARY:
✅ Correct: {v_correct}/{v_total}
📈 Success Rate: {v_percentage:.1f}%

Keep learning! 🎓
    """
    
    keyboard = [[InlineKeyboardButton("🏠 Main Menu", callback_data='main_menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(message, reply_markup=reply_markup)

# ============================================
# 🚀 MAIN FUNCTION - START THE BOT
# ============================================

def main():
    """Start the bot"""
    print("🤖 Starting English Learning Bot...")
    
    # Check if token is configured
    if BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        print("❌ ERROR: Please set your Telegram bot token!")
        print("   1. Talk to @BotFather on Telegram")
        print("   2. Create a new bot and get your token")
        print("   3. Replace 'YOUR_BOT_TOKEN_HERE' in bot.py")
        return
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    print("✅ Bot is running!")
    print("💡 Press Ctrl+C to stop")
    
    # Start the bot using LONG POLLING (perfect for PythonAnywhere)
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
