# 🎯 Student Setup Guide - Step by Step

This guide will help you set up your English practice bot in **less than 15 minutes**!

---

## 📋 What You'll Need

- ✅ A Telegram account
- ✅ A GitHub account (free)
- ✅ A Render account (free)

No programming experience needed! Just follow these steps.

---

## 🚀 STEP 1: Create Your Bot on Telegram

### 1. Open Telegram
- On your phone or computer

### 2. Find BotFather
- Search for: `@BotFather`
- This is Telegram's official bot creator

### 3. Create Your Bot
- Send command: `/newbot`
- BotFather will ask you questions:

**Question 1: "What's your bot name?"**
- Type: `My English Practice Bot` (or any name you like)

**Question 2: "What's your bot username?"**
- Type: `my_english_bot` (must end with "bot")
- Must be unique! If taken, try: `studentname_english_bot`

### 4. SAVE YOUR TOKEN
- BotFather will send you a **bot token**
- Looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`
- **IMPORTANT**: Copy this token! You'll need it later.

✅ **Step 1 Complete!** You now have a Telegram bot.

---

## 📁 STEP 2: Upload Code to GitHub

### 1. Create GitHub Account
- Go to: https://github.com
- Click "Sign up"
- Follow instructions (it's free!)

### 2. Create New Repository
- Click the **"+"** icon (top right)
- Select **"New repository"**

### 3. Configure Repository
- **Repository name**: `english-practice-bot`
- **Description**: `Telegram bot for English practice`
- **Public** or **Private**: Choose Public
- ✅ Check "Add a README file"
- Click **"Create repository"**

### 4. Upload Bot Files
- Click **"Add file"** → **"Upload files"**
- Drag and drop these 5 files:
  1. `bot.py`
  2. `database.py`
  3. `grammar_questions.py`
  4. `vocabulary_questions.py`
  5. `requirements.txt`

- Click **"Commit changes"** (green button at bottom)

✅ **Step 2 Complete!** Your code is on GitHub.

---

## 🌐 STEP 3: Deploy to Render (Make Bot Live!)

### 1. Create Render Account
- Go to: https://render.com
- Click **"Get Started"**
- Sign up with your **GitHub account** (easiest option)

### 2. Connect GitHub
- Render will ask to access your GitHub
- Click **"Authorize Render"**
- Allow access to your `english-practice-bot` repository

### 3. Create Background Worker
- In Render dashboard, click **"New +"**
- Select **"Background Worker"**

### 4. Select Your Repository
- Choose `english-practice-bot` from the list
- Click **"Connect"**

### 5. Configure Service
Fill in these fields:

**Name**: 
```
english-practice-bot
```

**Region**: 
- Choose closest to you (e.g., Frankfurt, Oregon)

**Branch**: 
```
main
```

**Runtime**: 
```
Python 3
```

**Build Command**: 
```
pip install -r requirements.txt
```

**Start Command**: 
```
python bot.py
```

**Instance Type**: 
- Select **"Free"** (0€/month)

### 6. Add Environment Variable (CRITICAL!)
- Scroll down to **"Environment Variables"**
- Click **"Add Environment Variable"**

**Key**: 
```
TELEGRAM_BOT_TOKEN
```

**Value**: 
```
(Paste your bot token from Step 1 here)
```

Example: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

- Click **"Save"**

### 7. Deploy!
- Click **"Create Background Worker"** (blue button at bottom)
- Wait 2-3 minutes while Render builds your bot
- Watch the logs - you should see:
  ```
  ✅ Database initialized successfully
  Bot started successfully!
  ```

✅ **Step 3 Complete!** Your bot is LIVE!

---

## 🎉 STEP 4: Test Your Bot

### 1. Open Telegram
- On your phone or computer

### 2. Search for Your Bot
- Type your bot username (e.g., `@my_english_bot`)

### 3. Start Chatting
- Send command: `/start`
- You should see:
  ```
  👋 Welcome!
  
  Choose what you want to practice:
  📘 Grammar
  📗 Vocabulary
  📊 My Score
  📈 My Performance
  ```

### 4. Try a Quiz!
- Click **📘 Grammar**
- Choose level: **A1**
- Answer 10 questions
- See your results!

✅ **Congratulations! Your bot is working!** 🎊

---

## 📱 Using Your Bot

### Main Commands:
- `/start` - Main menu
- `/score` - See your statistics
- `/performance` - View progress chart

### Taking a Quiz:
1. Choose Grammar or Vocabulary
2. Pick your level (A1 = easiest, C2 = hardest)
3. Answer 10 questions (click A, B, C, or D)
4. Get instant results!
5. Review all answers to learn from mistakes

### Tracking Progress:
- Take at least 2 quizzes
- Click **📈 My Performance**
- See a graph of your improvement!

---

## 🔧 Common Problems & Solutions

### ❌ Problem: Bot doesn't respond
**Solution**:
- Check Render dashboard → Make sure service is "Running" (green)
- Check environment variable → Token must be correct
- Try clicking "Manual Deploy" in Render

### ❌ Problem: "No questions available"
**Solution**:
- Check that question files were uploaded to GitHub
- Make sure files have `.py` extension
- Try deploying again

### ❌ Problem: Can't see performance chart
**Solution**:
- You need at least 2 quiz attempts
- Take another quiz and try again

### ❌ Problem: Forgot bot username
**Solution**:
- Open BotFather in Telegram
- Send `/mybots`
- Select your bot to see details

---

## 📊 Understanding Your Stats

### After Each Quiz:
- **Score**: How many you got correct (e.g., 7/10)
- **Percentage**: Your accuracy (e.g., 70%)
- **Review**: See all questions with:
  - ✅ = You got it right
  - ❌ = You got it wrong
  - Shows correct answer for every question

### Overall Statistics (`/score`):
- **Total Quizzes**: How many you've taken
- **Grammar Avg**: Average score on grammar quizzes
- **Vocabulary Avg**: Average score on vocabulary quizzes
- **Overall Accuracy**: Your average across all quizzes

### Performance Chart (`/performance`):
- **Line graph** showing your scores over time
- **Green line at 80%** = Target goal
- Watch your line go up as you improve!

---

## 🎯 Study Tips

### 1. Start Easy
- Begin with A1 level
- Move up when you consistently score 80%+

### 2. Practice Regularly
- Take 1-2 quizzes per day
- Consistency is key!

### 3. Review Mistakes
- Read the final review carefully
- Understand WHY answers are correct

### 4. Track Progress
- Check your performance chart weekly
- Celebrate improvements!

### 5. Mix Topics
- Alternate between Grammar and Vocabulary
- Well-rounded practice = better results

---

## 🆘 Need Help?

### Where to Check:
1. **Render Logs**: Shows error messages
   - Go to your service in Render
   - Click "Logs" tab

2. **GitHub Files**: Make sure all files are there
   - Check your repository
   - All 5 files should be visible

3. **Environment Variable**: Token is correct
   - Render → Your service → Environment
   - Check `TELEGRAM_BOT_TOKEN` value

### Still Stuck?
- Ask your teacher or classmates
- Check that you followed every step exactly
- Try creating a new bot and starting over

---

## 🎓 Learning Goals

### What You'll Practice:
- **Grammar**: Tenses, sentence structure, rules
- **Vocabulary**: Words, phrases, expressions
- **6 Levels**: A1 (Beginner) to C2 (Proficient)

### How You'll Improve:
- ✅ Immediate feedback
- ✅ Visual progress tracking
- ✅ Learn from mistakes
- ✅ Regular practice

---

## 🌟 Success Checklist

Before considering your setup complete, verify:

- [ ] Bot responds to `/start`
- [ ] Can select Grammar or Vocabulary
- [ ] Can choose level (A1-C2)
- [ ] Questions appear with 4 options
- [ ] Can answer all 10 questions
- [ ] See final score and review
- [ ] Stats show in `/score`
- [ ] Chart appears after 2+ quizzes

If all checked ✅ - **Perfect! You're ready to learn!**

---

## 📅 Next Steps

1. **Today**: Complete setup, take first quiz
2. **This Week**: Take 1 quiz per day
3. **This Month**: Complete at least 20 quizzes
4. **Track**: Watch your performance chart improve!

---

**Remember**: Learning a language takes time and practice. This bot is your personal tutor, available 24/7. Use it regularly and watch your English skills grow! 🚀

---

**Questions? Ask your teacher or check the main README.md file!**

Good luck! 🍀📚
