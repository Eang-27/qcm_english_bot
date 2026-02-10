# 🎯 Quick Reference Card - English Practice Bot

Print or save this for quick access to important information!

---

## 📱 Bot Commands

| Command | What It Does |
|---------|--------------|
| `/start` | Show main menu |
| `/score` | View your statistics |
| `/performance` | See progress chart |

---

## 🎮 How to Take a Quiz

1. **Start**: Send `/start`
2. **Choose**: Click 📘 Grammar or 📗 Vocabulary
3. **Level**: Select A1, A2, B1, B2, C1, or C2
4. **Answer**: Click A, B, C, or D for each question
5. **Review**: See final score and all answers
6. **Repeat**: Take another quiz to improve!

---

## 📊 CEFR Levels Guide

| Level | Name | Description |
|-------|------|-------------|
| **A1** | Beginner | Basic words, simple sentences |
| **A2** | Elementary | Everyday phrases, basic conversations |
| **B1** | Intermediate | Common situations, express opinions |
| **B2** | Upper Intermediate | Complex texts, fluent discussions |
| **C1** | Advanced | Detailed texts, professional level |
| **C2** | Proficient | Near-native mastery |

💡 **Tip**: Start at A1 and move up when you score 80%+ consistently!

---

## 🎯 Study Goals

### Daily Practice
- [ ] Take 1-2 quizzes
- [ ] Review all wrong answers
- [ ] Understand why correct answer is right

### Weekly Goals
- [ ] 7+ quizzes completed
- [ ] Check progress chart
- [ ] Identify weak topics

### Monthly Goals
- [ ] 20+ quizzes completed
- [ ] Move up one level
- [ ] Maintain 70%+ average

---

## 📈 Understanding Your Stats

### Score Display
```
Final Score: 7/10 (70%)
✅ = Correct
❌ = Wrong
```

### Statistics (`/score`)
- **Total Quizzes**: How many you've taken
- **Grammar Avg**: Average grammar score
- **Vocabulary Avg**: Average vocabulary score
- **Overall Accuracy**: Combined average

### Performance Chart (`/performance`)
- Shows score trends over time
- Green line = 80% target
- Upward trend = improving!

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Bot doesn't respond | Wait 60 seconds (may be waking up) |
| No questions available | Try different level or report to teacher |
| Chart won't show | Need at least 2 quiz attempts |
| Wrong score | Review carefully, answer may be correct |

---

## 👨‍🏫 For Teachers

### Adding Questions
1. Edit `grammar_questions.py` or `vocabulary_questions.py`
2. Add to correct level (A1-C2)
3. Follow format:
```python
{
    "q": "Question text with ___",
    "options": ["A", "B", "C", "D"],
    "answer": 0  # 0=A, 1=B, 2=C, 3=D
},
```
4. Push to GitHub
5. Render auto-deploys

### Question Format Rules
- ✅ 4 options always
- ✅ 1 correct answer
- ✅ Answer index 0-3
- ✅ Comma after each question
- ❌ No missing brackets
- ❌ No duplicate answers

---

## 🌐 Render Deployment

### Environment Variable
```
Key: TELEGRAM_BOT_TOKEN
Value: Your token from @BotFather
```

### Build Command
```bash
pip install -r requirements.txt
```

### Start Command
```bash
python bot.py
```

### Service Type
**Background Worker** (not Web Service)

---

## 📁 File Structure

```
english-practice-bot/
├── bot.py                     # Main bot logic
├── database.py                # Data storage
├── grammar_questions.py       # Grammar Q&A
├── vocabulary_questions.py    # Vocabulary Q&A
├── requirements.txt           # Dependencies
├── README.md                  # Main documentation
├── STUDENT_GUIDE.md          # Step-by-step setup
├── TEACHER_GUIDE.md          # Customization guide
└── quiz_bot.db               # Database (auto-created)
```

---

## 🔑 Important Links

### Create Bot
- BotFather: `@BotFather` on Telegram

### Hosting
- Render: https://render.com

### Documentation
- Python Telegram Bot: https://docs.python-telegram-bot.org/
- SQLite: https://www.sqlitetutorial.net/
- Matplotlib: https://matplotlib.org/

---

## ✨ Success Tips

### 1. Consistency
📅 Practice daily, even just 1 quiz

### 2. Review Mistakes
📝 Don't just check score - understand WHY

### 3. Progress Gradually
📈 Don't skip levels - master each one

### 4. Use the Chart
📊 Visual feedback is motivating!

### 5. Mix Topics
🔄 Alternate Grammar and Vocabulary

---

## 🎓 Learning Strategy

### Week 1-2: Foundation
- Start at A1 level
- Take 1-2 quizzes daily
- Aim for 70%+ scores

### Week 3-4: Building
- Move to A2 when comfortable
- Increase to 2-3 quizzes daily
- Aim for 80%+ scores

### Month 2+: Advancing
- Progress through B1, B2
- Consistent practice
- Track improvement via chart

---

## 📞 Getting Help

### Student Issues
1. Check bot username is correct
2. Try `/start` again
3. Wait if service is waking up
4. Ask teacher if problems persist

### Teacher Issues
1. Check Render logs
2. Verify environment variables
3. Test in Telegram yourself
4. Review documentation

---

## 🔐 Privacy & Security

- ✅ No names or emails stored
- ✅ Only Telegram user_id used
- ✅ Quiz results private to each student
- ✅ Bot token kept secure
- ✅ Data stays in database

---

## 💾 Data Backup (Teachers)

### Download Database
```bash
# In Render Shell:
cat quiz_bot.db > /tmp/backup.db
```

### View Data
```bash
sqlite3 quiz_bot.db
SELECT * FROM quiz_results;
```

---

## 🚀 Quick Start (Students)

1. **Open Telegram** → Search for bot
2. **Send** `/start`
3. **Choose** topic & level
4. **Answer** 10 questions
5. **Review** results
6. **Repeat** regularly!

---

## 🎯 Target Scores

| Level | Target Score | What It Means |
|-------|--------------|---------------|
| 90-100% | Excellent | Master this level! |
| 80-89% | Very Good | Almost there! |
| 70-79% | Good | Keep practicing |
| 60-69% | Fair | Review mistakes |
| Below 60% | Needs Work | Try easier level |

---

## 📅 Maintenance Schedule

### Daily (Automatic)
- ✅ Bot responds to students
- ✅ Database saves results
- ✅ Charts generate

### Weekly (Teacher)
- 📊 Check usage logs
- 🐛 Fix any reported issues
- 📝 Consider adding questions

### Monthly (Teacher)
- 🔄 Update question bank
- 📈 Review student progress
- ✨ Add new features (optional)

---

## 🏆 Achievements to Aim For

- 🥉 **Bronze**: 10 quizzes completed
- 🥈 **Silver**: 50 quizzes completed
- 🥇 **Gold**: 100 quizzes completed
- 🌟 **Star**: 90% overall average
- 🎯 **Expert**: Master all levels A1-C2

---

**Keep this card handy and practice regularly! 📚✨**

---

## Emergency Contacts

**Bot Down?**
- Wait 60 seconds (may be starting)
- Check Render service status
- Contact teacher/admin

**Questions Not Loading?**
- Try different level
- Report to teacher
- Check for updates

**Stats Not Showing?**
- Take at least 1 quiz first
- Use `/score` command
- Refresh by taking another quiz

---

**Happy Learning! 🎓🚀**
