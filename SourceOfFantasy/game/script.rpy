# Объявление фонов
image bg room = "images/BGs/BG.jpg"
image bg BG = "images/BGs/BG.jpg"

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.s

define e = Character("Eileen")
# когда такой персонаж говорит, то поле диалога пустое увеличивается в выостку до 100%
# define narrator = Character(None, kind=nvl) 
define narrator = Character(None)

# The game starts here.

label start:
    narrator "Добро пожаловать в игру Source of Fantasy"
    jump main_story
    
    return

