# backend/data.py
topic_flashcards = {
    "Nghề nghiệp": [
        {"word": "chef", "info": "đầu bếp"},
        {"word": "comedian", "info": "diễn viên hài"},
        {"word": "delivery man", "info": "nhân viên giao hàng"},
        {"word": "doctor", "info": "bác sĩ"},
        {"word": "entrepreneur", "info": "nhà kinh doanh"},
        {"word": "engineer", "info": "kỹ sư"},
        {"word": "factory worker", "info": "công nhân nhà máy"},
        {"word": "office worker", "info": "nhân viên văn phòng"},
        {"word": "florist", "info": "người bán hoa"},
        {"word": "hairdresser", "info": "thợ cắt tóc"},
    ],
    "Trái cây": [
        {"word": "pear", "info": "quả lê"},
        {"word": "grape", "info": "quả nho"},
        {"word": "peach", "info": "quả đào"},
        {"word": "orange", "info": "quả cam"},
        {"word": "mango", "info": "quả xoài"},
        {"word": "coconut", "info": "quả dừa"},
        {"word": "pineapple", "info": "quả dứa"},
        {"word": "watermelon", "info": "dưa hấu"},
        {"word": "durian", "info": "sầu riêng"},
        {"word": "lychee", "info": "quả vải"},
        {"word": "guava", "info": "quả ổi"},
        {"word": "starfruit", "info": "quả khế"},
    ],
    "Gia đình": [
        {"word": "parent", "info": "bố hoặc mẹ"},
        {"word": "daughter", "info": "con gái"},
        {"word": "son", "info": "con trai"},
        {"word": "sibling", "info": "anh chị em ruột"},
        {"word": "sister", "info": "chị, em gái"},
        {"word": "brother", "info": "anh, em trai"},
        {"word": "grandmother", "info": "bà nội (ngoại)"},
        {"word": "grandfather", "info": "ông nội (ngoại)"},
        {"word": "grandparent", "info": "ông hoặc bà"},
        {"word": "relative", "info": "họ hàng"},
        {"word": "aunt", "info": "cô, dì"},
        {"word": "uncle", "info": "chú, bác, cậu, dượng"},
    ],
    "Động Vật": [
        {"word": "mouse", "info": "con chuột"},
        {"word": "cat", "info": "con mèo"},
        {"word": "dog", "info": "con chó"},
        {"word": "kitten", "info": "mèo con"},
        {"word": "puppy", "info": "chó con"},
        {"word": "pig", "info": "con lợn, heo"},
        {"word": "chicken", "info": "con gà"},
        {"word": "duck", "info": "con vịt"},
        {"word": "goose", "info": "con ngỗng"},
        {"word": "turkey", "info": "con gà tây"},
        {"word": "stork", "info": "con cò"},
        {"word": "swan", "info": "thiên nga"},
    ],
    "Rau Quả": [
        {"word": "bean", "info": "hạt đậu"},
        {"word": "pea", "info": "đậu Hà Lan"},
        {"word": "cabbage", "info": "bắp cải"},
        {"word": "carrot", "info": "củ cà rốt"},
        {"word": "corn", "info": "ngô, bắp"},
        {"word": "cucumber", "info": "dưa chuột"},
        {"word": "tomato", "info": "quả cà chua"},
        {"word": "garlic", "info": "tỏi"},
        {"word": "onion", "info": "củ hành"},
        {"word": "spring onion", "info": "hành lá"},
        {"word": "ginger", "info": "củ gừng"},
        {"word": "turmeric", "info": "củ nghệ"},
        {"word": "potato", "info": "khoai tây"},
        {"word": "sweet potato", "info": "khoai lang"},
    ],
    "Đồ Ăn": [
        {"word": "soup", "info": "món súp, món canh"},
        {"word": "salad", "info": "rau trộn, nộm rau"},
        {"word": "bread", "info": "bánh mì"},
        {"word": "sausage", "info": "xúc xích"},
        {"word": "hot dog", "info": "bánh mỳ kẹp xúc xích"},
        {"word": "bacon", "info": "thịt xông khói"},
        {"word": "ham", "info": "thịt giăm bông"},
        {"word": "egg", "info": "trứng"},
        {"word": "pork", "info": "thịt lợn"},
        {"word": "beef", "info": "thịt bò"},
        {"word": "chicken", "info": "thịt gà"},
        {"word": "duck", "info": "thịt vịt"},
        {"word": "lamb", "info": "thịt cừu"},
        {"word": "ribs", "info": "sườn"},
    ],
    "Động tác cơ thể": [
        {"word": "tiptoe", "info": "đi nhón chân"},
        {"word": "jump", "info": "nhảy"},
        {"word": "leap", "info": "nhảy vọt, nhảy xa"},
        {"word": "stand", "info": "đứng"},
        {"word": "sit", "info": "ngồi"},
        {"word": "lean", "info": "dựa, tựa"},
        {"word": "wave", "info": "vẫy tay"},
        {"word": "clap", "info": "vỗ tay"},
        {"word": "point", "info": "chỉ, trỏ"},
        {"word": "catch", "info": "bắt, đỡ"},
        {"word": "stretch", "info": "vươn (vai..), ưỡn lưng"},
        {"word": "push", "info": "đẩy"},
        {"word": "pull", "info": "kéo"},
        {"word": "crawl", "info": "bò, trườn"},
    ],
    'Bộ phận cơ thế': [
    {"word": "head", "info": "đầu"},
    {"word": "hair", "info": "tóc"},
    {"word": "face", "info": "gương mặt"},
    {"word": "forehead", "info": "trán"},
    {"word": "eyebrow", "info": "lông mày"},
    {"word": "eye", "info": "mắt"},
    {"word": "eyelash", "info": "lông mi"},
    {"word": "nose", "info": "mũi"},
    {"word": "ear", "info": "tai"},
    {"word": "cheek", "info": "má"} 
    ],
    'Trường học': [
    {"word": "school", "info": "trường học"},
    {"word": "class", "info": "lớp học"},
    {"word": "student", "info": "học sinh, sinh viên"},
    {"word": "pupil", "info": "học sinh"},
    {"word": "teacher", "info": "giáo viên"},
    {"word": "principal", "info": "hiệu trưởng"},
    {"word": "course", "info": "khóa học"},
    {"word": "semester", "info": "học kì"},
    {"word": "exercise", "info": "bài tập"},
    {"word": "homework", "info": "bài tập về nhà"}
    ],
    'Tính cách': [
    {"word": "active", "info": "năng nổ, lanh lợi"},
    {"word": "alert", "info": "tỉnh táo, cảnh giác"},
    {"word": "ambitious", "info": "tham vọng"},
    {"word": "attentive", "info": "chăm chú, chú tâm"},
    {"word": "bold", "info": "táo bạo, mạo hiểm"},
    {"word": "brave", "info": "dũng cảm, gan dạ"},
    {"word": "careful", "info": "cẩn thận, thận trọng"},
    {"word": "careless", "info": "bất cẩn, cẩu thả"},
    {"word": "cautious", "info": "thận trọng, cẩn thận"},
    {"word": "conscientious", "info": "chu đáo, tỉ mỉ"},
    {"word": "courageous", "info": "can đảm"}
    ],
    'Đồ dùng học tập': 
    [
    {"word": "pen", "info": "bút mực"},
    {"word": "pencil", "info": "bút chì"},
    {"word": "highlighter", "info": "bút nhớ"},
    {"word": "ruler", "info": "thước kẻ"},
    {"word": "eraser", "info": "tẩy, gôm"},
    {"word": "pencil case", "info": "hộp bút"},
    {"word": "book", "info": "quyển sách"},
    {"word": "notebook", "info": "vở"},
    {"word": "paper", "info": "giấy"},
    {"word": "scissors", "info": "kéo"}
     ],
    'Thiên nhiên ': [
    {"word": "forest", "info": "rừng"},
    {"word": "rainforest", "info": "rừng mưa nhiệt đới"},
    {"word": "mountain", "info": "núi, dãy núi"},
    {"word": "highland", "info": "cao nguyên"},
    {"word": "hill", "info": "đồi"},
    {"word": "valley", "info": "thung lũng, châu thổ, lưu vực"},
    {"word": "cave", "info": "hang động"},
    {"word": "rock", "info": "đá"},
    {"word": "slope", "info": "dốc"},
    {"word": "volcano", "info": "núi lửa"}
    ],
    'Du lịch': [
    {"word": "travel", "info": "đi du lịch"},
    {"word": "depart", "info": "khởi hành"},
    {"word": "leave", "info": "rời đi"},
    {"word": "arrive", "info": "đến nơi"},
    {"word": "airport", "info": "sân bay"},
    {"word": "take off", "info": "cất cánh"},
    {"word": "land", "info": "hạ cánh"},
    {"word": "check in", "info": "đăng ký phòng ở khách sạn"},
    {"word": "check out", "info": "trả phòng khách sạn"},
    {"word": "visit", "info": "thăm viếng"}
]
}

