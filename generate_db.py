import sqlite3
from datetime import datetime

def generate_tables():
    # Create database instance
    db = LearningDatabase("learning.db")
    print("Database tables created successfully!")
    db.close()

class LearningDatabase:
    def __init__(self, db_name="learning.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.setup_database()

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()

    def setup_database(self):
        """Create all necessary tables if they don't exist"""
        self.connect()
        
        self.cursor.executescript('''
            -- Core user table
            CREATE TABLE IF NOT EXISTS user (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                fullname TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                birthdate DATE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            -- Dictation topics table
            CREATE TABLE IF NOT EXISTS dictation_topic (
                topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_name TEXT NOT NULL,
                difficulty_level TEXT CHECK(difficulty_level IN ('beginner', 'intermediate', 'advanced'))
            );

            -- Dictation questions table
            CREATE TABLE IF NOT EXISTS dictation_question (
                question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id INTEGER,
                question_text TEXT NOT NULL,
                correct_answer TEXT NOT NULL,
                audio_file_path TEXT,
                FOREIGN KEY (topic_id) REFERENCES dictation_topic(topic_id)
            );

            -- Reading materials table
            CREATE TABLE IF NOT EXISTS reading_material (
                material_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                reading_file_path TEXT NOT NULL,
                difficulty_level TEXT CHECK(difficulty_level IN ('beginner', 'intermediate', 'advanced')),
                estimated_time_minutes INTEGER
            );

            -- Reading comprehension questions
            CREATE TABLE IF NOT EXISTS reading_question (
                question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                material_id INTEGER,
                question_text TEXT NOT NULL,
                correct_answer TEXT NOT NULL,
                FOREIGN KEY (material_id) REFERENCES reading_material(material_id)
            );

            -- Flashcard topics table
            CREATE TABLE IF NOT EXISTS flashcard_topic (
                topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_name TEXT NOT NULL,
                description TEXT
            );

            -- Flashcards table
            CREATE TABLE IF NOT EXISTS flashcard (
                card_id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id INTEGER,
                front_content TEXT NOT NULL,
                back_content TEXT NOT NULL,
                FOREIGN KEY (card_id) REFERENCES flashcard_topic(topic_id)
            );

            -- User progress tracking for dictation
            CREATE TABLE IF NOT EXISTS user_dictation_progress (
                user_id INTEGER,
                topic_id INTEGER,
                number_of_correct_answer INTEGER,
                number_of_incorrect_answer INTEGER,
                attempt_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, topic_id, attempt_date),
                FOREIGN KEY (user_id) REFERENCES user(user_id),
                FOREIGN KEY (topic_id) REFERENCES dictation_topic(topic_id)
            );

            -- User progress tracking for reading
            CREATE TABLE IF NOT EXISTS user_reading_progress (
                user_id INTEGER,
                material_id INTEGER,
                completion_percentage REAL DEFAULT 0,
                PRIMARY KEY (user_id, material_id),
                FOREIGN KEY (user_id) REFERENCES user(user_id),
                FOREIGN KEY (material_id) REFERENCES reading_material(material_id)
            );

            -- User progress tracking for flashcards
            CREATE TABLE IF NOT EXISTS user_flashcard_progress (
                user_id INTEGER,
                card_id INTEGER,
                proficiency_level INTEGER DEFAULT 0, -- 0-5 scale
                next_review_date TIMESTAMP,
                last_review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, card_id),
                FOREIGN KEY (user_id) REFERENCES user(user_id),
                FOREIGN KEY (card_id) REFERENCES flashcard(card_id)
            );

            -- User study statistics
            CREATE TABLE IF NOT EXISTS user_study_stats (
                user_id INTEGER,
                study_date DATE,
                content_type TEXT CHECK(content_type IN ('dictation', 'reading', 'flashcard')),
                time_spent_minutes INTEGER DEFAULT 0,
                items_completed INTEGER DEFAULT 0,
                PRIMARY KEY (user_id, study_date, content_type),
                FOREIGN KEY (user_id) REFERENCES user(user_id)
            );
        ''')
        
        self.conn.commit()

    def add_user(self, username, fullname, email, birthdate, password_hash):
        """Insert a new user into the user table"""
        self.connect()
        try:
            self.cursor.execute(
                '''
                INSERT INTO user (username, fullname, email, birthdate, password_hash) 
                VALUES (?, ?, ?, ?, ?)
                ''',
                (username, fullname, email, birthdate, password_hash)
            )
            self.conn.commit()
            print("User added successfully.")
        except sqlite3.IntegrityError as e:
            print(f"Error adding user: {e}")
        #finally:
            #self.close()

    def add_flashcard(self, topic_id, front_content, back_content):
        """Add a new flashcard"""
        try:
            self.cursor.execute('''
                INSERT INTO flashcard (topic_id, front_content, back_content)
                VALUES (?, ?, ?)
            ''', (topic_id, front_content, back_content))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding flashcard: {e}")
            return None
        
    def add_flashcard_topic(self, topic_name, description=None):
        """Add a new flashcard topic"""
        try:
            self.cursor.execute('''
                INSERT INTO flashcard_topic (topic_name, description)
                VALUES (?, ?)
            ''', (topic_name, description))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding flashcard topic: {e}")
            return None
    def add_dictation_topic(self, topic_name, difficulty_level):
        """Add a new dictation topic"""
        try:
            self.cursor.execute('''
                INSERT INTO dictation_topic (topic_name, difficulty_level)
                VALUES (?, ?)
            ''', (topic_name, difficulty_level))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding dictation topic: {e}")
            return None
    def add_dictation_question(self, topic_id, question_text, correct_answer, audio_file_path=None):
        """Add a new dictation question"""
        try:
            self.cursor.execute('''
                INSERT INTO dictation_question (topic_id, question_text, correct_answer, audio_file_path)
                VALUES (?, ?, ?, ?)
            ''', (topic_id, question_text, correct_answer, audio_file_path))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding dictation question: {e}")
            return None
    def update_dictation_progress(self, user_id, topic_id, number_of_correct_answer, number_of_incorrect_answer):
        """Update user's dictation progress"""
        try:
            self.cursor.execute('''
                INSERT INTO user_dictation_progress 
                (user_id, topic_id, number_of_correct_answer, number_of_incorrect_answer)
                VALUES (?, ?, ?, ?)
            ''', (user_id, topic_id, number_of_correct_answer, number_of_incorrect_answer))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating dictation progress: {e}")
            return False
    def add_reading_material(self, title, reading_file_path, difficulty_level, estimated_time_minutes):
        """Add new reading material"""
        try:
            self.cursor.execute('''
                INSERT INTO reading_material 
                (title, reading_file_path, difficulty_level, estimated_time_minutes)
                VALUES (?, ?, ?, ?)
            ''', (title, reading_file_path, difficulty_level, estimated_time_minutes))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding reading material: {e}")
            return None
    def add_reading_question(self, material_id, question_text, correct_answer):
        """Add a reading comprehension question"""
        try:
            self.cursor.execute('''
                INSERT INTO reading_question (material_id, question_text, correct_answer)
                VALUES (?, ?, ?)
            ''', (material_id, question_text, correct_answer))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding reading question: {e}")
            return None
if __name__ == "__main__":
    db = LearningDatabase("learning.db")
    db.add_flashcard(1,"Python", "A high-level programming language.")
    db.add_dictation_topic("A litte snow", "beginner")
    db.add_dictation_question("1", "Something like that", 12, "D:\\audio.mp3")
