# Константы игры

init python:
    # Игровые константы
    GAME_VERSION = "0.1"
    GAME_TITLE = "Source of Fantasy"
    
    # Константы боевой системы
    BASE_ATTACK_DAMAGE = 1
    BASE_MAGIC_DAMAGE = 2
    BASE_HEALTH = 10
    BASE_MANA = 10
    MAX_LEVEL = 50
    

    
    # Константы инвентаря
    MAX_INVENTORY_SIZE = 20
    MAX_EQUIPMENT_SLOTS = 3
    

    
    # Константы экономики
    STARTING_GOLD = 100
    STARTING_LEVEL = 1
    
    # Цвета для интерфейса
    COLORS = {
        "health": "#FF4444",
        "mana": "#4444FF",
        "exp": "#44FF44",
        "gold": "#FFD700",
        "success": "#00FF00",
        "failure": "#FF0000",
        "warning": "#FFFF00",
        "info": "#00FFFF"
    }
    
    # Типы предметов
    ITEM_TYPES = {
        "weapon": "Оружие",
        "armor": "Броня",
        "accessory": "Аксессуар",
        "consumable": "Расходник",
        "material": "Материал",
        "quest": "Квестовый предмет"
    }
    
    # Редкости предметов
    RARITIES = {
        "common": {"name": "Обычный", "color": "#FFFFFF", "chance": 60},
        "uncommon": {"name": "Необычный", "color": "#1EFF1E", "chance": 25},
        "rare": {"name": "Редкий", "color": "#0070FF", "chance": 10},
        "epic": {"name": "Эпический", "color": "#A335EE", "chance": 4},
        "legendary": {"name": "Легендарный", "color": "#FF8000", "chance": 1}
    }
    
    # Типы действий
    ACTION_TYPES = {
        "battle": "Бой",
        "trade": "Торговля",
        "quest": "Квест",
        "rest": "Отдых"
    }
    

    

    
    # Достижения
    ACHIEVEMENTS = {
        "first_victory": {"name": "Первая победа", "description": "Победите в первом бою"},
        "wealthy": {"name": "Богач", "description": "Накопите 1000 золота"}
    }
    
    # Сообщения системы
    SYSTEM_MESSAGES = {
        "level_up": "Уровень повышен!",
        "skill_up": "Навык улучшен!",
        "item_found": "Найден предмет: {item_name}",
        "gold_gained": "Получено золота: {amount}",
        "achievement_unlocked": "Достижение разблокировано: {achievement_name}",
        "battle_victory": "Победа!",
        "battle_defeat": "Поражение!"
    }
    
    # Настройки игры
    GAME_SETTINGS = {
        "auto_save": True,
        "show_tooltips": True,
        "sound_enabled": True,
        "music_enabled": True,
        "difficulty": "normal"  # easy, normal, hard
    } 