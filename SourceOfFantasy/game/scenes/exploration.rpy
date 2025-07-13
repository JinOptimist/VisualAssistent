# Сцены исследования мира

# Исследование леса
label explore_forest:
    scene bg room
    "Вы входите в темный лес. Деревья высоко поднимаются над головой, создавая таинственную атмосферу."
    "Вдалеке слышны звуки диких животных."
    menu:
        "Что делать?"
        "Исследовать глубже":
            jump deep_forest_exploration
        "Искать следы":
            jump search_tracks
        "Собрать ресурсы":
            jump gather_resources
        "Вернуться":
            jump world_map

# Глубокое исследование леса
label deep_forest_exploration:
    scene bg room
    "Вы углубляетесь в лес. Воздух становится более влажным, а тропинки менее заметными."
    python:
        r = renpy.random.randint(1, 100)
        if r <= 30:
            renpy.jump("forest_discovery")
        elif r <= 70:
            renpy.jump("forest_battle")
        else:
            renpy.jump("forest_nothing")

# Находка в лесу
label forest_discovery:
    scene bg room
    "Среди деревьев вы замечаете что-то блестящее!"
    python:
        discoveries = [
            {"item": "health_potion", "message": "Вы нашли зелье здоровья!"},
            {"item": "mana_potion", "message": "Вы нашли зелье маны!"},
            {"item": "rusty_sword", "message": "Вы нашли ржавый меч!"},
            {"gold": 25, "message": "Вы нашли небольшой мешочек с золотом!"}
        ]
        discovery = renpy.random.choice(discoveries)
        renpy.say(None, discovery["message"])
        if "item" in discovery:
            result = inventory_system.add_item(discovery["item"])
            renpy.say(None, result)
        elif "gold" in discovery:
            result = inventory_system.add_gold(discovery["gold"])
            renpy.say(None, result)
    jump explore_forest

# Бой в лесу
label forest_battle:
    scene bg room
    "Из-за деревьев выскакивает дикое животное!"
    python:
        animals = ["goblin", "orc"]
        animal = renpy.random.choice(animals)
        battle_system.start_battle(animal)
    "Вы встречаете [battle_system.enemy_name]!"
    jump battle_loop

# Ничего не найдено
label forest_nothing:
    "Вы исследуете местность, но ничего интересного не находите."
    jump explore_forest

# Поиск следов
label search_tracks:
    scene bg room
    "Вы внимательно осматриваете землю в поисках следов."
    python:
        if renpy.random.randint(1, 100) <= 50:
            renpy.jump("tracks_found")
        else:
            renpy.jump("no_tracks")

# Следы найдены
label tracks_found:
    scene bg room
    "Вы находите свежие следы! Они ведут в определенном направлении."
    menu:
        "Следовать по следам":
            jump follow_tracks
        "Игнорировать":
            jump explore_forest

# Следование по следам
label follow_tracks:
    scene bg room
    "Вы следуете по следам, которые приводят вас к небольшой поляне."
    "В центре поляны вы видите что-то интересное!"
    python:
        if renpy.random.randint(1, 100) <= 60:
            renpy.jump("treasure_found")
        else:
            renpy.jump("ambush")

# Найден клад
label treasure_found:
    scene bg room
    "Вы нашли спрятанный клад!"
    python:
        treasures = [
            {"item": "iron_sword", "message": "В кладе был железный меч!"},
            {"item": "leather_armor", "message": "В кладе была кожаная броня!"},
            {"item": "charm_ring", "message": "В кладе было кольцо очарования!"},
            {"gold": 100, "message": "В кладе было много золота!"}
        ]
        treasure = renpy.random.choice(treasures)
        renpy.say(None, treasure["message"])
        if "item" in treasure:
            result = inventory_system.add_item(treasure["item"])
            renpy.say(None, result)
        elif "gold" in treasure:
            result = inventory_system.add_gold(treasure["gold"])
            renpy.say(None, result)
    jump explore_forest

