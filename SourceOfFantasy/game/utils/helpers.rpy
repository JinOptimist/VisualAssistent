# Вспомогательные функции

init python:
    import random
    
    def roll_dice(sides=6):
        """Бросает кости с указанным количеством граней"""
        return random.randint(1, sides)
    
    def calculate_success_chance(base_chance, modifiers):
        """Рассчитывает шанс успеха с модификаторами"""
        total_chance = base_chance
        for modifier in modifiers:
            total_chance += modifier
        return max(0, min(100, total_chance))
    
    def format_gold(amount):
        """Форматирует количество золота для отображения"""
        if amount >= 1000:
            return f"{amount/1000:.1f}k"
        return str(amount)
    
    def format_exp(amount):
        """Форматирует количество опыта для отображения"""
        if amount >= 1000:
            return f"{amount/1000:.1f}k"
        return str(amount)
    
    def get_rarity_color(rarity):
        """Возвращает цвет для редкости предмета"""
        colors = {
            "common": "#FFFFFF",      # Белый
            "uncommon": "#1EFF1E",    # Зеленый
            "rare": "#0070FF",        # Синий
            "epic": "#A335EE",        # Фиолетовый
            "legendary": "#FF8000"    # Оранжевый
        }
        return colors.get(rarity, "#FFFFFF")
    
    def get_rarity_name(rarity):
        """Возвращает название редкости на русском"""
        names = {
            "common": "Обычный",
            "uncommon": "Необычный",
            "rare": "Редкий",
            "epic": "Эпический",
            "legendary": "Легендарный"
        }
        return names.get(rarity, "Неизвестный")
    
    def calculate_level_exp(level):
        """Рассчитывает количество опыта для достижения уровня"""
        return int(100 * (level ** 1.5))
    

    

    

    

    

    
    def save_game_state():
        """Сохраняет состояние всех систем игры"""
        # Эта функция будет реализована позже для сохранения прогресса
        pass
    
    def load_game_state():
        """Загружает состояние всех систем игры"""
        # Эта функция будет реализована позже для загрузки прогресса
        pass
    
    def reset_game_state():
        """Сбрасывает состояние всех систем игры"""
        # Сбрасываем все системы к начальным значениям
        battle_system.reset_battle()
        inventory_system.__init__()
        current_location = "town_square" 