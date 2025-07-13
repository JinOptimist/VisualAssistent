# Боевые сцены

# Основная боевая сцена
label battle_scene:
    python:
        battle_system.start_battle("goblin")
    scene bg BG
    "Вы попадаете на поле боя!"
    "Перед вами появляется [battle_system.enemy_name]!"
    jump battle_loop

# Бой с гоблином
label battle_scene_goblin:
    python:
        battle_system.start_battle("goblin")
    scene bg BG
    "Вы встречаете гоблина в темном лесу!"
    "Маленький, но опасный противник готов к бою!"
    jump battle_loop

# Бой с орком
label battle_scene_orc:
    python:
        battle_system.start_battle("orc")
    scene bg BG
    "Из-за деревьев выходит огромный орк!"
    "Его мощные руки сжимают тяжелое оружие!"
    jump battle_loop

# Бой с троллем
label battle_scene_troll:
    python:
        battle_system.start_battle("troll")
    scene bg BG
    "Земля дрожит под ногами - это тролль!"
    "Монстр размером с дом приближается к вам!"
    jump battle_loop

# Основной боевой цикл
label battle_loop:
    scene bg BG
    
    # Показываем статус боя
    "=== СТАТУС БОЯ ==="
    "Ваше здоровье: [battle_system.player_hp]/[battle_system.player_max_hp]"
    "Ваша мана: [battle_system.player_mp]/[battle_system.player_max_mp]"
    "Ваш щит: [battle_system.player_shield]"
    ""
    "[battle_system.enemy_name] здоровье: [battle_system.enemy_hp]/[battle_system.enemy_max_hp]"
    "[battle_system.enemy_name] мана: [battle_system.enemy_mp]/[battle_system.enemy_max_mp]"
    "[battle_system.enemy_name] щит: [battle_system.enemy_shield]"
    ""
    
    # Проверяем, не закончен ли бой
    if battle_system.is_battle_over():
        jump battle_end
    
    # Выбор действия игрока
    menu:
        "Выберите действие:"
        "Атаковать":
            python:
                result = battle_system.player_attack()
            "[result]"
            jump enemy_turn
        "Защищаться":
            python:
                result = battle_system.player_defend()
            "[result]"
            jump enemy_turn
        "Использовать предмет":
            jump use_item_in_battle
        "Попытаться сбежать":
            "Вы пытаетесь сбежать..."
            if renpy.random.randint(1, 100) <= 50:
                "Успешно! Вы сбежали от боя!"
                jump battle_escape
            else:
                "Неудача! Противник не дает вам сбежать!"
                jump enemy_turn

# Ход противника
label enemy_turn:
    python:
        result = battle_system.enemy_turn()
    "[result]"
    jump battle_loop

# Использование предмета в бою
label use_item_in_battle:
    python:
        items = inventory_system.get_inventory_list()
    
    menu:
        "Выберите предмет:"
        "Зелье здоровья" if "health_potion" in inventory_system.inventory:
            python:
                result = inventory_system.use_item("health_potion")
            "[result]"
            jump enemy_turn
        "Зелье маны" if "mana_potion" in inventory_system.inventory:
            python:
                result = inventory_system.use_item("mana_potion")
            "[result]"
            jump enemy_turn
        "Назад":
            jump battle_loop

# Конец боя
label battle_end:
    python:
        result = battle_system.get_battle_result()
    
    if result == "victory":
        "Победа! Вы победили [battle_system.enemy_name]!"
        python:
            # Награды за победу
            exp_gain = 20
            gold_gain = 50
            progression_system.gain_exp(exp_gain)
            inventory_system.add_gold(gold_gain)
            progression_system.gain_skill_exp("sword_mastery", 10)
            # Проверяем достижения
            if not progression_system.achievements["first_victory"]["unlocked"]:
                achievement = progression_system.unlock_achievement("first_victory")
                if achievement:
                    renpy.notify(achievement)
        "Получено опыта: [exp_gain]"
        "Получено золота: [gold_gain]"
        "Навык владения мечом улучшен!"
    elif result == "defeat":
        "Поражение! Вы проиграли бой..."
        "Но не отчаивайтесь, в следующий раз повезет больше!"
    jump after_battle

# После боя
label after_battle:
    menu:
        "Что делать дальше?"
        "Продолжить путешествие":
            jump world_map
        "Отдохнуть и восстановиться":
            python:
                battle_system.add_health("player", 5)
                battle_system.add_mana("player", 5)
            "Вы отдохнули и восстановили силы!"
            jump world_map
        "Проверить инвентарь":
            jump inventory_menu

# Побег из боя
label battle_escape:
    "Вы успешно сбежали от боя!"
    "Но ваша репутация немного пострадала..."
    python:
        progression_system.player_reputation = max(-10, progression_system.player_reputation - 1)
    jump world_map

# Меню инвентаря
label inventory_menu:
    "=== ИНВЕНТАРЬ ==="
    python:
        items = inventory_system.get_inventory_list()
        gold = inventory_system.gold
        if items:
            inv_text = ""
            for item in items:
                inv_text += f"{item['name']} x{item['quantity']} - {item['description']}\n"
        else:
            inv_text = "Инвентарь пуст"
    "Золото: {gold}"
    ""
    "{inv_text}"
    menu:
        "Выберите действие:"
        "Использовать предмет":
            jump use_item_menu
        "Экипировка":
            jump equipment_menu
        "Назад":
            jump after_battle

# Меню использования предметов
label use_item_menu:
    python:
        items = inventory_system.get_inventory_list()
        item_choices = [(f"{item['name']} x{item['quantity']}", item['id']) for item in items]
    if not item_choices:
        "Нет предметов для использования."
        jump inventory_menu
    $ choice = renpy.display_menu(item_choices + [("Назад", "back")])
    if choice == "back":
        jump inventory_menu
    python:
        result = inventory_system.use_item(choice)
    "{result}"
    jump inventory_menu

# Меню экипировки
label equipment_menu:
    "=== ЭКИПИРОВКА ==="
    python:
        equipment = inventory_system.get_equipment_list()
        weapon = equipment['weapon']['name'] if equipment['weapon'] else 'Не экипировано'
        armor = equipment['armor']['name'] if equipment['armor'] else 'Не экипирована'
        accessory = equipment['accessory']['name'] if equipment['accessory'] else 'Не экипирован'
    "Оружие: {weapon}"
    "Броня: {armor}"
    "Аксессуар: {accessory}"
    menu:
        "Выберите действие:"
        "Снять оружие" if equipment['weapon']:
            python:
                result = inventory_system.unequip_item("weapon")
            "{result}"
            jump equipment_menu
        "Снять броню" if equipment['armor']:
            python:
                result = inventory_system.unequip_item("armor")
            "{result}"
            jump equipment_menu
        "Снять аксессуар" if equipment['accessory']:
            python:
                result = inventory_system.unequip_item("accessory")
            "{result}"
            jump equipment_menu
        "Назад":
            jump inventory_menu 