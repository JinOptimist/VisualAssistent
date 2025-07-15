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
            self.player_stream_attack_is_active = False
            self.player_stream_attack_turns = 0
            
            # Переменные противника
            self.enemy_name = "Гоблин"
            self.enemy_hp = 5
            self.enemy_max_hp = 5
            self.enemy_mp = 3
            self.enemy_max_mp = 3
            self.enemy_shield = 0
            self.enemy_blood_overflow = False
            self.enemy_mana_overflow = False
            self.enemy_stream_attack_is_active = False
            self.enemy_stream_attack_turns = 0
            
            # Словарь с данными противников
            self.enemies = {
                "goblin": {
                    "name": "Гоблин",
                    "hp": 5,
                    "max_hp": 5,
                    "mp": 3,
                    "max_mp": 3
                },
                "orc": {
                    "name": "Орк",
                    "hp": 8,
                    "max_hp": 8,
                    "mp": 2,
                    "max_mp": 2
                },
                "troll": {
                    "name": "Тролль",
                    "hp": 12,
                    "max_hp": 12,
                    "mp": 1,
                    "max_mp": 1
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
            self.player_stream_attack_is_active = False
            self.player_stream_attack_turns = 0
            
            self.enemy_shield = 0
            self.enemy_blood_overflow = False
            self.enemy_mana_overflow = False
            self.enemy_stream_attack_is_active = False
            self.enemy_stream_attack_turns = 0
        
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
        
        def player_projectile_attack(self):
            """Атака снарядом игрока"""
            if self.enemy_hp <= 0:
                return "Противник уже побежден!"
            if self.player_stream_attack_is_active:
                return "Вы находитесь под эффектом 'Атака Потоком' и не можете использовать другие атаки!"
            if self.player_mp >= 1:
                damage = 1
                if self.enemy_shield > 0:
                    self.enemy_shield -= 1
                    damage = 0
                self.enemy_hp = max(0, self.enemy_hp - damage)
                self.player_mp -= 1
                return f"Вы используете атаку снарядом! Нанесено урона: {damage}"
            else:
                return "Недостаточно маны для атаки снарядом!"
        
        def player_attack(self):
            """Базовая атака игрока (атака снарядом)"""
            return self.player_projectile_attack()
        
        def player_stream_attack(self):
            """Атака потоком игрока"""
            if self.enemy_hp <= 0:
                return "Противник уже побежден!"
            if self.player_stream_attack_is_active:
                return "Вы уже находитесь под эффектом 'Атака Потоком'!"
            if self.player_mp >= 2:
                # Активируем статус "Атака Потоком"
                self.player_stream_attack_is_active = True
                self.player_stream_attack_turns = 3
                self.player_mp -= 2
                
                # Немедленное нанесение урона
                damage = 1
                if self.enemy_shield > 0:
                    self.enemy_shield -= 1
                    damage = 0
                self.enemy_hp = max(0, self.enemy_hp - damage)
                
                return f"Вы активируете атаку потоком! Нанесено урона: {damage}. Эффект активен 3 хода."
            else:
                return "Недостаточно маны для атаки потоком! (требуется 2 MP)"
        
        def enemy_stream_attack(self):
            """Атака потоком противника"""
            if self.player_hp <= 0:
                return "Игрок побежден!"
            if self.enemy_stream_attack_is_active:
                return f"{self.enemy_name} уже находится под эффектом 'Атака Потоком'!"
            if self.enemy_mp >= 2:
                # Активируем статус "Атака Потоком"
                self.enemy_stream_attack_is_active = True
                self.enemy_stream_attack_turns = 3
                self.enemy_mp -= 2
                
                # Немедленное нанесение урона
                damage = 1
                if self.player_shield > 0:
                    self.player_shield -= 1
                    damage = 0
                elif self.player_defending:
                    self.player_defending = False
                    damage = 0
                self.player_hp = max(0, self.player_hp - damage)
                
                return f"{self.enemy_name} активирует атаку потоком! Вы получаете {damage} урона. Эффект активен 3 хода."
            else:
                return f"{self.enemy_name} не может использовать атаку потоком! (требуется 2 MP)"
        
        def player_defend(self):
            """Защита игрока"""
            if self.player_stream_attack_is_active:
                return "Вы находитесь под эффектом 'Атака Потоком' и не можете защищаться!"
            if self.player_mp >= 1:
                self.player_shield += 1
                self.player_mp -= 1
                self.player_defending = True
                return "Вы защищаетесь! Щит увеличен."
            else:
                return "Недостаточно маны для защиты!"
        
        def player_shield_spell(self):
            """Создание щита игроком"""
            if self.player_stream_attack_is_active:
                return "Вы находитесь под эффектом 'Атака Потоком' и не можете создавать щиты!"
            if self.player_mp >= 1:
                self.player_shield += 1
                self.player_mp -= 1
                return "Вы создаете щит! Щит увеличен."
            else:
                return "Недостаточно маны для создания щита!"
        
        def player_heal(self):
            """Лечение игрока"""
            if self.player_stream_attack_is_active:
                return "Вы находитесь под эффектом 'Атака Потоком' и не можете лечиться!"
            if self.player_mp >= 2:
                healed = self.add_health("player", 2)
                self.player_mp -= 2
                return f"Вы лечитесь! Восстановлено здоровья: {healed}"
            else:
                return "Недостаточно маны для лечения!"
        
        def apply_stream_attack_effect(self, character):
            """Применяет эффект 'Атака Потоком' к указанному персонажу"""
            if character == "player" and self.player_stream_attack_is_active and self.player_stream_attack_turns > 0:
                damage = 1
                if self.enemy_shield > 0:
                    self.enemy_shield -= 1
                    damage = 0
                self.enemy_hp = max(0, self.enemy_hp - damage)
                self.player_stream_attack_turns -= 1
                if self.player_stream_attack_turns <= 0:
                    self.player_stream_attack_is_active = False
                return f"Автоматическая атака потоком! Нанесено урона: {damage}. Осталось ходов: {self.player_stream_attack_turns}"
            elif character == "enemy" and self.enemy_stream_attack_is_active and self.enemy_stream_attack_turns > 0:
                damage = 1
                if self.player_shield > 0:
                    self.player_shield -= 1
                    damage = 0
                elif self.player_defending:
                    self.player_defending = False
                    damage = 0
                self.player_hp = max(0, self.player_hp - damage)
                self.enemy_stream_attack_turns -= 1
                if self.enemy_stream_attack_turns <= 0:
                    self.enemy_stream_attack_is_active = False
                return f"{self.enemy_name} использует автоматическую атаку потоком! Вы получаете {damage} урона. Осталось ходов: {self.enemy_stream_attack_turns}"
            return None
        
        def check_stream_attack_status(self, character):
            """Проверяет и обновляет статус 'Атака Потоком' персонажа"""
            if character == "player":
                if self.player_stream_attack_is_active and self.player_stream_attack_turns <= 0:
                    self.player_stream_attack_is_active = False
                    return "Статус 'Атака Потоком' снят."
            elif character == "enemy":
                if self.enemy_stream_attack_is_active and self.enemy_stream_attack_turns <= 0:
                    self.enemy_stream_attack_is_active = False
                    return f"Статус 'Атака Потоком' {self.enemy_name} снят."
            return None
        
        def apply_overflow_effects(self, character):
            """Применяет эффекты статусов переполнения к указанному персонажу"""
            if character == "player":
                if self.player_blood_overflow:
                    self.player_hp = max(0, self.player_hp - 1)
                    self.player_mp = max(0, self.player_mp - 2)
                if self.player_mana_overflow:
                    self.player_hp = max(0, self.player_hp - 1)
                    self.player_mp = max(0, self.player_mp - 2)
            elif character == "enemy":
                if self.enemy_blood_overflow:
                    self.enemy_hp = max(0, self.enemy_hp - 1)
                    self.enemy_mp = max(0, self.enemy_mp - 2)
                if self.enemy_mana_overflow:
                    self.enemy_hp = max(0, self.enemy_hp - 1)
                    self.enemy_mp = max(0, self.enemy_mp - 2)
        
        def check_overflow_status(self, character):
            """Проверяет и обновляет статусы переполнения персонажа"""
            if character == "player":
                # Проверяем переполнение кровью
                if self.player_hp <= self.player_max_hp:
                    self.player_blood_overflow = False
                # Проверяем переполнение маной
                if self.player_mp <= self.player_max_mp:
                    self.player_mana_overflow = False
            elif character == "enemy":
                # Проверяем переполнение кровью
                if self.enemy_hp <= self.enemy_max_hp:
                    self.enemy_blood_overflow = False
                # Проверяем переполнение маной
                if self.enemy_mp <= self.enemy_max_mp:
                    self.enemy_mana_overflow = False
        
        def enemy_turn(self):
            """Ход противника"""
            if self.enemy_hp <= 0:
                return "Противник побежден!"
            
            # Если противник под эффектом "Атака Потоком", применяем автоматическую атаку
            if self.enemy_stream_attack_is_active:
                return self.apply_stream_attack_effect("enemy")
            
            # Простая ИИ противника с новой атакой потоком
            if self.enemy_mp >= 2:
                # 30% шанс выбрать атаку потоком, если достаточно маны
                import random
                choice = random.random()
                
                if choice < 0.3:  # Атака потоком
                    return self.enemy_stream_attack()
                elif choice < 0.533:  # Атака снарядом
                    damage = 1
                    if self.player_shield > 0:
                        self.player_shield -= 1
                        damage = 0
                    elif self.player_defending:
                        self.player_defending = False
                        damage = 0
                    self.player_hp = max(0, self.player_hp - damage)
                    self.enemy_mp -= 1
                    return f"{self.enemy_name} использует атаку снарядом! Вы получаете {damage} урона!"
                elif choice < 0.766:  # Создание щита
                    self.enemy_shield += 1
                    self.enemy_mp -= 1
                    return f"{self.enemy_name} создает щит!"
                else:  # Лечение
                    if self.enemy_mp >= 2:
                        healed = self.add_health("enemy", 2)
                        self.enemy_mp -= 2
                        return f"{self.enemy_name} лечится! Восстановлено здоровья: {healed}"
                    else:
                        return f"{self.enemy_name} пропускает ход!"
            elif self.enemy_mp >= 1:
                # Если маны мало, только атака снарядом или создание щита
                import random
                if random.random() < 0.5:  # Атака снарядом
                    damage = 1
                    if self.player_shield > 0:
                        self.player_shield -= 1
                        damage = 0
                    elif self.player_defending:
                        self.player_defending = False
                        damage = 0
                    self.player_hp = max(0, self.player_hp - damage)
                    self.enemy_mp -= 1
                    return f"{self.enemy_name} использует атаку снарядом! Вы получаете {damage} урона!"
                else:  # Создание щита
                    self.enemy_shield += 1
                    self.enemy_mp -= 1
                    return f"{self.enemy_name} создает щит!"
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