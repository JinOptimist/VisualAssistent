# Сцены прокачки персонажа

# Тренировочная площадка
label training_ground:
    scene bg room
    "Вы приходите на тренировочную площадку."
    "Здесь можно улучшить свои боевые навыки и физические характеристики."
    jump training_menu

# Меню тренировок
label training_menu:
    scene bg room
    "=== ТРЕНИРОВОЧНАЯ ПЛОЩАДКА ==="
    python:
        stats = progression_system.get_player_stats()
    "Уровень: [stats['level']]"
    "Опыт: [stats['exp']]/[stats['exp_to_next']]"
    "Очки характеристик: [stats['stat_points']]"
    ""
    "Сила: [stats['strength']]"
    "Ловкость: [stats['agility']]"
    "Интеллект: [stats['intelligence']]"
    "Харизма: [stats['charisma']]"
    "Живучесть: [stats['vitality']]"
    ""
    menu:
        "Выберите тренировку:"
        "Тренировка силы":
            jump strength_training
        "Тренировка ловкости":
            jump agility_training
        "Изучение магии":
            jump magic_training
        "Тренировка харизмы":
            jump charisma_training
        "Тренировка выносливости":
            jump vitality_training
        "Распределить очки характеристик":
            jump stat_allocation
        "Просмотр навыков":
            jump skills_view
        "Назад":
            jump world_map

# Тренировка силы
label strength_training:
    scene bg room
    "Вы подходите к тяжелым гирям и начинаете тренировку силы."
    python:
        cost = 20
        if inventory_system.gold >= cost:
            inventory_system.spend_gold(cost)
            exp_gain = 15
            skill_gain = 10
            progression_system.gain_exp(exp_gain)
            progression_system.gain_skill_exp("sword_mastery", skill_gain)
            result = f"Тренировка завершена! Получено опыта: {exp_gain}, навык меча улучшен!"
        else:
            result = "Недостаточно золота для тренировки!"
        renpy.say(None, result)
    jump training_menu

# Тренировка ловкости
label agility_training:
    scene bg room
    "Вы тренируетесь на полосе препятствий, улучшая свою ловкость."
    python:
        cost = 15
        if inventory_system.gold >= cost:
            inventory_system.spend_gold(cost)
            exp_gain = 12
            skill_gain = 8
            progression_system.gain_exp(exp_gain)
            progression_system.gain_skill_exp("stealth", skill_gain)
            result = f"Тренировка завершена! Получено опыта: {exp_gain}, навык скрытности улучшен!"
        else:
            result = "Недостаточно золота для тренировки!"
        renpy.say(None, result)
    jump training_menu

# Изучение магии
label magic_training:
    scene bg room
    "Вы садитесь в медитативную позу и изучаете магические руны."
    python:
        cost = 25
        if inventory_system.gold >= cost:
            inventory_system.spend_gold(cost)
            exp_gain = 18
            skill_gain = 12
            progression_system.gain_exp(exp_gain)
            progression_system.gain_skill_exp("magic_mastery", skill_gain)
            result = f"Изучение завершено! Получено опыта: {exp_gain}, навык магии улучшен!"
        else:
            result = "Недостаточно золота для обучения!"
        renpy.say(None, result)
    jump training_menu

# Тренировка харизмы
label charisma_training:
    scene bg room
    "Вы практикуетесь в ораторском искусстве перед зеркалом."
    python:
        cost = 30
        if inventory_system.gold >= cost:
            inventory_system.spend_gold(cost)
            exp_gain = 20
            skill_gain = 15
            progression_system.gain_exp(exp_gain)
            progression_system.gain_skill_exp("seduction_art", skill_gain)
            result = f"Тренировка завершена! Получено опыта: {exp_gain}, навык соблазнения улучшен!"
        else:
            result = "Недостаточно золота для тренировки!"
        renpy.say(None, result)
    jump training_menu