# Засада
label ambush:
    scene bg room
    "Это была ловушка! Из засады выскакивают бандиты!"
    python:
        battle_system.start_battle("goblin")
    "Вы встречаете [battle_system.enemy_name]!"
    jump battle_loop

# Сбор ресурсов
label gather_resources:
    scene bg room
    "Вы собираете полезные растения и материалы."
    python:
        resources = [
            {"item": "health_potion", "chance": 40},
            {"item": "mana_potion", "chance": 30},
            {"gold": 10, "chance": 50}
        ]
        found_items = []
        for resource in resources:
            if renpy.random.randint(1, 100) <= resource["chance"]:
                found_items.append(resource)
        if found_items:
            renpy.say(None, "Вы собрали:")
            for item in found_items:
                if "item" in item:
                    result = inventory_system.add_item(item["item"])
                    renpy.say(None, result)
                elif "gold" in item:
                    result = inventory_system.add_gold(item["gold"])
                    renpy.say(None, result)
        else:
            renpy.say(None, "К сожалению, вы не нашли ничего полезного.")
    jump explore_forest

# Исследование пещеры
label explore_cave:
    scene bg room
    "Вы входите в темную пещеру. Воздух здесь влажный и прохладный."
    "Вдалеке слышны капающие звуки воды."
    menu:
        "Что делать?"
        "Исследовать глубже":
            jump deep_cave_exploration
        "Искать минералы":
            jump search_minerals
        "Искать сокровища":
            jump search_treasure
        "Вернуться":
            jump world_map

# Глубокое исследование пещеры
label deep_cave_exploration:
    scene bg room
    "Вы углубляетесь в пещеру. Становится темнее и опаснее."
    python:
        r = renpy.random.randint(1, 100)
        if r <= 60:
            renpy.jump("cave_battle")
        elif r <= 90:
            renpy.jump("cave_discovery")
        else:
            renpy.jump("cave_nothing")

# Бой в пещере
label cave_battle:
    scene bg room
    "Из темноты появляется опасное существо!"
    python:
        cave_enemies = ["troll", "orc"]
        enemy = renpy.random.choice(cave_enemies)
        battle_system.start_battle(enemy)
    "Вы встречаете [battle_system.enemy_name]!"
    jump battle_loop

# Находка в пещере
label cave_discovery:
    scene bg room
    "В глубине пещеры вы находите что-то интересное!"
    python:
        cave_discoveries = [
            {"item": "magic_staff", "message": "Вы нашли магический посох!"},
            {"item": "iron_armor", "message": "Вы нашли железную броню!"},
            {"item": "love_potion", "message": "Вы нашли зелье любви!"},
            {"gold": 150, "message": "Вы нашли сокровища!"}
        ]
        discovery = renpy.random.choice(cave_discoveries)
        renpy.say(None, discovery["message"])
        if "item" in discovery:
            result = inventory_system.add_item(discovery["item"])
            renpy.say(None, result)
        elif "gold" in discovery:
            result = inventory_system.add_gold(discovery["gold"])
            renpy.say(None, result)
    jump explore_cave

# Пустая часть пещеры
label cave_nothing:
    "Эта часть пещеры пуста."
    jump explore_cave

# Поиск минералов
label search_minerals:
    scene bg room
    "Вы ищете минералы в стенах пещеры."
    python:
        if renpy.random.randint(1, 100) <= 40:
            renpy.jump("minerals_found")
        else:
            renpy.jump("no_minerals")

label minerals_found:
    scene bg room
    "Вы нашли ценные минералы!"
    python:
        result = inventory_system.add_item("rare_mineral")
        renpy.say(None, result)
    jump explore_cave

label no_minerals:
    "Вы не нашли ничего ценного."
    jump explore_cave

# Поиск сокровищ
label search_treasure:
    scene bg room
    "Вы ищете сокровища в пещере."
    python:
        if renpy.random.randint(1, 100) <= 30:
            renpy.jump("treasure_found")
        else:
            renpy.jump("no_treasure")

label no_treasure:
    "Вы не нашли сокровищ."
    jump explore_cave 