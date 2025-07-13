# Объявление фонов
image bg room = "images/BGs/BG.jpg"
image bg BG = "images/BGs/BG.jpg"

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define narrator = Character(None, kind=nvl)

# The game starts here.

label start:
    # Запрашиваем имя игрока
    python:
        player_name = renpy.input("Как вас зовут?", length=32)
        player_name = player_name.strip()
        
        # Если имя пустое, используем значение по умолчанию
        if player_name == "":
            player_name = "Игрок"

    scene bg room
    show eileen happy

    e "Рада видеть, [player_name]!"
    e "Добро пожаловать в мир приключений!"

    jump world_map

    return

# Главная карта мира
label world_map:
    scene bg room
    
    "=== КАРТА МИРА ==="
    python:
        location_info = get_location_info(current_location)
        available_actions = get_available_actions(current_location)
        connected_locations = get_connected_locations(current_location)
    
    "Текущая локация: [location_info['name']]"
    "[location_info['description']]"
    ""
    
    menu:
        "Выберите действие:"
        
        "Исследовать локацию":
            jump explore_location
        
        "Переместиться":
            jump travel_menu
        
        "Бой":
            jump battle_choice
        
        "Соблазнение":
            jump seduction_choice
        
        "Тренировка":
            jump training_ground
        
        "Инвентарь":
            jump inventory_menu
        
        "Характеристики":
            jump character_stats
        
        "Настройки":
            jump game_settings

# Исследование локации
label explore_location:
    scene bg room
    python:
        location_info = get_location_info(current_location)
        available_actions = get_available_actions(current_location)
    
    "Вы исследуете [location_info['name']]..."
    
    if "battle" in available_actions:
        "В этой локации можно найти противников для боя."
    if "seduction" in available_actions:
        "Здесь есть люди, которых можно попытаться соблазнить."
    if "trade" in available_actions:
        "В этой локации можно торговать."
    if "training" in available_actions:
        "Здесь можно тренироваться."
    if "quest" in available_actions:
        "Здесь могут быть доступны квесты."
    
    menu:
        "Что делать дальше?"
        
        "Попытаться найти противника" if "battle" in available_actions:
            jump random_battle
        
        "Попытаться соблазнить кого-то" if "seduction" in available_actions:
            jump seduction_choice
        
        "Торговать" if "trade" in available_actions:
            jump trade_menu
        
        "Тренироваться" if "training" in available_actions:
            jump training_ground
        
        "Назад":
            jump world_map

# Случайный бой
label random_battle:
    scene bg room
    "Вы ищете противника..."
    python:
        enemies = ["goblin", "orc", "troll"]
        enemy = renpy.random.choice(enemies)
        battle_system.start_battle(enemy)
    
    "Вы встречаете [battle_system.enemy_name]!"
    jump battle_loop

# Выбор боя
label battle_choice:
    menu:
        "Выберите противника:"
        
        "Гоблин":
            jump battle_scene_goblin
        
        "Орк":
            jump battle_scene_orc
        
        "Тролль":
            jump battle_scene_troll
        
        "Случайный противник":
            jump random_battle
        
        "Назад":
            jump world_map

# Меню путешествий
label travel_menu:
    scene bg room
    "=== ПУТЕШЕСТВИЕ ==="
    python:
        connected_locations = get_connected_locations(current_location)
        locations_text = ""
        for location_id in connected_locations:
            location_info = get_location_info(location_id)
            locations_text += f"{location_info['name']} - {location_info['description']}\n"
    "Доступные локации:"
    "{locations_text}"
    python:
        menu_choices = [(get_location_info(loc)['name'], loc) for loc in connected_locations]
        menu_choices.append(("Назад", "back"))
        choice = renpy.display_menu(menu_choices)
    if choice == "back":
        jump world_map
    python:
        change_location(choice)
        loc_name = get_location_info(choice)['name']
    "Вы перемещаетесь в {loc_name}."
    jump world_map

# Меню торговли
label trade_menu:
    scene bg room
    "=== ТОРГОВЛЯ ==="
    python:
        gold = inventory_system.gold
        items = inventory_system.get_inventory_list()
        items_text = ""
        if items:
            for item in items:
                items_text += f"{item['name']} x{item['quantity']} - {item['description']}\n"
        else:
            items_text = "У вас нет предметов для продажи."
    "Ваше золото: {gold}"
    ""
    "Ваши предметы:"
    "{items_text}"
    menu:
        "Выберите действие:"
        "Купить предметы":
            jump buy_items
        "Продать предметы":
            jump sell_items
        "Назад":
            jump world_map

# Покупка предметов
label buy_items:
    scene bg room
    "=== ПОКУПКА ==="
    python:
        gold = inventory_system.gold
    "Ваше золото: {gold}"
    ""
    menu:
        "Что купить?"
        "Зелье здоровья (30 золота)" if gold >= 30:
            python:
                result = inventory_system.add_item("health_potion")
                inventory_system.spend_gold(30)
            "{result}"
            jump trade_menu
        "Зелье маны (25 золота)" if gold >= 25:
            python:
                result = inventory_system.add_item("mana_potion")
                inventory_system.spend_gold(25)
            "{result}"
            jump trade_menu
        "Ржавый меч (50 золота)" if gold >= 50:
            python:
                result = inventory_system.add_item("rusty_sword")
                inventory_system.spend_gold(50)
            "{result}"
            jump trade_menu
        "Кожаная броня (80 золота)" if gold >= 80:
            python:
                result = inventory_system.add_item("leather_armor")
                inventory_system.spend_gold(80)
            "{result}"
            jump trade_menu
        "Назад":
            jump trade_menu

# Продажа предметов
label sell_items:
    scene bg room
    "=== ПРОДАЖА ==="
    python:
        items = inventory_system.get_inventory_list()
    if not items:
        "У вас нет предметов для продажи."
        jump trade_menu
    python:
        menu_choices = []
        for item in items:
            item_data = inventory_system.all_items[item['id']]
            menu_choices.append((f"{item['name']} x{item['quantity']} (Цена: {item_data['value']} золота)", item['id']))
        menu_choices.append(("Назад", "back"))
        choice = renpy.display_menu(menu_choices)
    if choice == "back":
        jump trade_menu
    python:
        item_data = inventory_system.all_items[choice]
        sell_price = item_data['value'] // 2
        result = inventory_system.remove_item(choice, 1)
        inventory_system.add_gold(sell_price)
    "Продано за {sell_price} золота!"
    jump trade_menu

# Настройки игры
label game_settings:
    scene bg room
    "=== НАСТРОЙКИ ИГРЫ ==="
    python:
        settings = GAME_SETTINGS
    
    "Автосохранение: {'Включено' if settings['auto_save'] else 'Выключено'}"
    "Подсказки: {'Включены' if settings['show_tooltips'] else 'Выключены'}"
    "Звук: {'Включен' if settings['sound_enabled'] else 'Выключен'}"
    "Музыка: {'Включена' if settings['music_enabled'] else 'Выключена'}"
    "Сложность: [settings['difficulty']]"
    ""
    
    menu:
        "Выберите настройку:"
        
        "Сбросить прогресс":
            python:
                reset_game_state()
            "Прогресс сброшен!"
            jump world_map
        
        "Информация об игре":
            "Версия игры: [GAME_VERSION]"
            "Название: [GAME_TITLE]"
            "Автор: AI Assistant"
            jump game_settings
        
        "Назад":
            jump world_map