import uuid
from generate_db import db
class User:
    def __init__(self, username):
        self.id = str(uuid.uuid4())
        self.username = username
        self.review_history = {}  # Lưu lịch sử ôn tập theo ngày
        self.review_stats = {
            'total_reviewed': 0,
            'total_remembered': 0,
            'streak_days': 0
        }

# backend/game_logic.py
import random

class GameLogic:
    def __init__(self):
        self.albums = {}  # Dictionary lưu trữ album
        self.review_album = db.load_user_review_album(1)  # Album cho từ cần ôn tập
        self.current_word = ""
        self.current_info = ""
        self.filtered_words = []
        self.score = 0

    # Lấy danh sách các album
    def get_albums(self):
        return self.albums
    
    # Lấy danh sách các chủ đề
    def get_topics(self):
        return topic_flashcards.keys()
        

    # Lấy danh sách các chủ đề
    def get_topics(self):
        return topic_flashcards.keys()

    # Đặt nguồn từ vựng cho game (có thể là album hoặc chủ đề)
    def set_word_source(self, source, is_album=False):
        if is_album:
            self.filtered_words = [(entry["word"], entry["info"]) for entry in self.albums[source]]
        else:
            self.filtered_words = [(entry["word"], entry["info"]) for entry in topic_flashcards[source]]
        return len(self.filtered_words) > 0

    # Lấy từ tiếp theo để người dùng đoán
    def get_next_word(self):
        if not self.filtered_words:
            return None, None
        
        self.current_word, self.current_info = random.choice(self.filtered_words)
        word_letters = list(self.current_word.lower())
        random.shuffle(word_letters)
        scrambled_word = ''.join(word_letters)
        return scrambled_word, len(self.current_word)

    # Kiểm tra đáp án của người dùng
    def check_answer(self, user_input):
        if not user_input:
            return False, "empty"
        
        is_correct = user_input.lower() == self.current_word.lower()
        if is_correct:
            self.score += 1
            self.filtered_words.remove((self.current_word, self.current_info))
        else:
            if (self.current_word, self.current_info) not in self.review_album:
                self.review_album.append((self.current_word, self.current_info))
        
        return is_correct, self.current_word

    # Bỏ qua từ hiện tại
    def skip_current_word(self):
        if (self.current_word, self.current_info) not in self.review_album:
            self.review_album.append((self.current_word, self.current_info))
        return self.current_word

    # Đặt lại điểm số
    def reset_game(self):
        self.score = 0
        return self.score
    def save_review(self):
        try:
            print(self.review_album)
            success_count = 0
            for index, (front_content, back_content) in enumerate(self.review_album, start=1):
                print(front_content, back_content)
                # Sử dụng index như review_id
                # Có thể tuỳ chỉnh ngày review nếu cần
                success = db.add_user_review(user_id = 1, front_content = front_content, back_content = back_content)
                if success:
                    success_count += 1
            print(f"Saved {success_count} reviews back to user_review for user_id=1.")
            return True
        except Exception as e:
            print(f"Error saving reviews with existing function: {e}")
            return False

