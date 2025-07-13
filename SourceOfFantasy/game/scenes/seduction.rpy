# Сцены соблазнения

# Соблазнение дочери торговца
label seduction_merchant_daughter:
    python:
        seduction_system.start_seduction("merchant_daughter")
    scene bg room
    "Вы заходите в лавку торговца и видите его дочь."
    "Она застенчиво улыбается, когда вы подходите к прилавку."
    jump seduction_loop

# Соблазнение благородной леди
label seduction_noble_lady:
    python:
        seduction_system.start_seduction("noble_lady")
    scene bg room
    "В роскошном саду вы встречаете благородную леди."
    "Ее загадочный взгляд привлекает ваше внимание."
    jump seduction_loop

# Соблазнение таверной девки
label seduction_tavern_wench:
    python:
        seduction_system.start_seduction("tavern_wench")
    scene bg room
    "В шумной таверне вы замечаете дерзкую девушку."
    "Она смело смотрит на вас и подмигивает."
    jump seduction_loop

# Основной цикл соблазнения
label seduction_loop:
    scene bg room
    
    # Показываем статус соблазнения
    "=== СОБЛАЗНЕНИЕ ==="
    $ target_name = seduction_system.target_name
    $ target_affection = seduction_system.target_affection
    $ target_difficulty = seduction_system.target_difficulty
    $ seduction_progress = int(seduction_system.get_seduction_progress())
    $ player_charm = seduction_system.player_charm
    $ player_max_charm = seduction_system.player_max_charm
    $ player_confidence = seduction_system.player_confidence
    $ player_max_confidence = seduction_system.player_max_confidence
    "Цель: {target_name}"
    "Привязанность: {target_affection}/{target_difficulty}"
    "Прогресс: {seduction_progress}%"
    ""
    "Ваша харизма: {player_charm}/{player_max_charm}"
    "Ваша уверенность: {player_confidence}/{player_max_confidence}"
    ""
    
    python:
        if seduction_system.is_seduction_successful():
            renpy.jump("seduction_success")
    
    menu:
        "Выберите действие:"
        "Сделать комплимент":
            jump seduction_compliment
        "Подарить подарок":
            jump seduction_gift
        "Завести разговор":
            jump seduction_conversation
        "Попытаться соблазнить":
            jump seduction_attempt
        "Отступить":
            "Вы решаете отступить..."
            jump seduction_failure

# Делаем комплимент
label seduction_compliment:
    menu:
        "Какой комплимент сделать?"
        "Общий комплимент":
            python:
                result = seduction_system.compliment("general")
            "{result}"
            jump seduction_loop
        "Комплимент внешности":
            python:
                result = seduction_system.compliment("appearance")
            "{result}"
            jump seduction_loop
        "Комплимент уму":
            python:
                result = seduction_system.compliment("intelligence")
            "{result}"
            jump seduction_loop
        "Комплимент характеру":
            python:
                result = seduction_system.compliment("personality")
            "{result}"
            jump seduction_loop
        "Флиртующий комплимент":
            python:
                result = seduction_system.compliment("flirtatious")
            "{result}"
            jump seduction_loop
        "Назад":
            jump seduction_loop

# Дарим подарок
label seduction_gift:
    menu:
        "Какой подарок подарить?"
        "Цветы" if inventory_system.gold >= 10:
            python:
                inventory_system.spend_gold(10)
                result = seduction_system.gift("flower")
            "{result}"
            jump seduction_loop
        "Книгу" if inventory_system.gold >= 25:
            python:
                inventory_system.spend_gold(25)
                result = seduction_system.gift("book")
            "{result}"
            jump seduction_loop
        "Вино" if inventory_system.gold >= 30:
            python:
                inventory_system.spend_gold(30)
                result = seduction_system.gift("wine")
            "{result}"
            jump seduction_loop
        "Драгоценности" if inventory_system.gold >= 100:
            python:
                inventory_system.spend_gold(100)
                result = seduction_system.gift("jewelry")
            "{result}"
            jump seduction_loop
        "Дорогой подарок" if inventory_system.gold >= 200:
            python:
                inventory_system.spend_gold(200)
                result = seduction_system.gift("expensive")
            "{result}"
            jump seduction_loop
        "Назад":
            jump seduction_loop

