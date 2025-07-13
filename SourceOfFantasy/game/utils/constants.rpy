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
    
    # Константы соблазнения
    BASE_SEDUCTION_CHANCE = 50
    MAX_AFFECTION = 100
    MIN_AFFECTION = 0
    
    # Константы инвентаря
    MAX_INVENTORY_SIZE = 20
    MAX_EQUIPMENT_SLOTS = 3
    
    # Константы прокачки
    EXP_PER_LEVEL = 100
    STAT_POINTS_PER_LEVEL = 3
    MAX_SKILL_LEVEL = 10
    
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
        "seduction": "Соблазнение",
        "training": "Тренировка",
        "trade": "Торговля",
        "explore": "Исследование",
        "quest": "Квест",
        "rest": "Отдых"
    }
    
    # Статистики персонажа
    STATS = {
        "strength": {"name": "Сила", "description": "Влияет на физический урон"},
        "agility": {"name": "Ловкость", "description": "Влияет на уклонение и критический удар"},
        "intelligence": {"name": "Интеллект", "description": "Влияет на магический урон и ману"},
        "charisma": {"name": "Харизма", "description": "Влияет на соблазнение и торговлю"},
        "vitality": {"name": "Живучесть", "description": "Влияет на здоровье"}
    }
    
    # Навыки
    SKILLS = {
        "sword_mastery": {"name": "Владение мечом", "description": "Увеличивает физический урон"},
        "magic_mastery": {"name": "Мастерство магии", "description": "Увеличивает магический урон"},
        "seduction_art": {"name": "Искусство соблазнения", "description": "Увеличивает шанс успеха соблазнения"},
        "trading": {"name": "Торговля", "description": "Улучшает цены при торговле"},
        "stealth": {"name": "Скрытность", "description": "Позволяет избегать боев"}
    }
    
    # Достижения
    ACHIEVEMENTS = {
        "first_victory": {"name": "Первая победа", "description": "Победите в первом бою"},
        "seduction_master": {"name": "Мастер соблазнения", "description": "Достигните 10 уровня в искусстве соблазнения"},
        "wealthy": {"name": "Богач", "description": "Накопите 1000 золота"},
        "explorer": {"name": "Исследователь", "description": "Посетите все локации"},
        "warrior": {"name": "Воин", "description": "Достигните 10 уровня"},
        "mage": {"name": "Маг", "description": "Достигните 10 уровня в магии"},
        "lover": {"name": "Любовник", "description": "Соблазните 5 разных персонажей"}
    }
    
    # Сообщения системы
    SYSTEM_MESSAGES = {
        "level_up": "Уровень повышен!",
        "skill_up": "Навык улучшен!",
        "item_found": "Найден предмет: {item_name}",
        "gold_gained": "Получено золота: {amount}",
        "exp_gained": "Получено опыта: {amount}",
        "achievement_unlocked": "Достижение разблокировано: {achievement_name}",
        "battle_victory": "Победа!",
        "battle_defeat": "Поражение!",
        "seduction_success": "Соблазнение успешно!",
        "seduction_failure": "Соблазнение не удалось!"
    }
    
    # Настройки игры
    GAME_SETTINGS = {
        "auto_save": True,
        "show_tooltips": True,
        "sound_enabled": True,
        "music_enabled": True,
        "difficulty": "normal"  # easy, normal, hard
    } 