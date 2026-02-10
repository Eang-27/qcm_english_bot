# 🎓 English Grammar & Vocabulary Practice Bot

A Telegram bot for students to practice English through multiple-choice quizzes with performance tracking and visualization.

---

## 📚 What This Bot Does

### For Students:
- ✅ Practice Grammar & Vocabulary at 6 levels (A1-C2)
- ✅ Take 10-question quizzes with instant feedback
- ✅ Review all answers after completing a quiz
- ✅ Track scores and progress over time
- ✅ View performance charts to see improvement

### Key Features:
1. **Level-Based Learning**: Choose from A1 (Beginner) to C2 (Proficient)
2. **Immediate Review**: See all questions, your answers, and correct answers after each quiz
3. **Performance Tracking**: SQLite database stores every quiz attempt
4. **Visual Progress**: Line charts show score trends over time
5. **Easy Expansion**: Add new questions without changing bot code

---

## 🗂️ Project Structure

```
english-practice-bot/
│
├── bot.py                      # Main bot logic (quiz flow, menus, handlers)
├── database.py                 # SQLite database functions
├── grammar_questions.py        # Grammar question bank (A1-C2)
├── vocabulary_questions.py     # Vocabulary question bank (A1-C2)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── quiz_bot.db                 # SQLite database (created automatically)
```

---

## 🚀 Setup Instructions