# Заводим разговор
label seduction_conversation:
    menu:
        "О чем поговорить?"
        "Обычная беседа":
            python:
                result = seduction_system.conversation("casual")
            "{result}"
            jump seduction_loop
        "Личная беседа":
            python:
                result = seduction_system.conversation("personal")
            "{result}"
            jump seduction_loop
        "Романтическая беседа":
            python:
                result = seduction_system.conversation("romantic")
            "{result}"
            jump seduction_loop
        "Интеллектуальная беседа":
            python:
                result = seduction_system.conversation("intellectual")
            "{result}"
            jump seduction_loop
        "Назад":
            jump seduction_loop

# Попытка соблазнения
label seduction_attempt:
    "Вы решаете сделать решительный шаг..."
    python:
        base_chance = seduction_system.get_seduction_progress()
        charm_bonus = seduction_system.player_charm * 5
        confidence_bonus = seduction_system.player_confidence * 3
        total_chance = base_chance + charm_bonus + confidence_bonus
        if renpy.random.randint(1, 100) <= total_chance:
            seduction_system.target_affection = seduction_system.target_difficulty
            renpy.jump("seduction_success")
        else:
            seduction_system.player_confidence = max(0, seduction_system.player_confidence - 2)
            renpy.jump("seduction_failure")

# Успешное соблазнение
label seduction_success:
    scene bg room
    $ target_name = seduction_system.target_name
    "Успех! {target_name} покорена вашим обаянием!"
    python:
        exp_gain = 30
        gold_gain = 100
        progression_system.gain_exp(exp_gain)
        inventory_system.add_gold(gold_gain)
        progression_system.gain_skill_exp("seduction_art", 20)
        progression_system.player_reputation = min(10, progression_system.player_reputation + 2)
        if progression_system.get_skill_level("seduction_art") >= 10:
            achievement = progression_system.unlock_achievement("seduction_master")
            if achievement:
                renpy.notify(achievement)
    "Получено опыта: {exp_gain}"
    "Получено золота: {gold_gain}"
    "Навык соблазнения улучшен!"
    "Ваша репутация повысилась!"
    jump after_seduction

# Неудачное соблазнение
label seduction_failure:
    scene bg room
    $ target_name = seduction_system.target_name
    "{target_name} не поддается на ваши ухаживания."
    "Возможно, стоит попробовать другой подход..."
    python:
        progression_system.player_reputation = max(-10, progression_system.player_reputation - 1)
    jump after_seduction

# После соблазнения
label after_seduction:
    menu:
        "Что делать дальше?"
        "Продолжить путешествие":
            jump world_map
        "Попробовать соблазнить другую":
            jump seduction_choice
        "Проверить характеристики":
            jump character_stats

# Выбор цели для соблазнения
label seduction_choice:
    menu:
        "Кого попытаться соблазнить?"
        "Дочь торговца":
            jump seduction_merchant_daughter
        "Благородная леди":
            jump seduction_noble_lady
        "Таверная девка":
            jump seduction_tavern_wench
        "Назад":
            jump world_map

# Просмотр характеристик персонажа
label character_stats:
    "=== ХАРАКТЕРИСТИКИ ПЕРСОНАЖА ==="
    python:
        stats = progression_system.get_player_stats()
        rep = progression_system.player_reputation
    "Уровень: {stats['level']}"
    "Опыт: {stats['exp']}/{stats['exp_to_next']}"
    "Очки характеристик: {stats['stat_points']}"
    ""
    "Сила: {stats['strength']}"
    "Ловкость: {stats['agility']}"
    "Интеллект: {stats['intelligence']}"
    "Харизма: {stats['charisma']}"
    "Живучесть: {stats['vitality']}"
    ""
    "Репутация: {rep}"
    if stats['stat_points'] > 0:
        menu:
            "Распределить очки характеристик:"
            "Увеличить силу":
                python:
                    result = progression_system.increase_stat("strength")
                "{result}"
                jump character_stats
            "Увеличить ловкость":
                python:
                    result = progression_system.increase_stat("agility")
                "{result}"
                jump character_stats
            "Увеличить интеллект":
                python:
                    result = progression_system.increase_stat("intelligence")
                "{result}"
                jump character_stats
            "Увеличить харизму":
                python:
                    result = progression_system.increase_stat("charisma")
                "{result}"
                jump character_stats
            "Увеличить живучесть":
                python:
                    result = progression_system.increase_stat("vitality")
                "{result}"
                jump character_stats
            "Назад":
                jump after_seduction
    else:
        menu:
            "Назад":
                jump after_seduction 