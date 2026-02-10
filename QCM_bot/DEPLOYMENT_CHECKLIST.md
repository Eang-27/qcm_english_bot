# ✅ Render Deployment Checklist

Use this checklist to ensure smooth deployment of your English Practice Bot on Render.

---

## 📋 Pre-Deployment Checklist

### 1. Files Ready
- [ ] `bot.py` - Main bot code
- [ ] `database.py` - Database functions
- [ ] `grammar_questions.py` - Grammar questions (15+ per level)
- [ ] `vocabulary_questions.py` - Vocabulary questions (15+ per level)
- [ ] `requirements.txt` - Dependencies listed

### 2. GitHub Repository
- [ ] Repository created on GitHub
- [ ] All 5 files uploaded
- [ ] Repository is accessible (public or connected to Render)

### 3. Telegram Bot
- [ ] Bot created via @BotFather
- [ ] Bot token saved securely
- [ ] Bot username noted

---

## 🌐 Render Setup Steps

### Step 1: Create Service
- [ ] Logged into Render (render.com)
- [ ] Clicked "New +" → "Background Worker"
- [ ] Selected correct GitHub repository
- [ ] Connected repository to Render

### Step 2: Configure Service

**Basic Settings**:
- [ ] Name: `english-practice-bot` (or your choice)
- [ ] Region: Selected closest region
- [ ] Branch: `main` (or `master`)
- [ ] Runtime: `Python 3`

**Build & Start**:
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `python bot.py`

**Instance Type**:
- [ ] Selected "Free" plan

### Step 3: Environment Variables

**Critical Step**:
- [ ] Clicked "Environment" section
- [ ] Added environment variable:
  - Key: `TELEGRAM_BOT_TOKEN`
  - Value: (Your bot token from BotFather)
- [ ] Saved changes

### Step 4: Deploy
- [ ] Clicked "Create Background Worker"
- [ ] Deployment started
- [ ] Waited for build to complete (2-3 minutes)

---

## 🔍 Post-Deployment Verification

### Check Logs
- [ ] Opened "Logs" tab in Render
- [ ] Saw "✅ Database initialized successfully"
- [ ] Saw "Bot started successfully!"
- [ ] No error messages visible

### Service Status
- [ ] Service shows "Running" (green indicator)
- [ ] No "Deploy failed" messages
- [ ] No "Build failed" messages

---

## 🧪 Testing the Bot

### Basic Functionality
- [ ] Opened Telegram
- [ ] Searched for bot username
- [ ] Sent `/start` command
- [ ] Received welcome message
- [ ] Saw main menu buttons

### Quiz Flow
- [ ] Clicked "📘 Grammar"
- [ ] Saw level selection (A1-C2)
- [ ] Selected a level (e.g., A1)
- [ ] First question appeared
- [ ] All 4 options visible
- [ ] Selected an answer
- [ ] Next question appeared
- [ ] Completed all 10 questions
- [ ] Received final score
- [ ] Saw complete review with:
  - [ ] All 10 questions
  - [ ] Your answers shown
  - [ ] Correct answers shown
  - [ ] ✅/❌ indicators

### Statistics
- [ ] Used `/score` command
- [ ] Saw quiz statistics
- [ ] Took another quiz
- [ ] Statistics updated

### Performance Chart
- [ ] Took at least 2 quizzes
- [ ] Used `/performance` command
- [ ] Received chart image
- [ ] Chart shows quiz progression

---

## 🔧 Troubleshooting Guide

### Issue: Bot doesn't respond to /start

**Check**:
- [ ] Service is "Running" in Render
- [ ] Bot token is correct in environment variables
- [ ] No typos in bot username

**Fix**:
- [ ] Restart service in Render (click "Manual Deploy")
- [ ] Verify token matches BotFather exactly
- [ ] Check logs for error messages

---

### Issue: "No questions available"

**Check**:
- [ ] Question files exist in GitHub
- [ ] Files have correct names
- [ ] Level has at least 10 questions

**Fix**:
- [ ] Verify files uploaded to GitHub
- [ ] Check syntax in question files (commas, brackets)
- [ ] Add more questions if needed
- [ ] Redeploy service

---

### Issue: Questions appear but answers don't work

**Check**:
- [ ] Answer index is 0-3 (not 1-4)
- [ ] Question has 4 options
- [ ] No syntax errors in question files

**Fix**:
- [ ] Review question format
- [ ] Check answer indices
- [ ] Look for missing commas
- [ ] Redeploy after fixes

---

### Issue: Performance chart doesn't show

**Check**:
- [ ] Student has taken 2+ quizzes
- [ ] `matplotlib` in requirements.txt
- [ ] No errors in logs

**Fix**:
- [ ] Take another quiz
- [ ] Try `/performance` again
- [ ] Check Render logs for matplotlib errors

---

### Issue: Database errors

**Check**:
- [ ] `database.py` file exists
- [ ] Service has write permissions
- [ ] No syntax errors in database.py

**Fix**:
- [ ] Check Render logs for specific error
- [ ] Restart service
- [ ] Re-deploy from GitHub

---

## 🚀 Optimization Tips

### After Successful Deployment

**1. Monitor Usage**:
- [ ] Check logs regularly
- [ ] Monitor for errors
- [ ] Track user engagement

**2. Improve Content**:
- [ ] Add more questions (aim for 20+ per level)
- [ ] Review question difficulty
- [ ] Fix questions with 100% success rate (too easy)

**3. Enable Auto-Deploy** (Optional):
- [ ] In Render settings
- [ ] Enable "Auto-Deploy"
- [ ] Changes in GitHub auto-deploy to Render

**4. Set Up Monitoring** (Optional):
- [ ] Enable email notifications in Render
- [ ] Get alerts if service goes down

---

## 📊 Success Metrics

Your deployment is successful when:

- ✅ Service stays "Running" for 24+ hours
- ✅ Students can complete quizzes without errors
- ✅ Statistics update correctly
- ✅ Charts generate after 2+ quizzes
- ✅ No error messages in logs

---

## 🔄 Regular Maintenance

### Weekly:
- [ ] Check Render logs for errors
- [ ] Verify service is running
- [ ] Review student usage

### Monthly:
- [ ] Add new questions
- [ ] Update based on student feedback
- [ ] Check for bot library updates

### As Needed:
- [ ] Fix reported bugs
- [ ] Improve question quality
- [ ] Add new features

---

## 📞 Getting Help

### Render Support:
- Documentation: https://render.com/docs
- Community: https://community.render.com

### Python Telegram Bot:
- Docs: https://docs.python-telegram-bot.org/
- Examples: https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples

### SQLite:
- Tutorial: https://www.sqlitetutorial.net/
- Browser: https://sqlitebrowser.org/

---

## 🎉 Final Checklist

Before announcing the bot to students:

- [ ] All tests passed
- [ ] At least 15 questions per level
- [ ] Service stable for 24+ hours
- [ ] Student guide ready
- [ ] Backup plan if service goes down
- [ ] Students know bot username
- [ ] Instructions shared with class

---

**Congratulations! Your English Practice Bot is ready for students! 🎓**

Remember: Render free tier may sleep after 15 minutes of inactivity. First message after sleep might take 30-60 seconds to wake the service.

---

## 🔐 Security Notes

- ✅ Bot token kept in environment variables (not in code)
- ✅ Database local to Render service
- ✅ No personal student data collected
- ✅ Telegram user_id is anonymous
- ✅ Repository can be private if desired

---

**Happy Deploying! 🚀**