# Тренировка выносливости
label vitality_training:
    scene bg room
    "Вы выполняете изнурительные упражнения для улучшения выносливости."
    python:
        cost = 18
        if inventory_system.gold >= cost:
            inventory_system.spend_gold(cost)
            exp_gain = 14
            battle_system.player_max_hp += 1
            battle_system.player_hp = battle_system.player_max_hp
            result = f"Тренировка завершена! Получено опыта: {exp_gain}, максимальное здоровье увеличено!"
        else:
            result = "Недостаточно золота для тренировки!"
        renpy.say(None, result)
    jump training_menu

# Распределение очков характеристик
label stat_allocation:
    scene bg room
    "=== РАСПРЕДЕЛЕНИЕ ОЧКОВ ХАРАКТЕРИСТИК ==="
    python:
        stats = progression_system.get_player_stats()
    "Доступно очков: [stats['stat_points']]"
    ""
    "Сила: [stats['strength']] (влияет на физический урон)"
    "Ловкость: [stats['agility']] (влияет на уклонение и критический удар)"
    "Интеллект: [stats['intelligence']] (влияет на магический урон и ману)"
    "Харизма: [stats['charisma']] (влияет на соблазнение и торговлю)"
    "Живучесть: [stats['vitality']] (влияет на здоровье)"
    if stats['stat_points'] > 0:
        menu:
            "Выберите характеристику для увеличения:"
            "Увеличить силу":
                python:
                    result = progression_system.increase_stat("strength")
                    renpy.say(None, result)
                jump stat_allocation
            "Увеличить ловкость":
                python:
                    result = progression_system.increase_stat("agility")
                    renpy.say(None, result)
                jump stat_allocation
            "Увеличить интеллект":
                python:
                    result = progression_system.increase_stat("intelligence")
                    renpy.say(None, result)
                jump stat_allocation
            "Увеличить харизму":
                python:
                    result = progression_system.increase_stat("charisma")
                    renpy.say(None, result)
                jump stat_allocation
            "Увеличить живучесть":
                python:
                    result = progression_system.increase_stat("vitality")
                    renpy.say(None, result)
                jump stat_allocation
            "Назад":
                jump training_menu
    else:
        menu:
            "У вас нет очков характеристик для распределения."
            "Назад":
                jump training_menu

# Просмотр навыков
label skills_view:
    scene bg room
    "=== НАВЫКИ ПЕРСОНАЖА ==="
    python:
        skills = progression_system.skills
    "Владение мечом: [skills['sword_mastery']['level']]/[skills['sword_mastery']['max_level']]"
    "Мастерство магии: [skills['magic_mastery']['level']]/[skills['magic_mastery']['max_level']]"
    "Искусство соблазнения: [skills['seduction_art']['level']]/[skills['seduction_art']['max_level']]"
    "Торговля: [skills['trading']['level']]/[skills['trading']['max_level']]"
    "Скрытность: [skills['stealth']['level']]/[skills['stealth']['max_level']]"
    ""
    menu:
        "Назад":
            jump training_menu

# Мастер навыков
label skill_master:
    scene bg room
    "Вы находите мастера, который может обучить вас новым навыкам."
    "Но обучение стоит дорого..."
    python:
        master_cost = 500
        if inventory_system.gold >= master_cost:
            inventory_system.spend_gold(master_cost)
            progression_system.stat_points += 5
            for skill_name in progression_system.skills:
                progression_system.gain_skill_exp(skill_name, 50)
            result = f"Мастер обучил вас! Получено 5 очков характеристик и улучшены все навыки!"
        else:
            result = "Недостаточно золота для обучения у мастера!"
        renpy.say(None, result)
    jump training_menu

# Достижения
label achievements_view:
    scene bg room
    "=== ДОСТИЖЕНИЯ ==="
    python:
        achievements = progression_system.achievements
    if achievements:
        python:
            for achievement_id, achievement in achievements.items():
                renpy.say(None, f"{achievement['name']}: {achievement['description']} ({'Получено' if achievement['unlocked'] else 'Не получено'})")
    else:
        "У вас пока нет достижений."
    menu:
        "Назад":
            jump training_menu 