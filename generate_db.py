import sqlite3
from datetime import datetime
import os

class LearningDatabase:
    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), "learning.db")
        self.db_name = db_path
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
                status TEXT DEFAULT 'off' CHECK(status in ('on', 'off')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );


            -- Flashcard topics table
            CREATE TABLE IF NOT EXISTS personal_flashcard_topic (
                topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                topic_name TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user(user_id)
            );

            -- Flashcards table
            CREATE TABLE IF NOT EXISTS flashcard (
                card_id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id INTEGER,
                front_content TEXT NOT NULL,
                back_content TEXT NOT NULL,
                FOREIGN KEY (topic_id) REFERENCES personal_flashcard_topic(topic_id)
            );
                                  
            -- User progress tracking for review words
            CREATE TABLE IF NOT EXISTS user_review (
                user_id INTEGER,
                review_id INTEGER PRIMARY KEY AUTOINCREMENT,
                front_content TEXT NOT NULL,
                back_content TEXT NOT NULL,
                last_review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(user_id)
            );
                                  
            
            -- User study statistics
            CREATE TABLE IF NOT EXISTS user_study_stats (
                user_id INTEGER,
                study_date DATE,
                time_spent_minutes INTEGER DEFAULT 0,
                items_completed INTEGER DEFAULT 0,
                PRIMARY KEY (user_id, study_date),
                FOREIGN KEY (user_id) REFERENCES user(user_id)
            );
        ''')
        
        self.conn.commit()

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
                INSERT INTO personal_flashcard_topic (topic_name, description)
                VALUES (?, ?)
            ''', (topic_name, description))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding flashcard topic: {e}")
            return None
    def add_user_review(self, user_id, front_content, back_content):
        """Add a new user review record"""
        try:
        # Thực hiện câu lệnh INSERT
            self.cursor.execute('''
                INSERT INTO user_review (user_id, front_content, back_content )
                VALUES (?, ?, ?)
            ''', (user_id, front_content, back_content))
        
        # Ghi thay đổi vào cơ sở dữ liệu
            self.conn.commit()
            review_id = self.cursor.lastrowid  # Get the auto-generated review_id
        # Xác nhận nếu thêm thành công
            print(f"User review added: user_id={user_id}")
            return True
        except sqlite3.Error as e:
        # Thông báo lỗi nếu xảy ra
            print(f"Error adding user review: {e}")
            return False
    def delete_review_card(self, user_id, review_id):
        """Delete a review card from the user_review table"""
        try:
        # Thực hiện câu lệnh DELETE với điều kiện user_id và review_id
            self.cursor.execute('''
                DELETE FROM user_review
                WHERE user_id = ? AND review_id = ?
            ''', (user_id, review_id))
            self.conn.commit()
           
            print(f"Review card deleted: user_id={user_id}, review_id={review_id}")
            return True
        except sqlite3.Error as e:
            print(f"Error deleting review card: {e}")
            return False
    def count_all_reviews(self):
        """Count the total number of words (flashcards) in the user_review table"""
        try:
        # Truy vấn đếm tổng số từ trong bảng user_review
            self.cursor.execute('''
                SELECT COUNT(*) 
                FROM user_review
            ''')
            count = self.cursor.fetchone()[0]  # Lấy kết quả đầu tiên từ truy vấn
            print(f"Total words in review: {count}")  # In ra tổng số từ
            return count
        except sqlite3.Error as e:
            print(f"Error counting all reviews: {e}")
            return None
    def load_user_review_album(self, user_id):
        """Load all front_content and back_content for a specific user into review_album"""
        try:
        # Truy vấn để lấy tất cả front_content và back_content của user_id
            self.cursor.execute('''
                SELECT front_content, back_content
                FROM user_review
                WHERE user_id = ?
            ''', (user_id,))
            # Lấy tất cả kết quả từ truy vấn
            rows = self.cursor.fetchall()
        
            # Lưu vào album review_album
            review_album = [(row[0], row[1]) for row in rows]
            # Xóa toàn bộ các review card của user_id đó
            self.cursor.execute('''
                DELETE FROM user_review
                WHERE user_id = ?
             ''', (user_id,))
        
             # Ghi nhận thay đổi
            self.conn.commit()
            
            print(f"Loaded {len(review_album)} review cards for user_id={user_id}")
            return review_album
        except sqlite3.Error as e:
            print(f"Error loading review album: {e}")
            return []


db = LearningDatabase()