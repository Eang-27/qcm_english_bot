# 👨‍🏫 Teacher's Guide - Managing the English Practice Bot

This guide explains how to customize questions, monitor usage, and expand the bot's capabilities.

---

## 📚 Table of Contents

1. [Adding New Questions](#adding-new-questions)
2. [Question Writing Guidelines](#question-writing-guidelines)
3. [Understanding the Database](#understanding-the-database)
4. [Viewing Student Statistics](#viewing-student-statistics)
5. [Customizing the Bot](#customizing-the-bot)
6. [Common Modifications](#common-modifications)

---

## ➕ Adding New Questions

### Quick Reference

**File Locations**:
- Grammar: `grammar_questions.py`
- Vocabulary: `vocabulary_questions.py`

### Step-by-Step Process

#### 1. Open the Appropriate File

For grammar questions, edit `grammar_questions.py`:
```python
GRAMMAR_QUESTIONS = {
    "A1": [ ... ],
    "A2": [ ... ],
    "B1": [ ... ],
    "B2": [ ... ],
    "C1": [ ... ],
    "C2": [ ... ],
}
```

#### 2. Locate the Correct Level

Each level is a list of question dictionaries. Example for A1:
```python
"A1": [
    {
        "q": "She ___ a student.",
        "options": ["am", "is", "are", "be"],
        "answer": 1  # Index of correct answer (0=first, 1=second, etc.)
    },
    {
        "q": "I ___ from France.",
        "options": ["am", "is", "are", "be"],
        "answer": 0
    },
    # Add more questions here
],
```

#### 3. Add Your Question

**Template**:
```python
{
    "q": "Your question text here with ___ for blank",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": X  # Replace X with 0, 1, 2, or 3
},
```

**Complete Example**:
```python
{
    "q": "They ___ to the park every Sunday.",
    "options": ["go", "goes", "going", "gone"],
    "answer": 0  # "go" is correct
},
```

#### 4. Important Syntax Rules

✅ **DO**:
- Use 4 options per question
- Put a comma after each question dictionary
- Use 0 for first option, 1 for second, 2 for third, 3 for fourth
- Keep consistent formatting

❌ **DON'T**:
- Forget the comma after `}`
- Use answer numbers outside 0-3 range
- Mix up the answer index
- Leave empty options

#### 5. Test Your Questions

After adding questions:
1. Push changes to GitHub
2. Render will auto-deploy (or manually deploy)
3. Test in Telegram:
   - Select the level you edited
   - Take a quiz
   - Verify questions appear correctly

---

## 📝 Question Writing Guidelines

### CEFR Level Descriptions

**A1 - Beginner**:
- Basic grammar: present simple, "to be", basic questions
- Simple vocabulary: everyday objects, family, numbers
- Example: "I ___ a teacher." → "am"

**A2 - Elementary**:
- Past simple, present continuous, comparatives
- Common phrases, daily activities
- Example: "Yesterday, I ___ to the cinema." → "went"

**B1 - Intermediate**:
- Present perfect, conditionals, passive voice
- Work, travel, experiences vocabulary
- Example: "If I ___ you, I would accept." → "were"

**B2 - Upper Intermediate**:
- Advanced conditionals, reported speech, inversions
- Abstract concepts, formal language
- Example: "Rarely ___ such beauty." → "have I seen"

**C1 - Advanced**:
- Complex grammar structures, subtle differences
- Academic, professional vocabulary
- Example: "The evidence was ___ by testimony." → "corroborated"

**C2 - Proficient**:
- Nuanced language, idiomatic expressions
- Sophisticated vocabulary, near-native level
- Example: "The argument is ___ on assumptions." → "predicated"

### Best Practices

#### 1. Clear Questions
- Use `___` to indicate the blank
- Make sure only ONE answer is correct
- Avoid ambiguous wording

#### 2. Plausible Distractors
- All 4 options should seem possible
- Don't make wrong answers obviously wrong
- Test similar grammatical structures

**Good Example**:
```python
{
    "q": "She ___ to London three times.",
    "options": [
        "has been",      # Correct
        "was",           # Common mistake
        "has gone",      # Common confusion
        "is being"       # Grammatically plausible
    ],
    "answer": 0
}
```

**Bad Example**:
```python
{
    "q": "She ___ to London three times.",
    "options": [
        "has been",      # Correct
        "banana",        # Obviously wrong
        "very",          # Not a verb
        "12345"          # Nonsense
    ],
    "answer": 0
}
```

#### 3. Appropriate Difficulty
- Match question complexity to level
- Don't put C1 questions in A1 level
- Gradually increase difficulty within each level

#### 4. Variety
- Mix question types (fill-in-blank, choose correct form)
- Include different grammar topics
- Vary vocabulary themes

---

## 🗄️ Understanding the Database

### Database Structure

The bot uses SQLite to store quiz results in `quiz_bot.db`.

**Table: quiz_results**
```sql
- id: Unique quiz identifier
- user_id: Telegram user ID (identifies student)
- topic: "grammar" or "vocabulary"
- level: "A1", "A2", "B1", "B2", "C1", "C2"
- score: Number correct (0-10)
- total: Total questions (always 10)
- percentage: (score/total) × 100
- date: When quiz was taken (ISO format)
```

### Example Database Entry
```
id: 1
user_id: 123456789
topic: grammar
level: B1
score: 8
total: 10
percentage: 80.0
date: 2024-02-10T14:30:00
```

### Accessing the Database

If you want to view student data directly:

#### Option 1: Use Render Shell
1. Go to your service in Render
2. Click "Shell" tab
3. Run: `sqlite3 quiz_bot.db`
4. Query: `SELECT * FROM quiz_results;`

#### Option 2: Download Database
1. In Render, go to "Shell"
2. Run: `cat quiz_bot.db > /tmp/db_backup.db`
3. Download the file
4. Open with SQLite browser on your computer

---

## 📊 Viewing Student Statistics

### Built-in Features

Students can see their own stats with:
- `/score` - Overall statistics
- `/performance` - Progress chart

### Manual Queries (Advanced)

If you want to see ALL students' data:

```sql
-- Total quizzes per student
SELECT user_id, COUNT(*) as total_quizzes
FROM quiz_results
GROUP BY user_id;

-- Average score by level
SELECT level, AVG(percentage) as avg_score
FROM quiz_results
GROUP BY level;

-- Most common quiz type
SELECT topic, COUNT(*) as count
FROM quiz_results
GROUP BY topic;

-- Recent activity
SELECT user_id, date, topic, level, percentage
FROM quiz_results
ORDER BY date DESC
LIMIT 20;
```

### Creating Reports

You can export data and create reports:

```python
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('quiz_bot.db')

# Load all data
df = pd.read_sql_query("SELECT * FROM quiz_results", conn)

# Create summary
summary = df.groupby('user_id').agg({
    'score': 'mean',
    'percentage': 'mean',
    'id': 'count'
}).rename(columns={'id': 'total_quizzes'})

print(summary)
```

---

## 🎨 Customizing the Bot

### 1. Change Number of Questions per Quiz

In `bot.py`, find this line:
```python
quiz_questions = random.sample(questions, min(10, len(questions)))
```

Change `10` to any number (e.g., `15` for 15 questions):
```python
quiz_questions = random.sample(questions, min(15, len(questions)))
```

**Also update** the display text in `show_question()`:
```python
text = f"""
📝 {topic_name} - Level {state['level']}

Question {question_index + 1}/15  # ← Change this
```

### 2. Add Explanations to Answers

Modify question format to include explanations:

**In question files**:
```python
{
    "q": "She ___ a student.",
    "options": ["am", "is", "are", "be"],
    "answer": 1,
    "explanation": "We use 'is' with 'she' (third person singular)."
},
```

**In `bot.py`**, modify `show_final_review()`:
```python
# After showing correct answer, add:
if "explanation" in question_data:
    review_text += f"💡 {question_data['explanation']}\n\n"
```

### 3. Add Timer per Question

**In `bot.py`**, add to `user_quiz_state`:
```python
user_quiz_state[user_id] = {
    "topic": topic,
    "level": level,
    "questions": quiz_questions,
    "current_index": 0,
    "answers": [],
    "correct_count": 0,
    "start_time": datetime.now(),  # Add this
}
```

**Track time per question**:
```python
async def process_answer(query, user_id, question_index, selected_option):
    # ... existing code ...
    
    time_taken = (datetime.now() - state["start_time"]).seconds
    state["answers"].append({
        "selected": selected_option,
        "correct": correct_answer,
        "is_correct": is_correct,
        "time": time_taken  # Add this
    })
    
    state["start_time"] = datetime.now()  # Reset for next question
```

### 4. Add Achievement Badges

Create a new achievements system:

```python
def check_achievements(user_id):
    stats = get_user_stats(user_id)
    badges = []
    
    if stats['total_quizzes'] >= 10:
        badges.append("🏆 Practice Master (10 quizzes)")
    
    if stats['overall_avg'] >= 90:
        badges.append("⭐ Excellent Student (90% average)")
    
    if stats['grammar_count'] >= 5 and stats['vocabulary_count'] >= 5:
        badges.append("🎯 Balanced Learner")
    
    return badges
```

### 5. Multiple Language Support

Add translations:

```python
MESSAGES = {
    "en": {
        "welcome": "Welcome!",
        "choose_topic": "Choose what you want to practice:",
        # ... more translations
    },
    "es": {
        "welcome": "¡Bienvenido!",
        "choose_topic": "Elige lo que quieres practicar:",
        # ... more translations
    }
}

# In bot code:
lang = "en"  # Get from user preference
welcome_text = MESSAGES[lang]["welcome"]
```

---

## 🔧 Common Modifications

### Add New Levels

To add a "Pre-A1" level:

**1. Add to question files**:
```python
GRAMMAR_QUESTIONS = {
    "Pre-A1": [
        # Your easiest questions
    ],
    "A1": [ ... ],
    # ... rest
}
```

**2. Update level selection in `bot.py`**:
```python
keyboard = [
    [
        InlineKeyboardButton("Pre-A1", callback_data=f"level_{topic}_Pre-A1"),
        InlineKeyboardButton("A1", callback_data=f"level_{topic}_A1"),
    ],
    # ... rest
]
```

### Change Quiz Categories

Instead of Grammar/Vocabulary, use Reading/Listening:

**1. Create new question files**:
- `reading_questions.py`
- `listening_questions.py`

**2. Update imports in `bot.py`**:
```python
from reading_questions import READING_QUESTIONS
from listening_questions import LISTENING_QUESTIONS
```

**3. Update menu**:
```python
keyboard = [
    [InlineKeyboardButton("📖 Reading", callback_data="topic_reading")],
    [InlineKeyboardButton("🎧 Listening", callback_data="topic_listening")],
    # ...
]
```

### Add Difficulty Rating

Let students rate question difficulty:

**After quiz**, add rating buttons:
```python
keyboard = [
    [InlineKeyboardButton("😊 Easy", callback_data="rate_easy")],
    [InlineKeyboardButton("😐 Medium", callback_data="rate_medium")],
    [InlineKeyboardButton("😰 Hard", callback_data="rate_hard")],
]
```

Store ratings in database for analytics.

---

## 📈 Monitoring & Analytics

### Key Metrics to Track

1. **Engagement**:
   - Total active users
   - Quizzes per day
   - Average session length

2. **Performance**:
   - Average score by level
   - Improvement rate over time
   - Most failed questions

3. **Content Quality**:
   - Questions with lowest success rate
   - Topics needing more questions
   - Level difficulty balance

### Creating Analytics Dashboard

```python
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('quiz_bot.db')
cursor = conn.cursor()

# Get daily quiz counts
cursor.execute("""
    SELECT DATE(date) as day, COUNT(*) as count
    FROM quiz_results
    GROUP BY day
    ORDER BY day
""")

data = cursor.fetchall()
dates, counts = zip(*data)

plt.plot(dates, counts)
plt.title('Daily Quiz Activity')
plt.xlabel('Date')
plt.ylabel('Number of Quizzes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('analytics.png')
```

---

## 🎓 Pedagogical Tips

### Question Design

1. **Test Understanding, Not Memory**
   - Focus on applying rules, not recalling facts
   - Use context clues in questions

2. **Progressive Difficulty**
   - Start each level with easier questions
   - End with challenging ones

3. **Real-World Relevance**
   - Use authentic language examples
   - Include current, relevant vocabulary

### Using Data to Improve Teaching

1. **Identify Weak Areas**
   - Which grammar topics have lowest scores?
   - Focus classroom time on difficult concepts

2. **Track Individual Progress**
   - Monitor student improvement over weeks
   - Provide targeted support when needed

3. **Adjust Question Bank**
   - Replace questions with 100% success rate (too easy)
   - Add more practice for <60% success questions

---

## 🆘 Troubleshooting for Teachers

### Students Report Issues

**"Questions are too hard"**
- Review question difficulty for that level
- Add more A1/A2 questions
- Consider adding hints

**"Same questions appear"**
- Ensure at least 15-20 questions per level
- Questions are randomly selected from pool

**"Chart doesn't show"**
- Student needs 2+ quiz attempts
- Check matplotlib is installed

### Technical Issues

**Bot stops responding**
- Check Render service status
- Review logs for errors
- Verify bot token is correct

**Questions not updating**
- Ensure changes are pushed to GitHub
- Trigger manual deploy in Render
- Check file syntax (commas, brackets)

**Database errors**
- Database file may be corrupted
- Download backup from Render
- Re-initialize if needed

---

## 📚 Resources

### Learning More

- Python Telegram Bot docs: https://docs.python-telegram-bot.org/
- SQLite tutorial: https://www.sqlitetutorial.net/
- Matplotlib gallery: https://matplotlib.org/stable/gallery/

### Community

- Share questions with other teachers
- Create collaborative question banks
- Discuss best practices

---

**Happy Teaching! 👨‍🏫📚**

This bot is a tool to enhance your teaching, not replace it. Use it to reinforce lessons, track progress, and motivate students to practice independently!
