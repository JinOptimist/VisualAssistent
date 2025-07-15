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
    
    # Применяем эффекты статусов в начале хода
    python:
        # Применяем эффекты переполнения
        battle_system.apply_overflow_effects("player")
        battle_system.check_overflow_status("player")
        
        # Применяем эффект "Атака Потоком" если активен
        if battle_system.player_stream_attack_is_active:
            result = battle_system.apply_stream_attack_effect("player")
            if result:
                renpy.notify(result)
            battle_system.check_stream_attack_status("player")
    
    show screen battle_screen
    $ renpy.pause(0.1, hard=True)
    if battle_system.is_battle_over():
        hide screen battle_screen
        jump battle_end
    $ renpy.pause(9999, hard=True) # Ожидание действия игрока через экран

# Действия игрока (вызываются кнопками на экране)
label player_action_projectile_attack:
    $ result = battle_system.player_projectile_attack()
    $ renpy.notify(result)
    if battle_system.is_battle_over():
        hide screen battle_screen
        jump battle_end
    jump enemy_turn

label player_action_stream_attack:
    $ result = battle_system.player_stream_attack()
    $ renpy.notify(result)
    if battle_system.is_battle_over():
        hide screen battle_screen
        jump battle_end
    jump enemy_turn

label player_action_defend:
    $ result = battle_system.player_defend()
    $ renpy.notify(result)
    if battle_system.is_battle_over():
        hide screen battle_screen
        jump battle_end
    jump enemy_turn

label player_action_shield:
    $ result = battle_system.player_shield_spell()
    $ renpy.notify(result)
    if battle_system.is_battle_over():
        hide screen battle_screen
        jump battle_end
    jump enemy_turn

label player_action_heal:
    $ result = battle_system.player_heal()
    $ renpy.notify(result)
    if battle_system.is_battle_over():
        hide screen battle_screen
        jump battle_end
    jump enemy_turn

label player_action_continue_stream:
    # Просто переходим к ходу противника, так как эффект "Атака Потоком" уже применен в начале хода
    $ renpy.notify("Продолжаете атаку потоком...")
    jump enemy_turn

label player_action_escape:
    $ import renpy
    $ escape_success = renpy.random.randint(1, 100) <= 50
    if escape_success:
        $ renpy.notify("Успешно! Вы сбежали от боя!")
        hide screen battle_screen
        jump battle_escape
    else:
        $ renpy.notify("Неудача! Противник не дает вам сбежать!")
        jump enemy_turn

label player_action_use_item:
    # Здесь можно реализовать выбор предмета через отдельный экран или простое меню
    $ result = "Пока не реализовано: выбор и использование предмета в бою"
    $ renpy.notify(result)
    jump enemy_turn

# Ход противника
label enemy_turn:
    # Применяем эффекты статусов противника
    python:
        # Применяем эффекты переполнения
        battle_system.apply_overflow_effects("enemy")
        battle_system.check_overflow_status("enemy")
        
        # Применяем эффект "Атака Потоком" если активен
        if battle_system.enemy_stream_attack_is_active:
            result = battle_system.apply_stream_attack_effect("enemy")
            if result:
                renpy.notify(result)
            battle_system.check_stream_attack_status("enemy")
        else:
            # Обычный ход противника
            result = battle_system.enemy_turn()
            renpy.notify(result)
    
    if battle_system.is_battle_over():
        hide screen battle_screen
        jump battle_end
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
    hide screen battle_screen
    $ result = battle_system.get_battle_result()
    
    if result == "victory":
        "Победа! Вы победили [battle_system.enemy_name]!"
        $ gold_gain = 50
        $ inventory_system.add_gold(gold_gain)
        "Получено золота: [gold_gain]"
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
    "Но ваша честь немного пострадала..."
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