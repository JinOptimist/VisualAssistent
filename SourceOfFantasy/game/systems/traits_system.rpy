# Система особенностей персонажа
init python:
    class TraitsSystem:
        def __init__(self):
            # Словарь всех доступных особенностей
            self.all_traits = {
                "absolute_polyglot": {
                    "name": "Абсолютный полиглот",
                    "description": "Вы понимаете А-а-абсолютно все языки",
                    "cost": 50
                },
                "strongman": {
                    "name": "Силач",
                    "description": "Вы были хорошим ребёнком и съедали всю кашу\n|Сила +1|",
                    "cost": 2
                },
                "weakling": {
                    "name": "Дохляк",
                    "description": "Могли бы в детстве хоть пару раз присесть.\nВаши силы слабые \n|Сила -1|",
                    "cost": -2
                },
                "acrobat": {
                    "name": "Ловкач",
                    "description": "Кто бы мог подумать, что жонглирование вам поможет в жизни\n|Ловкость +1|",
                    "cost": 2
                },
                "elephant_in_china_shop": {
                    "name": "Слон в посудной лавке",
                    "description": "Железная посуда, ваше единственное спасение\n|Ловкость -1|",
                    "cost": -2
                },
                "smart_guy": {
                    "name": "Умник",
                    "description": "Вы не считаете себя умным. Просто все вокруг глупее вас\n|Интеллект +1|",
                    "cost": 2
                },
                "fool": {
                    "name": "Балбес",
                    "description": "Вас ещё ни разу не назвали дураком. Или назвали, но вы не поняли этого, а может просто забыли\n|Интеллект -1|",
                    "cost": -2
                },
                "black_cat": {
                    "name": "Чёрный кот",
                    "description": "|Удача -1|",
                    "cost": -2
                },
                "lucky_guy": {
                    "name": "Удачник",
                    "description": "Какой стороной упадёт монетка? Конечно же нужной вам\n|Удача +1|",
                    "cost": 2
                },
                "commoner": {
                    "name": "Простолюдин",
                    "description": "Герой учиться всему на лету. Почувствуй же себя в шкуре НПС, потеряй бафф на прокачку\n|скорость роста опыта x0.2|",
                    "cost": -5
                }
            }
            
            # Выбранные особенности игрока
            self.selected_traits = []
            
            # Начальные очки развития
            self.development_points = 10
        
        def get_trait(self, trait_id):
            """Возвращает данные особенности по ID"""
            return self.all_traits.get(trait_id, None)
        
        def get_all_traits(self):
            """Возвращает все доступные особенности"""
            return self.all_traits
        
        def select_trait(self, trait_id):
            """Выбирает особенность"""
            # Валидация входных данных
            validation_result = self._validate_trait_selection(trait_id)
            if not validation_result["success"]:
                return False, validation_result["message"]
            
            trait = self.all_traits[trait_id]
            cost = trait["cost"]
            
            # Обновляем состояние
            self._add_trait_to_selection(trait_id)
            self._update_development_points(cost)
            
            return True, f"Выбрана особенность: {trait['name']}"
        
        def _validate_trait_selection(self, trait_id):
            """Проверяет возможность выбора особенности"""
            if trait_id not in self.all_traits:
                return {"success": False, "message": "Особенность не найдена!"}
            
            if trait_id in self.selected_traits:
                return {"success": False, "message": "Эта особенность уже выбрана!"}
            
            trait = self.all_traits[trait_id]
            cost = trait["cost"]
            
            if self._is_positive_trait(cost) and not self._has_enough_points(cost):
                return {
                    "success": False, 
                    "message": f"Недостаточно очков развития! Нужно: {cost}, доступно: {self.development_points}"
                }
            
            return {"success": True, "message": ""}
        
        def _add_trait_to_selection(self, trait_id):
            """Добавляет особенность в выбор"""
            self.selected_traits.append(trait_id)
        
        def _update_development_points(self, cost):
            """Обновляет очки развития"""
            if self._is_positive_trait(cost):
                self.development_points -= cost
            else:
                self.development_points += abs(cost)
        
        def _is_positive_trait(self, cost):
            """Проверяет, является ли особенность положительной"""
            return cost > 0
        
        def _has_enough_points(self, cost):
            """Проверяет, хватает ли очков для покупки"""
            return self.development_points >= cost
        
        def deselect_trait(self, trait_id):
            """Отменяет выбор особенности"""
            # Валидация
            if trait_id not in self.selected_traits:
                return False, "Эта особенность не выбрана!"
            
            trait = self.all_traits[trait_id]
            cost = trait["cost"]
            
            # Обновляем состояние
            self._remove_trait_from_selection(trait_id)
            self._restore_development_points(cost)
            
            return True, f"Отменена особенность: {trait['name']}"
        
        def _remove_trait_from_selection(self, trait_id):
            """Удаляет особенность из выбора"""
            self.selected_traits.remove(trait_id)
        
        def _restore_development_points(self, cost):
            """Восстанавливает очки развития при отмене выбора"""
            if self._is_positive_trait(cost):
                self.development_points += cost
            else:
                self.development_points -= abs(cost)
        
        def get_selected_traits(self):
            """Возвращает список выбранных особенностей"""
            return [self.all_traits[trait_id] for trait_id in self.selected_traits]
        
        def get_development_points(self):
            """Возвращает количество очков развития"""
            return self.development_points
        
        def get_total_trait_cost(self):
            """Возвращает общую стоимость выбранных особенностей"""
            total = 0
            for trait_id in self.selected_traits:
                total += self.all_traits[trait_id]["cost"]
            return total
        
        def reset_selection(self):
            """Сбрасывает выбор особенностей"""
            self.selected_traits = []
            self.development_points = 10
        
        def confirm_selection(self):
            """Подтверждает выбор особенностей"""
            if not self.selected_traits:
                return False, "Выберите хотя бы одну особенность!"
            
            return True, "Выбор особенностей подтвержден!"

    # Создаем глобальный экземпляр системы особенностей
    traits_system = TraitsSystem() 