# Система соблазнения
init python:
    class SeductionSystem:
        def __init__(self):
            # Характеристики игрока для соблазнения
            self.player_charm = 5
            self.player_max_charm = 10
            self.player_confidence = 5
            self.player_max_confidence = 10
            self.player_reputation = 0  # -10 до 10
            
            # Цель соблазнения
            self.target_name = "Неизвестная"
            self.target_affection = 0  # 0 до 100
            self.target_difficulty = 50  # Сложность соблазнения
            self.target_personality = "normal"  # normal, shy, aggressive, mysterious
            
            # Словарь с данными целей
            self.targets = {
                "merchant_daughter": {
                    "name": "Дочь торговца",
                    "affection": 0,
                    "difficulty": 40,
                    "personality": "shy",
                    "description": "Застенчивая девушка, которая помогает отцу в лавке"
                },
                "noble_lady": {
                    "name": "Благородная леди",
                    "affection": 0,
                    "difficulty": 70,
                    "personality": "mysterious",
                    "description": "Таинственная аристократка с загадочным прошлым"
                },
                "tavern_wench": {
                    "name": "Таверная девка",
                    "affection": 0,
                    "difficulty": 30,
                    "personality": "aggressive",
                    "description": "Дерзкая и прямолинейная девушка из таверны"
                }
            }
        
        def start_seduction(self, target_type="merchant_daughter"):
            """Начинает сцену соблазнения с указанной целью"""
            if target_type in self.targets:
                target_data = self.targets[target_type]
                self.target_name = target_data["name"]
                self.target_affection = target_data["affection"]
                self.target_difficulty = target_data["difficulty"]
                self.target_personality = target_data["personality"]
            else:
                # Значения по умолчанию
                self.target_name = "Неизвестная"
                self.target_affection = 0
                self.target_difficulty = 50
                self.target_personality = "normal"
        
        def compliment(self, compliment_type="general"):
            """Делает комплимент"""
            base_chance = 60
            charm_bonus = self.player_charm * 2
            confidence_bonus = self.player_confidence * 1.5
            
            # Модификаторы в зависимости от типа комплимента
            type_modifiers = {
                "general": 0,
                "appearance": 10,
                "intelligence": 15,
                "personality": 20,
                "flirtatious": 25
            }
            
            modifier = type_modifiers.get(compliment_type, 0)
            total_chance = base_chance + charm_bonus + confidence_bonus + modifier
            
            # Проверяем успех
            if renpy.random.randint(1, 100) <= total_chance:
                affection_gain = renpy.random.randint(5, 15)
                self.target_affection = min(100, self.target_affection + affection_gain)
                self.player_confidence = min(self.player_max_confidence, self.player_confidence + 1)
                return f"Успех! {self.target_name} оценила ваш комплимент. Привязанность +{affection_gain}"
            else:
                self.player_confidence = max(0, self.player_confidence - 1)
                return f"Неудача! {self.target_name} не оценила ваш комплимент."
        
        def gift(self, gift_type="flower"):
            """Дарит подарок"""
            gift_values = {
                "flower": 10,
                "jewelry": 25,
                "book": 15,
                "wine": 20,
                "expensive": 40
            }
            
            value = gift_values.get(gift_type, 5)
            self.target_affection = min(100, self.target_affection + value)
            return f"Вы подарили {gift_type}. Привязанность +{value}"
        
        def conversation(self, topic="casual"):
            """Ведет разговор на определенную тему"""
            topics = {
                "casual": {"chance": 70, "gain": (5, 10)},
                "personal": {"chance": 50, "gain": (10, 20)},
                "romantic": {"chance": 40, "gain": (15, 25)},
                "intellectual": {"chance": 60, "gain": (8, 15)}
            }
            
            topic_data = topics.get(topic, topics["casual"])
            chance = topic_data["chance"] + self.player_charm * 3
            
            if renpy.random.randint(1, 100) <= chance:
                gain = renpy.random.randint(topic_data["gain"][0], topic_data["gain"][1])
                self.target_affection = min(100, self.target_affection + gain)
                return f"Отличная беседа! Привязанность +{gain}"
            else:
                return f"Разговор не задался..."
        
        def is_seduction_successful(self):
            """Проверяет, успешно ли соблазнение"""
            return self.target_affection >= self.target_difficulty
        
        def get_seduction_progress(self):
            """Возвращает прогресс соблазнения в процентах"""
            return (self.target_affection / self.target_difficulty) * 100
        
        def reset_seduction(self):
            """Сбрасывает состояние соблазнения"""
            self.target_affection = 0
            self.player_confidence = 5

init python:
    seduction_system = SeductionSystem() 