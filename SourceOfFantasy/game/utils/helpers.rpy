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
    
    def get_skill_name(skill_id):
        """Возвращает название навыка на русском"""
        names = {
            "sword_mastery": "Владение мечом",
            "magic_mastery": "Мастерство магии",
            "seduction_art": "Искусство соблазнения",
            "trading": "Торговля",
            "stealth": "Скрытность"
        }
        return names.get(skill_id, skill_id)
    
    def get_stat_name(stat_id):
        """Возвращает название характеристики на русском"""
        names = {
            "strength": "Сила",
            "agility": "Ловкость",
            "intelligence": "Интеллект",
            "charisma": "Харизма",
            "vitality": "Живучесть"
        }
        return names.get(stat_id, stat_id)
    
    def get_stat_description(stat_id):
        """Возвращает описание характеристики"""
        descriptions = {
            "strength": "Влияет на физический урон и переносимый вес",
            "agility": "Влияет на уклонение, критический удар и скрытность",
            "intelligence": "Влияет на магический урон, ману и изучение навыков",
            "charisma": "Влияет на соблазнение, торговлю и репутацию",
            "vitality": "Влияет на здоровье и сопротивляемость болезням"
        }
        return descriptions.get(stat_id, "Нет описания")
    
    def calculate_combat_power():
        """Рассчитывает общую боевую силу персонажа"""
        stats = progression_system.get_player_stats()
        equipment_bonuses = inventory_system.get_equipment_bonuses()
        
        power = (
            stats['strength'] * 2 +      # Сила влияет на урон
            stats['agility'] * 1.5 +     # Ловкость влияет на уклонение
            stats['intelligence'] * 1.5 + # Интеллект влияет на магию
            stats['vitality'] * 3 +      # Живучесть влияет на здоровье
            equipment_bonuses['attack'] * 3 +
            equipment_bonuses['magic_attack'] * 2 +
            equipment_bonuses['defense'] * 2
        )
        
        return int(power)
    
    def calculate_seduction_power():
        """Рассчитывает силу соблазнения персонажа"""
        stats = progression_system.get_player_stats()
        equipment_bonuses = inventory_system.get_equipment_bonuses()
        skill_level = progression_system.get_skill_level("seduction_art")
        
        power = (
            stats['charisma'] * 3 +      # Харизма - основная характеристика
            skill_level * 5 +            # Уровень навыка
            equipment_bonuses['charisma'] * 2 +
            seduction_system.player_confidence * 2
        )
        
        return int(power)
    
    def get_player_title():
        """Возвращает титул игрока на основе уровня и репутации"""
        level = progression_system.player_level
        reputation = progression_system.player_reputation
        
        if level >= 20:
            if reputation >= 8:
                return "Легендарный герой"
            elif reputation >= 5:
                return "Прославленный воин"
            else:
                return "Опасный преступник"
        elif level >= 15:
            if reputation >= 5:
                return "Опытный авантюрист"
            else:
                return "Известный разбойник"
        elif level >= 10:
            if reputation >= 3:
                return "Умелый путешественник"
            else:
                return "Подозрительный тип"
        elif level >= 5:
            return "Новичок"
        else:
            return "Неопытный искатель приключений"
    
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
        seduction_system.reset_seduction()
        progression_system.__init__()
        inventory_system.__init__()
        current_location = "town_square" 