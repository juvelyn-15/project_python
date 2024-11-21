from nicegui import ui
from flashcard_backend import FlashcardManager
from typing import List, Dict, Optional

class FlashcardStudyPanel:
    def __init__(self):
        self.flashcard_manager = FlashcardManager()
        self.current_topic: Optional[str] = None
        self.cards: List[Dict[str, str]] = []
        self.current_index: int = 0
        self.is_flipped: bool = False
        self.ui_elements: Dict = {}
        
        # Main container with blurred background
        self.main_container = ui.column().classes('w-full min-h-screen items-center p-4') \
                .style('width: 144%; height: 80px; padding: 20px;').classes('p-8 flex-1') \
                .style('background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(20px);')
        
        # Create containers for different views
        with self.main_container:
            # New initial selection view
            self.initial_view = ui.column().classes('w-full max-w-4xl items-center gap-8')
            
            # Existing views
            self.topic_view = ui.column().classes('w-full max-w-4xl items-center gap-4')
            self.topic_view.visible = False
            
            self.flashcard_view = ui.column().classes('w-full max-w-4xl items-center gap-4')
            self.flashcard_view.visible = False
        
        # Setup views
        self.setup_initial_view()
        #self.setup_topic_view()
        self.setup_flashcard_view()

    def setup_initial_view(self) -> None:
        """Initialize the initial flashcard mode selection view."""
        with self.initial_view:
            with ui.row().classes('w-full items-center gap-4 mb-6'):
                ui.icon('school', size='32px').classes('text-pink-600')
                ui.label('FLASHCARD STUDY').classes('text-2xl font-bold text-pink-600')
            
            # Create a grid for buttons
            with ui.grid(columns=3).classes('w-full gap-4'):
                # Default Flashcards Button
                with ui.card().classes('hover:shadow-lg transition-shadow duration-200'):
                    with ui.column().classes('p-4 gap-2 items-center'):
                        ui.icon('library_books', size='48px').classes('text-pink-600')
                        ui.label('Default Flashcards').classes('text-xl font-semibold text-gray-800')
                        word_count = sum(self.flashcard_manager.get_default_card_count(topic) 
                                         for topic in self.flashcard_manager.get_default_topics())
                        ui.label(f'{word_count} cards').classes('text-sm text-gray-600')
                        ui.button(
                            'Study Now', 
                            on_click=self.show_default_topics
                        ).props('rounded').classes('bg-pink text-white px-4 py-2 hover:bg-pink-700')

                # Personal Flashcards Button
                with ui.card().classes('hover:shadow-lg transition-shadow duration-200'):
                    with ui.column().classes('p-4 gap-2 items-center'):
                        ui.icon('person', size='48px').classes('text-pink-600')
                        ui.label('Personal Flashcards').classes('text-xl font-semibold text-gray-800')
                        word_count = sum(self.flashcard_manager.get_personal_card_count(topic) 
                                         for topic in self.flashcard_manager.get_personal_topic())
                        ui.label(f'{word_count} cards').classes('text-sm text-gray-600')
                        ui.button(
                            'Study Now', 
                            on_click=self.show_personal_topics
                        ).props('rounded').classes('bg-pink text-white px-4 py-2 hover:bg-pink-700')

                # Add New Flashcards Button
                with ui.card().classes('hover:shadow-lg transition-shadow duration-200'):
                    with ui.column().classes('p-4 gap-2 items-center'):
                        ui.icon('add', size='48px').classes('text-pink-600')
                        ui.label('Create Flashcards').classes('text-xl font-semibold text-gray-800')
                        ui.label('Add new cards').classes('text-sm text-gray-600')
                        ui.button(
                            'Create', 
                            on_click=self.show_create_flashcards
                        ).props('rounded').classes('bg-pink text-white px-4 py-2 hover:bg-pink-700')

    def show_default_topics(self) -> None:
        """Switch to default topics view."""
        self.initial_view.visible = False
        self.topic_view.visible = True
        self._create_default_topic_cards()

    def show_personal_topics(self) -> None:
        """Switch to personal topics view."""
        self.initial_view.visible = False
        self.topic_view.visible = True
        self.create_personal_topic_cards()

    def show_create_flashcards(self) -> None:
        """Open dialog to create new flashcards."""
        with ui.dialog() as dialog, ui.card():
            ui.label('Create New Flashcard').classes('text-xl font-bold')
            
            # Input fields for a new card
            topic_input = ui.select(
                self.flashcard_manager.get_default_topics() + 
                self.flashcard_manager.get_personal_topic(),
                label='Topic'
            ).classes('w-full')
            
            word_input = ui.input('Word/Term').classes('w-full')
            info_input = ui.input('Definition/Info').classes('w-full')
            
            with ui.row().classes('w-full justify-end gap-4 mt-4'):
                ui.button('Cancel', on_click=dialog.close).classes('text-gray-600')
                ui.button('Save Card', on_click=lambda: self._save_new_card(
                    topic_input.value, 
                    word_input.value, 
                    info_input.value, 
                    dialog
                )).classes('bg-pink text-white')
            
            dialog.open()


    def show_topic_view(self) -> None:
        """Switch back to initial view."""
        self.flashcard_view.visible = False
        self.topic_view.visible = False
        self.initial_view.visible = True
        self.current_topic = None
        self.cards = []

    # ... [rest of the existing methods remain the same]

def main():
    FlashcardStudyPanel()
    ui.run(title='Flashcard Study App')

if __name__ in {"__main__", "__mp_main__"}:
    main()