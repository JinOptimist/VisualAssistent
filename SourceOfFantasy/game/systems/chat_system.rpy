# Система чата для визуальной новеллы
# Управляет отображением сообщений в стиле мессенджера

default chat_system = ChatSystem()

init python:
    import time
    from datetime import datetime
    
    class ChatMessage:
        def __init__(self, sender_name, text, sender_type="other", timestamp=None):
            self.sender_name = sender_name
            self.text = text
            self.sender_type = sender_type  # "me", "other", "system"
            self.timestamp = timestamp or datetime.now()
            self.time = self.timestamp.strftime("%H:%M")
            
            # Настройка внешнего вида в зависимости от типа отправителя
            if sender_type == "me":
                self.alignment = 1.0  # Справа
                self.bubble_color = "#0099cc"  # Синий для своих сообщений
                self.name_color = "#ffffff"
                self.text_color = "#ffffff"
            elif sender_type == "system":
                self.alignment = 0.5  # По центру
                self.bubble_color = "#666666"  # Серый для системных
                self.name_color = "#ffffff"
                self.text_color = "#ffffff"
            else:
                self.alignment = 0.0  # Слева
                self.bubble_color = "#2d2d2d"  # Темно-серый для других
                self.name_color = "#0099cc"
                self.text_color = "#ffffff"
    
    class ChatSystem:
        def __init__(self):
            self.messages = []
            self.is_typing = False
            self.typing_duration = 2.0  # Длительность анимации печати
            self.typing_side = 0.0  # 0.0 - left, 1.0 - right
            self.typing_active = False
        
        def add_message(self, sender_name, text, sender_type="other"):
            """Добавляет новое сообщение в чат"""
            message = ChatMessage(sender_name, text, sender_type)
            self.messages.append(message)
            return message
        
        def add_typing_indicator(self, sender_type):
            """Показывает индикатор печати с нужной стороны"""
            if sender_type == "me":
                self.typing_side = 1.0
                self.typing_active = True
                self.is_typing = True
                renpy.restart_interaction()
            elif sender_type == "other":
                self.typing_side = 0.0
                self.typing_active = True
                self.is_typing = True
                renpy.restart_interaction()
            else:
                self.typing_active = False
                self.is_typing = False
        
        def remove_typing_indicator(self):
            """Убирает индикатор печати"""
            self.is_typing = False
            self.typing_active = False
            renpy.restart_interaction()
        
        def clear_messages(self):
            """Очищает все сообщения"""
            self.messages = []
            self.is_typing = False
            self.typing_active = False
        
        def simulate_typing(self, sender_name, text, sender_type="other", typing_time=None):
            """Симулирует печать сообщения с задержкой"""
            if typing_time is None:
                typing_time = len(text) * 0.05  # 50мс на символ
            
            # Индикатор появляется до паузы
            self.add_typing_indicator(sender_type)
            renpy.pause(typing_time)
            self.remove_typing_indicator()
            # Только после этого появляется сообщение
            result = self.add_message(sender_name, text, sender_type)
            return result

    # Функции для удобного использования в сценариях
    def chat_message(sender_name, text, sender_type="other"):
        """Добавляет сообщение в чат"""
        return chat_system.add_message(sender_name, text, sender_type)

    def chat_typing(sender_name, text, sender_type="other", typing_time=None):
        """Симулирует печать сообщения"""
        return chat_system.simulate_typing(sender_name, text, sender_type, typing_time)

    def chat_clear():
        """Очищает чат"""
        chat_system.clear_messages()

    def show_chat():
        """Показывает экран чата"""
        renpy.show_screen("chat_screen")
        renpy.restart_interaction()

    def hide_chat():
        """Скрывает экран чата"""
        renpy.hide_screen("chat_screen")
        renpy.restart_interaction() 