# backend/review_logic.py
class ReviewLogic:
    def __init__(self, game_logic, user=None):
        self.game_logic = game_logic
        self.user = user
        self.current_index = 0
        self.card_flipped = False
        self.today_stats = {
            'reviewed': 0,
            'remembered': 0
        }
    
    # Thiết lập người dùng cho logic ôn tập
    def set_user(self, user):
        self.user = user
        self.load_user_progress()

    # Tải tiến trình ôn tập của người dùng
    def load_user_progress(self):
        if self.user:
            from datetime import date
            today = date.today().isoformat()
            if today not in self.user.review_history:
                self.user.review_history[today] = {
                    'reviewed': 0,
                    'remembered': 0
                }
            self.today_stats = self.user.review_history[today]

    # Cập nhật thống kê ôn tập
    def update_review_stats(self, remembered=False):
        if self.user:
            from datetime import date
            today = date.today().isoformat()
            
            self.today_stats['reviewed'] += 1
            if remembered:
                self.today_stats['remembered'] += 1
            
            self.user.review_history[today] = self.today_stats
            self.user.review_stats['total_reviewed'] += 1
            if remembered:
                self.user.review_stats['total_remembered'] += 1

    # Lấy thẻ flashcard hiện tại để ôn tập
    def get_current_card(self):
        if not self.game_logic.review_album:
            return None, None
        word, info = self.game_logic.review_album[self.current_index]
        return info if self.card_flipped else word

    # Lật thẻ flashcard để xem định nghĩa
    def flip_card(self):
        self.card_flipped = not self.card_flipped
        return self.get_current_card()

    # Chuyển đến thẻ flashcard tiếp theo
    def next_card(self):
        if self.game_logic.review_album:
            self.current_index = (self.current_index + 1) % len(self.game_logic.review_album)
            self.card_flipped = False
        return self.get_current_card()

    # Quay lại thẻ flashcard trước đó
    def prev_card(self):
        if self.game_logic.review_album:
            self.current_index = (self.current_index - 1) % len(self.game_logic.review_album)
            self.card_flipped = False
        return self.get_current_card()

    # Đánh dấu từ đã nhớ
    def mark_as_remembered(self):
        if self.game_logic.review_album:
            removed_word = self.game_logic.review_album.pop(self.current_index)
            if self.current_index >= len(self.game_logic.review_album):
                self.current_index = max(0, len(self.game_logic.review_album) - 1)
            return removed_word[0]
        return None

    # Lấy số lượng từ cần ôn tập
    def get_review_count(self):
        return len(self.game_logic.review_album)
    
    # Lấy thống kê ôn tập của người dùng
    def get_user_stats(self):
        if not self.user:
            return None
        return {
            'today': self.today_stats,
            'total': self.user.review_stats
        }



