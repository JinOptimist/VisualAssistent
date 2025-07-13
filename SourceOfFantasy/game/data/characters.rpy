# Определения персонажей

# Основные персонажи
define e = Character("Eileen", color="#c8a2c8")
define narrator = Character(None, kind=nvl)

# Боевые персонажи
define goblin = Character("Гоблин", color="#90EE90")
define orc = Character("Орк", color="#8B4513")
define troll = Character("Тролль", color="#228B22")

# Персонажи для соблазнения
define merchant_daughter = Character("Дочь торговца", color="#FFB6C1")
define noble_lady = Character("Благородная леди", color="#DDA0DD")
define tavern_wench = Character("Таверная девка", color="#F0E68C")

# NPC
define merchant = Character("Торговец", color="#DEB887")
define trainer = Character("Тренер", color="#4682B4")
define wizard = Character("Маг", color="#9370DB")
define guard = Character("Стражник", color="#696969")

# Специальные персонажи
define system = Character("Система", color="#FF6347", what_italic=True)
define achievement = Character("Достижение", color="#FFD700", what_bold=True) 