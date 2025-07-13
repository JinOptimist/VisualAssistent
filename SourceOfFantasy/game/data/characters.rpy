# Определения персонажей

# Основные персонажи
define e = Character("Eileen", color="#c8a2c8")
define narrator = Character(None, kind=nvl)

# Боевые персонажи
define goblin = Character("Гоблин", color="#90EE90")
define orc = Character("Орк", color="#8B4513")
define troll = Character("Тролль", color="#228B22")



# NPC
define merchant = Character("Торговец", color="#DEB887")

define wizard = Character("Маг", color="#9370DB")
define guard = Character("Стражник", color="#696969")

# Специальные персонажи
define system = Character("Система", color="#FF6347", what_italic=True)
define achievement = Character("Достижение", color="#FFD700", what_bold=True)

# ===== ПЕРСОНАЖИ ИЗ "SOURCE OF FANTASY" =====
define intro_qa = Character("", color="#FF1493", what_prefix='QA Джун: ')



# Главный герой
define pasha = Character("Паша", color="#4169E1")
define pasha_chat = Character("", color="#4169E1", what_prefix='Я: ')
define pasha_mind = Character("Мои мысли", color="#3250ac")

# Королевская семья
define linara = Character("Линара", color="#FF1493", what_prefix='"', what_suffix='"')
define queen = Character("Королева", color="#8B008B", what_prefix='"', what_suffix='"')

# Рыцари и защитники
define roni = Character("Рони", color="#2F4F4F", what_prefix='"', what_suffix='"')
define roni_teacher = Character("Учитель Рони", color="#556B2F", what_prefix='"', what_suffix='"')

# Друзья и союзники
define edi = Character("Эди", color="#32CD32", what_prefix='"', what_suffix='"')
define emma = Character("Эмма", color="#20B2AA", what_prefix='"', what_suffix='"')
define lumina = Character("Люми", color="#FF69B4", what_prefix='"', what_suffix='"')

# Маги и преподаватели
define professor = Character("Профессор", color="#9370DB", what_prefix='"', what_suffix='"')
define ilanir = Character("Иланир", color="#DAA520", what_prefix='"', what_suffix='"')
define red_mage = Character("Красный Маг", color="#DC143C", what_prefix='"', what_suffix='"')

# Разведка и тени
define seventh = Character("Седьмой", color="#000000", what_prefix='"', what_suffix='"')
define shadow = Character("Тень", color="#696969", what_prefix='"', what_suffix='"')

# Министры и политики
define finance_minister = Character("Министр Финансов", color="#FF8C00", what_prefix='"', what_suffix='"')
define magic_minister = Character("Министр Магии", color="#9932CC", what_prefix='"', what_suffix='"')
define tax_minister = Character("Министр Налогов", color="#8B4513", what_prefix='"', what_suffix='"')

# Враги и противники
define enemy_mage = Character("Вражеский маг", color="#8B0000", what_prefix='"', what_suffix='"')
define dark_coven = Character("Сумрачный Ковен", color="#2F2F2F", what_prefix='"', what_suffix='"')
define rebel_lord = Character("Мятежный лорд", color="#CD853F", what_prefix='"', what_suffix='"')

# Системные уведомления
define system_notification = Character("Системное уведомление", color="#FF6347", what_italic=True, what_bold=True)
define status_window = Character("Окно статуса", color="#FFD700", what_bold=True)
define achievement_notification = Character("Достижение", color="#FFD700", what_bold=True, what_italic=True)

# Боги и высшие силы
define gods = Character("Боги", color="#FFD700", what_italic=True, what_bold=True) 