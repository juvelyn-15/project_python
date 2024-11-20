import requests
from nicegui import ui

# Backend 
class DictionaryBackend:
    def __init__(self):
        self.api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        self.albums = {}  # Lưu trữ các album flashcard

    # Lấy thông tin của từ từ API
    def get_word_info(self, word):
        """Fetch word information from the API"""
        result = requests.get(self.api_url.format(word=word))
        return result.json()

    # Tạo một album flashcard mới
    def create_album(self, name):
        """Create a new flashcard album"""
        name = name.strip()
        if not name or name in self.albums:
            return False, "Tên album không hợp lệ hoặc đã tồn tại"
        self.albums[name] = []
        return True, f"Đã tạo album: {name}"

    # Thêm một từ vào album đã chỉ định với định nghĩa tùy chỉnh tùy chọn
    def add_to_album(self, album_name, word_data, custom_definition=None):
        """Add a word to specified album with optional custom definition"""
        if album_name not in self.albums:
            return False, "Không tìm thấy album"

        word = word_data['word']
        if any(card['word'] == word for card in self.albums[album_name]):
            return False, f"'{word}' đã tồn tại trong album"

        definitions = []
        # Thêm các định nghĩa từ API
        for meaning in word_data.get('meanings', []):
            for definition in meaning.get('definitions', []):
                definitions.append({
                    'definition': definition.get('definition', ''),
                    'example': definition.get('example', ''),
                    'part_of_speech': meaning.get('partOfSpeech', ''),
                    'is_custom': False
                })

        # Thêm định nghĩa tùy chỉnh nếu có
        if custom_definition:
            definitions.append({
                'definition': custom_definition,
                'example': '',
                'part_of_speech': 'custom',
                'is_custom': True
            })

        self.albums[album_name].append({
            "word": word,
            "definitions": definitions,
            "phonetic": word_data.get('phonetic', '')
        })
        return True, f"Đã thêm '{word}' vào album '{album_name}'"

    # Lấy danh sách tất cả các tên album
    def get_albums_list(self):
        """Get list of all album names"""
        return list(self.albums.keys())