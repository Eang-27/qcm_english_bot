"""
Database module for storing and retrieving quiz results
Uses SQLite for simple, file-based storage
"""

import sqlite3
from datetime import datetime
from typing import Dict, List, Optional


DB_NAME = "quiz_bot.db"


def init_db():
    """Initialize database and create tables if they don't exist"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create quiz_results table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            topic TEXT NOT NULL,
            level TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            percentage REAL NOT NULL,
            date TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully")


def save_quiz_result(
    user_id: int,
    topic: str,
    level: str,
    score: int,
    total: int,
    percentage: float
):
    """Save a quiz result to the database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    date = datetime.now().isoformat()
    
    cursor.execute("""
        INSERT INTO quiz_results (user_id, topic, level, score, total, percentage, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, topic, level, score, total, percentage, date))
    
    conn.commit()
    conn.close()


def get_user_stats(user_id: int) -> Optional[Dict]:
    """Get user's overall statistics"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Get total quizzes
    cursor.execute("""
        SELECT COUNT(*) FROM quiz_results WHERE user_id = ?
    """, (user_id,))
    total_quizzes = cursor.fetchone()[0]
    
    if total_quizzes == 0:
        conn.close()
        return None
    
    # Get grammar stats
    cursor.execute("""
        SELECT COUNT(*), AVG(percentage)
        FROM quiz_results
        WHERE user_id = ? AND topic = 'grammar'
    """, (user_id,))
    grammar_data = cursor.fetchone()
    grammar_count = grammar_data[0] or 0
    grammar_avg = grammar_data[1] or 0.0
    
    # Get vocabulary stats
    cursor.execute("""
        SELECT COUNT(*), AVG(percentage)
        FROM quiz_results
        WHERE user_id = ? AND topic = 'vocabulary'
    """, (user_id,))
    vocab_data = cursor.fetchone()
    vocab_count = vocab_data[0] or 0
    vocab_avg = vocab_data[1] or 0.0
    
    # Get overall average
    cursor.execute("""
        SELECT AVG(percentage)
        FROM quiz_results
        WHERE user_id = ?
    """, (user_id,))
    overall_avg = cursor.fetchone()[0] or 0.0
    
    conn.close()
    
    return {
        "total_quizzes": total_quizzes,
        "grammar_count": grammar_count,
        "grammar_avg": grammar_avg,
        "vocabulary_count": vocab_count,
        "vocabulary_avg": vocab_avg,
        "overall_avg": overall_avg,
    }


def get_user_history(user_id: int) -> List[Dict]:
    """Get user's quiz history ordered by date"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT date, topic, level, score, total, percentage
        FROM quiz_results
        WHERE user_id = ?
        ORDER BY date ASC
    """, (user_id,))
    
    results = cursor.fetchall()
    conn.close()
    
    history = []
    for row in results:
        history.append({
            "date": row[0],
            "topic": row[1],
            "level": row[2],
            "score": row[3],
            "total": row[4],
            "percentage": row[5],
        })
    
    return history


def get_latest_results(user_id: int, limit: int = 5) -> List[Dict]:
    """Get user's latest quiz results"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT date, topic, level, score, total, percentage
        FROM quiz_results
        WHERE user_id = ?
        ORDER BY date DESC
        LIMIT ?
    """, (user_id, limit))
    
    results = cursor.fetchall()
    conn.close()
    
    latest = []
    for row in results:
        latest.append({
            "date": row[0],
            "topic": row[1],
            "level": row[2],
            "score": row[3],
            "total": row[4],
            "percentage": row[5],
        })
    
    return latest
