# Боевая система
init python:
    class BattleSystem:
        def __init__(self):
            # Переменные игрока
            self.player_hp = 10
            self.player_max_hp = 10
            self.player_mp = 10
            self.player_max_mp = 10
            self.player_shield = 0
            self.player_defending = False
            self.player_blood_overflow = False
            self.player_mana_overflow = False
            
            # Переменные противника
            self.enemy_name = "Гоблин"
            self.enemy_hp = 5
            self.enemy_max_hp = 5
            self.enemy_mp = 3
            self.enemy_max_mp = 3
            self.enemy_shield = 0
            self.enemy_blood_overflow = False
            self.enemy_mana_overflow = False
            
            # Словарь с данными противников
            self.enemies = {
                "goblin": {
                    "name": "Гоблин",
                    "hp": 5,
                    "max_hp": 5,
                    "mp": 3,
                    "max_mp": 3,
                    "attack": 1,
                    "defense": 0
                },
                "orc": {
                    "name": "Орк",
                    "hp": 8,
                    "max_hp": 8,
                    "mp": 2,
                    "max_mp": 2,
                    "attack": 2,
                    "defense": 1
                },
                "troll": {
                    "name": "Тролль",
                    "hp": 12,
                    "max_hp": 12,
                    "mp": 1,
                    "max_mp": 1,
                    "attack": 3,
                    "defense": 2
                }
            }
        
        def start_battle(self, enemy_type="goblin"):
            """Начинает бой с указанным противником"""
            if enemy_type in self.enemies:
                enemy_data = self.enemies[enemy_type]
                self.enemy_name = enemy_data["name"]
                self.enemy_hp = enemy_data["hp"]
                self.enemy_max_hp = enemy_data["max_hp"]
                self.enemy_mp = enemy_data["mp"]
                self.enemy_max_mp = enemy_data["max_mp"]
            else:
                # Значения по умолчанию
                self.enemy_name = "Противник"
                self.enemy_hp = 5
                self.enemy_max_hp = 5
                self.enemy_mp = 3
                self.enemy_max_mp = 3
            
            self.reset_battle()
        
        def reset_battle(self):
            """Сбрасывает боевые переменные"""
            self.player_hp = self.player_max_hp
            self.player_mp = self.player_max_mp
            self.player_shield = 0
            self.player_defending = False
            self.player_blood_overflow = False
            self.player_mana_overflow = False
            
            self.enemy_shield = 0
            self.enemy_blood_overflow = False
            self.enemy_mana_overflow = False
        
        def add_health(self, character, amount):
            """Безопасное добавление здоровья"""
            if character == "player":
                old_hp = self.player_hp
                self.player_hp = min(self.player_max_hp, self.player_hp + amount)
                self.player_blood_overflow = self.player_hp > self.player_max_hp
                return self.player_hp - old_hp
            elif character == "enemy":
                old_hp = self.enemy_hp
                self.enemy_hp = min(self.enemy_max_hp, self.enemy_hp + amount)
                self.enemy_blood_overflow = self.enemy_hp > self.enemy_max_hp
                return self.enemy_hp - old_hp
        
        def add_mana(self, character, amount):
            """Безопасное добавление маны"""
            if character == "player":
                old_mp = self.player_mp
                self.player_mp = min(self.player_max_mp, self.player_mp + amount)
                self.player_mana_overflow = self.player_mp > self.player_max_mp
                return self.player_mp - old_mp
            elif character == "enemy":
                old_mp = self.enemy_mp
                self.enemy_mp = min(self.enemy_max_mp, self.enemy_mp + amount)
                self.enemy_mana_overflow = self.enemy_mp > self.enemy_max_mp
                return self.enemy_mp - old_mp
        
        def player_attack(self):
            """Атака игрока"""
            if self.enemy_hp <= 0:
                return "Противник уже побежден!"
            if self.player_mp >= 1:
                damage = 1
                if self.enemy_shield > 0:
                    self.enemy_shield -= 1
                    damage = 0
                self.enemy_hp = max(0, self.enemy_hp - damage)
                self.player_mp -= 1
                return f"Вы атакуете! Нанесено урона: {damage}"
            else:
                return "Недостаточно маны для атаки!"
        
        def player_defend(self):
            """Защита игрока"""
            if self.player_mp >= 1:
                self.player_shield += 1
                self.player_mp -= 1
                self.player_defending = True
                return "Вы защищаетесь! Щит увеличен."
            else:
                return "Недостаточно маны для защиты!"
        
        def enemy_turn(self):
            """Ход противника"""
            if self.enemy_hp <= 0:
                return "Противник побежден!"
            
            # Простая ИИ противника
            if self.enemy_mp >= 1:
                if self.player_shield > 0:
                    # Атакуем щит
                    self.player_shield -= 1
                    self.enemy_mp -= 1
                    return f"{self.enemy_name} атакует ваш щит!"
                else:
                    # Атакуем игрока
                    damage = 1
                    self.player_hp = max(0, self.player_hp - damage)
                    self.enemy_mp -= 1
                    return f"{self.enemy_name} атакует! Вы получаете {damage} урона!"
            else:
                return f"{self.enemy_name} восстанавливает ману!"
        
        def is_battle_over(self):
            """Проверяет, закончен ли бой"""
            return self.player_hp <= 0 or self.enemy_hp <= 0
        
        def get_battle_result(self):
            """Возвращает результат боя"""
            if self.player_hp <= 0:
                return "defeat"
            elif self.enemy_hp <= 0:
                return "victory"
            else:
                return "ongoing"

init python:
    battle_system = BattleSystem() 