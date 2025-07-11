import sqlite3

conn = sqlite3.connect("translation_logs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS translations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_text TEXT,
    target_lang TEXT,
    translated_text TEXT
)
''')
conn.commit()

def log_request(text, lang, translated):
    cursor.execute('''
    INSERT INTO translations (original_text, target_lang, translated_text)
    VALUES (?, ?, ?)
    ''', (text, lang, translated))
    conn.commit()