### Step 1: Create Your Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` command
3. Choose a name (e.g., "English Practice Bot")
4. Choose a username (must end in 'bot', e.g., "my_english_practice_bot")
5. **Save the bot token** (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

---

### Step 2: Deploy to Render (FREE Hosting)

#### A. Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub, GitLab, or email

#### B. Upload Your Code to GitHub
1. Create a new repository on GitHub
2. Upload all bot files:
   - `bot.py`
   - `database.py`
   - `grammar_questions.py`
   - `vocabulary_questions.py`
   - `requirements.txt`

#### C. Create Web Service on Render
1. In Render dashboard, click **"New +"** → **"Background Worker"**
2. Connect your GitHub repository
3. Configure:
   - **Name**: `english-practice-bot`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`

#### D. Add Environment Variable
1. In Render service settings, go to **"Environment"**
2. Add a new environment variable:
   - **Key**: `TELEGRAM_BOT_TOKEN`
   - **Value**: (paste your bot token from BotFather)
3. Click **"Save Changes"**

#### E. Deploy
1. Click **"Manual Deploy"** → **"Deploy latest commit"**
2. Wait 2-3 minutes for deployment
3. Check logs to see "Bot started successfully!"

---

### Step 3: Test Your Bot

1. Open Telegram
2. Search for your bot username
3. Send `/start`
4. You should see the main menu with buttons!

---

## 🎮 How to Use the Bot

### Commands:
- `/start` - Show main menu
- `/score` - View your statistics
- `/performance` - See your progress chart

### Quiz Flow:
1. Choose **Grammar** or **Vocabulary**
2. Select your level (A1-C2)
3. Answer 10 multiple-choice questions
4. See your final score
5. Review all questions with correct answers

---

## 📊 How Student Performance Tracking Works

### Database Structure
The bot uses **SQLite** (a simple file-based database) to store:

```
quiz_results table:
- id (unique quiz ID)
- user_id (Telegram user ID)
- topic (grammar or vocabulary)
- level (A1, A2, B1, B2, C1, C2)
- score (correct answers)
- total (total questions = 10)
- percentage (score ÷ total × 100)
- date (when quiz was taken)
```

### What Gets Tracked:
- Every quiz attempt is saved
- Each student's data is separate (identified by Telegram user_id)
- Statistics calculated:
  - Total quizzes taken
  - Average grammar score
  - Average vocabulary score
  - Overall accuracy percentage
  - Quiz history with dates

### Performance Chart:
- Uses **matplotlib** library
- Creates a line graph showing:
  - X-axis: Dates of quiz attempts
  - Y-axis: Percentage scores
  - Visual trend line to see improvement
- Saved as PNG image and sent to student

---

## ➕ How to Add New Questions

### Easy 3-Step Process:

#### Step 1: Open the question file
- For grammar: `grammar_questions.py`
- For vocabulary: `vocabulary_questions.py`

#### Step 2: Find the level
```python
GRAMMAR_QUESTIONS = {
    "A1": [ ... ],
    "A2": [ ... ],  # ← Add questions here for A2 level
    ...
}
```

#### Step 3: Add new questions in this format:
```python
{
    "q": "She ___ a teacher.",
    "options": ["am", "is", "are", "be"],
    "answer": 1  # Index 1 = "is" (0=first, 1=second, 2=third, 3=fourth)
},
```

⚠️ **Important**: 
- Make sure the `answer` index matches the correct option
- Use commas between questions
- Keep the same format

#### Step 4: Redeploy on Render
1. Push changes to GitHub
2. Render will auto-deploy, or click "Manual Deploy"

---

## 🛠️ Troubleshooting

### Bot not responding?
✅ Check Render logs for errors  
✅ Verify `TELEGRAM_BOT_TOKEN` is set correctly  
✅ Make sure the service is "Running" in Render dashboard

### Questions not showing?
✅ Check question file syntax (commas, brackets)  
✅ Verify at least 10 questions exist for the level

### Chart not generating?
✅ Student needs at least 2 quiz attempts  
✅ Check if `matplotlib` is installed (in requirements.txt)

### Database errors?
✅ Database auto-creates on first run  
✅ Check Render has write permissions

---

## 🎓 Educational Value

### For Students:
- **Self-paced learning**: Practice anytime, anywhere
- **Immediate feedback**: Learn from mistakes instantly
- **Progress tracking**: See improvement over time
- **Gamification**: Scores motivate continued practice

### For Teachers:
- **Easy customization**: Add relevant questions for your class
- **Free hosting**: No ongoing costs
- **Scalable**: Works for 1 or 1000 students
- **Data tracking**: See which topics need more practice

---

## 💡 Code Explanation (Simple Terms)

### bot.py
- **Main brain** of the bot
- Handles user interactions (button clicks, commands)
- Shows questions one by one
- Calculates final scores
- Generates performance charts

### database.py
- **Storage manager**
- Saves quiz results to SQLite database
- Retrieves user statistics
- Gets quiz history for charts

### grammar_questions.py & vocabulary_questions.py
- **Question banks**
- Organized by CEFR levels
- Easy to expand with new questions
- Each question = dictionary with question, options, answer

---

## 🔒 Privacy & Security

- ✅ No personal data collected (only Telegram user_id)
- ✅ Quiz results stored locally in SQLite
- ✅ No external API calls (except Telegram)
- ✅ Bot token stored securely in environment variables

---

## 📈 Future Enhancements (Ideas)

Want to improve the bot? Here are some ideas:

1. **Timer per question** (add time pressure)
2. **Leaderboards** (compare with classmates)
3. **Explanations** (show why answer is correct)
4. **Custom quizzes** (let students choose topics)
5. **Export results** (download as PDF/Excel)
6. **Admin panel** (teacher can see all student stats)
7. **Streak tracking** (practice X days in a row)
8. **Achievements** (badges for milestones)

---

## 🤝 Support

### Questions?
- Check Telegram Bot documentation: https://core.telegram.org/bots
- Python Telegram Bot library: https://docs.python-telegram-bot.org/

### Need Help?
- Review Render logs for error messages
- Check that all files are uploaded correctly
- Verify environment variables are set

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

## ✨ Credits

Built with:
- **python-telegram-bot** - Telegram Bot API wrapper
- **matplotlib** - Chart generation
- **SQLite** - Database storage

---

**Happy Learning! 🎓📚**

Start practicing English today and track your improvement over time!
