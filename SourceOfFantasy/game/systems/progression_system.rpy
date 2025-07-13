# Система прокачки персонажа
init python:
    class ProgressionSystem:
        def __init__(self):
            # Основные характеристики игрока
            self.player_level = 1
            self.player_exp = 0
            self.player_exp_to_next = 100
            
            # Характеристики
            self.strength = 5      # Сила - влияет на физический урон
            self.agility = 5       # Ловкость - влияет на уклонение и критический удар
            self.intelligence = 5  # Интеллект - влияет на магический урон и ману
            self.charisma = 5      # Харизма - влияет на соблазнение и торговлю
            self.vitality = 5      # Живучесть - влияет на здоровье
            
            # Максимальные значения характеристик
            self.max_strength = 20
            self.max_agility = 20
            self.max_intelligence = 20
            self.max_charisma = 20
            self.max_vitality = 20
            
            # Очки характеристик для распределения
            self.stat_points = 0
            
            # Навыки
            self.skills = {
                "sword_mastery": {"level": 1, "exp": 0, "max_level": 10},
                "magic_mastery": {"level": 1, "exp": 0, "max_level": 10},
                "seduction_art": {"level": 1, "exp": 0, "max_level": 10},
                "trading": {"level": 1, "exp": 0, "max_level": 10},
                "stealth": {"level": 1, "exp": 0, "max_level": 10}
            }
            
            # Достижения
            self.achievements = {
                "first_victory": {"unlocked": False, "name": "Первая победа", "description": "Победите в первом бою"},
                "seduction_master": {"unlocked": False, "name": "Мастер соблазнения", "description": "Достигните 10 уровня в искусстве соблазнения"},
                "wealthy": {"unlocked": False, "name": "Богач", "description": "Накопите 1000 золота"},
                "explorer": {"unlocked": False, "name": "Исследователь", "description": "Посетите все локации"}
            }
        
        def gain_exp(self, amount):
            """Получение опыта"""
            self.player_exp += amount
            
            # Проверяем повышение уровня
            while self.player_exp >= self.player_exp_to_next:
                self.level_up()
        
        def level_up(self):
            """Повышение уровня"""
            self.player_exp -= self.player_exp_to_next
            self.player_level += 1
            self.player_exp_to_next = int(self.player_exp_to_next * 1.5)
            self.stat_points += 3  # 3 очка характеристик за уровень
            
            # Обновляем максимальные значения характеристик
            self.max_strength = 5 + (self.player_level - 1) * 2
            self.max_agility = 5 + (self.player_level - 1) * 2
            self.max_intelligence = 5 + (self.player_level - 1) * 2
            self.max_charisma = 5 + (self.player_level - 1) * 2
            self.max_vitality = 5 + (self.player_level - 1) * 2
            
            return f"Уровень повышен! Теперь вы {self.player_level} уровня. Доступно очков характеристик: {self.stat_points}"
        
        def increase_stat(self, stat_name):
            """Увеличение характеристики"""
            if self.stat_points <= 0:
                return "Недостаточно очков характеристик!"
            
            stat_mapping = {
                "strength": ("strength", "max_strength"),
                "agility": ("agility", "max_agility"),
                "intelligence": ("intelligence", "max_intelligence"),
                "charisma": ("charisma", "max_charisma"),
                "vitality": ("vitality", "max_vitality")
            }
            
            if stat_name in stat_mapping:
                stat, max_stat = stat_mapping[stat_name]
                if getattr(self, stat) < getattr(self, max_stat):
                    setattr(self, stat, getattr(self, stat) + 1)
                    self.stat_points -= 1
                    return f"{stat_name.capitalize()} увеличена! Осталось очков: {self.stat_points}"
                else:
                    return f"{stat_name.capitalize()} уже максимальна!"
            else:
                return "Неизвестная характеристика!"
        
        def gain_skill_exp(self, skill_name, amount):
            """Получение опыта навыка"""
            if skill_name in self.skills:
                skill = self.skills[skill_name]
                skill["exp"] += amount
                
                # Проверяем повышение уровня навыка
                exp_needed = skill["level"] * 50
                while skill["exp"] >= exp_needed and skill["level"] < skill["max_level"]:
                    skill["exp"] -= exp_needed
                    skill["level"] += 1
                    exp_needed = skill["level"] * 50
                    
                    # Проверяем достижения
                    if skill_name == "seduction_art" and skill["level"] >= 10:
                        self.unlock_achievement("seduction_master")
                
                return f"Навык {skill_name} получил {amount} опыта!"
            else:
                return "Неизвестный навык!"
        
        def unlock_achievement(self, achievement_id):
            """Разблокировка достижения"""
            if achievement_id in self.achievements and not self.achievements[achievement_id]["unlocked"]:
                self.achievements[achievement_id]["unlocked"] = True
                return f"Достижение разблокировано: {self.achievements[achievement_id]['name']}"
            return ""
        
        def get_player_stats(self):
            """Возвращает статистику игрока"""
            return {
                "level": self.player_level,
                "exp": self.player_exp,
                "exp_to_next": self.player_exp_to_next,
                "strength": self.strength,
                "agility": self.agility,
                "intelligence": self.intelligence,
                "charisma": self.charisma,
                "vitality": self.vitality,
                "stat_points": self.stat_points
            }
        
        def get_skill_level(self, skill_name):
            """Возвращает уровень навыка"""
            if skill_name in self.skills:
                return self.skills[skill_name]["level"]
            return 0
        
        def calculate_battle_bonuses(self):
            """Рассчитывает бонусы для боя"""
            return {
                "damage_bonus": self.strength * 0.5,
                "magic_bonus": self.intelligence * 0.5,
                "dodge_chance": self.agility * 2,
                "critical_chance": self.agility * 1.5,
                "max_hp_bonus": self.vitality * 2,
                "max_mp_bonus": self.intelligence * 1.5
            }
        
        def calculate_seduction_bonuses(self):
            """Рассчитывает бонусы для соблазнения"""
            return {
                "charm_bonus": self.charisma * 2,
                "confidence_bonus": self.charisma * 1.5,
                "skill_bonus": self.skills["seduction_art"]["level"] * 5
            }

# Создаем глобальный экземпляр системы прокачки
init python:
    progression_system = ProgressionSystem() 