# frontend/ui_components.py
from nicegui import ui

class GameUI:
    def __init__(self, game_logic, review_logic):
        self.game_logic = game_logic
        self.review_logic = review_logic
        self.container = None
        self.mode_container = None
        self.game_controls = None
        self.game_interface = None
        self.review_section = None
        self.score_label = None
        self.word_display = None
        self.input_box = None
        self.stats_display = None
        

    def setup_ui(self, container):
        self.container = container
        with self.container:
            self._create_header()
            self._create_mode_selection()
            self._create_game_controls()
            self._create_game_interface()
            self._create_review_section()

    def _create_header(self):
        ui.label("Trò Chơi Sắp Xếp Lại Từ").classes('text-3xl font-bold mb-4')
        with ui.row().classes('gap-4 mb-4'):
            ui.button("Album của tôi", on_click=lambda: self.show_mode_options('album')).classes('bg-blue-500')
            ui.button("Chủ đề có sẵn", on_click=lambda: self.show_mode_options('topic')).classes('bg-green-500')

    def update_stats_display(self):
        self.stats_display.clear()
        stats = self.review_logic.get_user_stats()
        if stats:
            with self.stats_display:
                ui.label(f"Người dùng: {self.review_logic.user.username}").classes('text-lg')
                ui.label(f"Hôm nay: Đã ôn {stats['today']['reviewed']} từ, nhớ {stats['today']['remembered']} từ").classes('text-sm')
                ui.label(f"Tổng cộng: Đã ôn {stats['total']['total_reviewed']} từ, nhớ {stats['total']['total_remembered']} từ").classes('text-sm')

    def _create_mode_selection(self):
        self.mode_container = ui.column().classes('w-full mb-4')

    def _create_game_controls(self):
        self.game_controls = ui.column().classes('w-full mb-4')
        with self.game_controls:
            ui.button("Bắt đầu", on_click=self.start_new_game).classes('bg-green-500')
            ui.button("Chơi lại", on_click=self.reset_game).classes('bg-yellow-500')
        self.game_controls.set_visibility(False)

    def _create_game_interface(self):
        self.game_interface = ui.column().classes('w-full')
        with self.game_interface:
            self.score_label = ui.label(f"Điểm: 0").classes('text-lg mb-2')
            self.word_display = ui.label().classes('text-xl mb-2')
            self.hint_label = ui.label().classes('text-sm text-gray-500 mb-2')
            
            with ui.row().classes('gap-2'):
                self.input_box = ui.input(placeholder='Nhập từ của bạn...').classes('w-64')
                ui.button("Kiểm tra", on_click=self.check_word).classes('bg-blue-500')
                ui.button("Bỏ qua", on_click=self.skip_word).classes('bg-gray-500')
        self.game_interface.set_visibility(False)

    def _create_review_section(self):
        self.review_section = ui.column().classes('w-full mt-4')
        with self.review_section:
            ui.label("Từ cần ôn tập").classes('text-xl font-bold mb-2')
            self.review_count_label = ui.label().classes('text-sm text-gray-600 mb-2')
            
            self.flashcard = ui.card().classes('w-full h-48 cursor-pointer mb-4')
            with self.flashcard:
                self.card_content = ui.label().classes('text-xl text-center w-full h-full flex items-center justify-center')
            
            with ui.row().classes('w-full justify-center gap-4'):
                ui.button('←', on_click=self.prev_card).classes('bg-gray-500')
                ui.button('Lật thẻ', on_click=self.flip_card).classes('bg-blue-500')
                ui.button('→', on_click=self.next_card).classes('bg-gray-500')
            
            with ui.row().classes('w-full justify-center gap-4 mt-4'):
                ui.button('Đã nhớ', on_click=self.mark_as_remembered).classes('bg-green-500')
                ui.button('Chưa nhớ', on_click=self.next_card).classes('bg-red-500')
                ui.button('Kết thúc ôn tập', on_click=self.game_logic.save_review).classes('bg-red-500')
        self.review_section.set_visibility(False)
        self.update_review_section()

    def show_mode_options(self, mode):
        self.mode_container.clear()
        with self.mode_container:
            options = (list(self.game_logic.get_albums().keys()) if mode == 'album' 
                      else list(self.game_logic.get_topics()))
            
            if mode == 'album' and not options:
                ui.label("Bạn chưa có album nào").classes('text-red-500')
                return

            ui.select(
                label="Chọn " + ("album" if mode == 'album' else "chủ đề"),
                options=options,
                on_change=lambda e: self.on_source_change(e.value, mode == 'album')
            ).classes('w-full max-w-xs mb-4')

    def on_source_change(self, source, is_album):
        if self.game_logic.set_word_source(source, is_album):
            self.game_controls.set_visibility(True)
            self.game_interface.set_visibility(False)
            self.review_section.set_visibility(True)
            self.update_review_section()

    def start_new_game(self):
        scrambled_word, word_length = self.game_logic.get_next_word()
        if not scrambled_word:
            ui.notify("Vui lòng chọn nguồn từ vựng", color="warning")
            return
        
        self.game_interface.set_visibility(True)
        self.word_display.set_text(f"Sắp xếp lại: {scrambled_word}")
        self.hint_label.set_text(f"Độ dài: {word_length} ký tự")
        self.input_box.value = ""

    def check_word(self):
        is_correct, result = self.game_logic.check_answer(self.input_box.value.strip())
        if result == "empty":
            ui.notify("Vui lòng nhập từ", color="warning")
        elif is_correct:
            ui.notify("Chính xác! +1 điểm", color="success")
            self.score_label.set_text(f"Điểm: {self.game_logic.score}")
            self.update_review_section()
        else:
            ui.notify(f"Sai rồi! Đáp án đúng: {result}", color="error")
            self.update_review_section()
        self.start_new_game()

    def skip_word(self):
        correct_word = self.game_logic.skip_current_word()
        ui.notify(f"Từ đúng là: {correct_word}", color="warning")
        self.update_review_section()
        self.start_new_game()

    def reset_game(self):
        self.game_logic.reset_game()
        self.score_label.set_text("Điểm: 0")
        self.start_new_game()

    def update_review_section(self):
        count = self.review_logic.get_review_count()
        self.review_count_label.text = f'Còn {count} từ cần ôn tập'
        
        card_content = self.review_logic.get_current_card()
        if card_content:
            self.card_content.text = card_content[0] if isinstance(card_content, tuple) else card_content
            self.flashcard.style('background-color: ' + 
                               ('#4CAF50' if self.review_logic.card_flipped else 'white') + 
                               '; color: ' + ('white' if self.review_logic.card_flipped else 'black'))
        else:
            self.card_content.text = "Không còn từ nào cần ôn tập"

    def flip_card(self):
        self.review_logic.flip_card()
        self.update_review_section()

    def next_card(self):
        self.review_logic.next_card()
        self.update_review_section()

    def prev_card(self):
        self.review_logic.prev_card()
        self.update_review_section()

    def mark_as_remembered(self):
        removed_word = self.review_logic.mark_as_remembered()
        if removed_word:
            ui.notify(f'Đã xóa "{removed_word}" khỏi danh sách ôn tập', color="success")
            self.update_review_section()
            self.update_stats_display()  # Cập nhật thống kê


# main.py
@ui.page('/')
def main():
    game_logic = GameLogic()
    user = User("TestUser") 
    review_logic = ReviewLogic(game_logic, user)
    
    with ui.column().classes('w-full max-w-3xl mx-auto p-4'):
        game_ui = GameUI(game_logic, review_logic)
        game_ui.setup_ui(ui.column().classes('w-full'))

ui.run()
