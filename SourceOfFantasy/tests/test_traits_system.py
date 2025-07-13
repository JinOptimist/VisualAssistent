#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Тесты для системы особенностей персонажа
"""

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
                "description": "Вы были хорошим ребёнком и съедали всю кашу\n[Сила +1]",
                "cost": 2
            },
            "weakling": {
                "name": "Дохляк",
                "description": "Могли бы в детстве хоть пару раз присесть.\nВаши силы слабые [Сила -1]",
                "cost": -2
            },
            "acrobat": {
                "name": "Ловкач",
                "description": "Кто бы мог подумать, что жонглирование вам поможет в жизни\n[Ловкость +1]",
                "cost": 2
            },
            "elephant_in_china_shop": {
                "name": "Слон в посудной лавке",
                "description": "Железная посуда, ваше единственное спасение\n[Ловкость -1]",
                "cost": -2
            },
            "smart_guy": {
                "name": "Умник",
                "description": "Вы не считаете себя умным. Просто все вокруг глупее вас\n[Интеллект +1]",
                "cost": 2
            },
            "fool": {
                "name": "Балбес",
                "description": "Вас ещё ни разу не назвали дураком. Или назвали, но вы не поняли этого, а может просто забыли\n[Интеллект -1]",
                "cost": -2
            },
            "black_cat": {
                "name": "Чёрный кот",
                "description": "[Удача -1]",
                "cost": -2
            },
            "lucky_guy": {
                "name": "Удачник",
                "description": "Какой стороной упадёт монетка? Конечно же нужной вам\n[Удача +1]",
                "cost": 2
            },
            "commoner": {
                "name": "Простолюдин",
                "description": "Герой учиться всему на лету. Почувствуй же себя в шкуре НПС, потеряй бафф на прокачку\n[скорость роста опыта падает с 500% до 100%]",
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
        if trait_id not in self.all_traits:
            return False, "Особенность не найдена!"
        
        if trait_id in self.selected_traits:
            return False, "Эта особенность уже выбрана!"
        
        trait = self.all_traits[trait_id]
        cost = trait["cost"]
        
        # Проверяем, хватает ли очков
        if cost > 0 and self.development_points < cost:
            return False, f"Недостаточно очков развития! Нужно: {cost}, доступно: {self.development_points}"
        
        # Добавляем особенность
        self.selected_traits.append(trait_id)
        
        # Тратим очки (если особенность положительная)
        if cost > 0:
            self.development_points -= cost
        else:
            # Если особенность отрицательная, получаем очки
            self.development_points += abs(cost)
        
        return True, f"Выбрана особенность: {trait['name']}"
    
    def deselect_trait(self, trait_id):
        """Отменяет выбор особенности"""
        if trait_id not in self.selected_traits:
            return False, "Эта особенность не выбрана!"
        
        trait = self.all_traits[trait_id]
        cost = trait["cost"]
        
        # Удаляем особенность
        self.selected_traits.remove(trait_id)
        
        # Возвращаем очки (если особенность положительная)
        if cost > 0:
            self.development_points += cost
        else:
            # Если особенность отрицательная, тратим очки
            self.development_points -= abs(cost)
        
        return True, f"Отменена особенность: {trait['name']}"
    
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

def test_traits_system():
    """Основной тест системы особенностей"""
    print("Запуск тестов системы особенностей...")
    
    # Создаем экземпляр системы
    traits_system = TraitsSystem()
    
    # Тест 1: Проверка загрузки особенностей
    print("\nТест 1: Проверка загрузки особенностей")
    all_traits = traits_system.get_all_traits()
    print(f"Загружено особенностей: {len(all_traits)}")
    
    expected_traits = [
        "Абсолютный полиглот", "Силач", "Дохляк", "Ловкач", 
        "Слон в посудной лавке", "Умник", "Балбес", "Чёрный кот", 
        "Удачник", "Простолюдин"
    ]
    
    loaded_trait_names = [trait["name"] for trait in all_traits.values()]
    for expected in expected_traits:
        if expected in loaded_trait_names:
            print(f"✓ {expected}")
        else:
            print(f"✗ {expected} - НЕ НАЙДЕН")
    
    # Тест 2: Проверка начальных очков
    print("\nТест 2: Проверка начальных очков")
    points = traits_system.get_development_points()
    print(f"Начальные очки развития: {points}")
    assert points == 10, f"Ожидалось 10 очков, получено {points}"
    print("✓ Начальные очки корректны")
    
    # Тест 3: Выбор положительной особенности
    print("\nТест 3: Выбор положительной особенности")
    success, message = traits_system.select_trait("strongman")
    print(f"Результат: {message}")
    assert success, f"Ошибка при выборе особенности: {message}"
    
    points_after = traits_system.get_development_points()
    print(f"Очки после выбора: {points_after}")
    assert points_after == 8, f"Ожидалось 8 очков, получено {points_after}"
    print("✓ Положительная особенность выбрана корректно")
    
    # Тест 4: Выбор отрицательной особенности
    print("\nТест 4: Выбор отрицательной особенности")
    success, message = traits_system.select_trait("weakling")
    print(f"Результат: {message}")
    assert success, f"Ошибка при выборе особенности: {message}"
    
    points_after_negative = traits_system.get_development_points()
    print(f"Очки после выбора отрицательной: {points_after_negative}")
    # После выбора "Дохляк" (-2) очки должны вернуться к 10 (8 + 2 = 10)
    assert points_after_negative == 10, f"Ожидалось 10 очков, получено {points_after_negative}"
    print("✓ Отрицательная особенность выбрана корректно")
    
    # Тест 4.1: Проверка выбора отрицательной особенности с чистого листа
    print("\nТест 4.1: Выбор отрицательной особенности с чистого листа")
    traits_system.reset_selection()
    success, message = traits_system.select_trait("weakling")
    print(f"Результат: {message}")
    assert success, f"Ошибка при выборе особенности: {message}"
    
    points_after_negative_clean = traits_system.get_development_points()
    print(f"Очки после выбора отрицательной с чистого листа: {points_after_negative_clean}")
    # После выбора "Дохляк" (-2) с 10 очков должно стать 12 (10 + 2 = 12)
    assert points_after_negative_clean == 12, f"Ожидалось 12 очков, получено {points_after_negative_clean}"
    print("✓ Отрицательная особенность с чистого листа работает корректно")
    
    # Тест 5: Проверка выбранных особенностей
    print("\nТест 5: Проверка выбранных особенностей")
    selected = traits_system.get_selected_traits()
    print(f"Выбрано особенностей: {len(selected)}")
    for trait in selected:
        print(f"  - {trait['name']} (стоимость: {trait['cost']})")
    
    assert len(selected) == 1, f"Ожидалось 1 особенность, выбрано {len(selected)}"
    print("✓ Выбранные особенности корректны")
    
    # Тест 6: Отмена выбора особенности
    print("\nТест 6: Отмена выбора особенности")
    success, message = traits_system.deselect_trait("weakling")
    print(f"Результат: {message}")
    assert success, f"Ошибка при отмене особенности: {message}"
    
    points_after_deselect = traits_system.get_development_points()
    print(f"Очки после отмены: {points_after_deselect}")
    # После отмены "Дохляк" (-2) очки должны вернуться к 10 (12 - 2 = 10)
    assert points_after_deselect == 10, f"Ожидалось 10 очков, получено {points_after_deselect}"
    print("✓ Отмена выбора работает корректно")
    
    # Тест 7: Проверка недостатка очков
    print("\nТест 7: Проверка недостатка очков")
    # Пытаемся выбрать дорогую особенность
    success, message = traits_system.select_trait("absolute_polyglot")
    print(f"Результат: {message}")
    assert not success, "Должна быть ошибка недостатка очков"
    print("✓ Проверка недостатка очков работает")
    
    # Тест 8: Сброс выбора
    print("\nТест 8: Сброс выбора")
    traits_system.reset_selection()
    points_after_reset = traits_system.get_development_points()
    selected_after_reset = traits_system.get_selected_traits()
    
    print(f"Очки после сброса: {points_after_reset}")
    print(f"Выбрано особенностей после сброса: {len(selected_after_reset)}")
    
    assert points_after_reset == 10, f"Ожидалось 10 очков, получено {points_after_reset}"
    assert len(selected_after_reset) == 0, f"Ожидалось 0 особенностей, выбрано {len(selected_after_reset)}"
    print("✓ Сброс выбора работает корректно")
    
    # Тест 9: Подтверждение выбора
    print("\nТест 9: Подтверждение выбора")
    # Без выбора особенностей
    success, message = traits_system.confirm_selection()
    print(f"Результат без выбора: {message}")
    assert not success, "Должна быть ошибка отсутствия выбора"
    
    # С выбором особенностей
    traits_system.select_trait("lucky_guy")
    success, message = traits_system.confirm_selection()
    print(f"Результат с выбором: {message}")
    assert success, f"Ошибка при подтверждении: {message}"
    print("✓ Подтверждение выбора работает корректно")
    
    # Тест 10: Комбинированный тест - выбор нескольких особенностей
    print("\nТест 10: Комбинированный тест")
    traits_system.reset_selection()
    
    # Выбираем отрицательную особенность для получения дополнительных очков
    success, message = traits_system.select_trait("weakling")
    print(f"Выбор 'Дохляк': {message}")
    points_after_weakling = traits_system.get_development_points()
    print(f"Очки после 'Дохляк': {points_after_weakling}")
    
    # Выбираем ещё одну отрицательную особенность
    success, message = traits_system.select_trait("fool")
    print(f"Выбор 'Балбес': {message}")
    points_after_fool = traits_system.get_development_points()
    print(f"Очки после 'Балбес': {points_after_fool}")
    
    # Теперь выбираем положительную особенность
    success, message = traits_system.select_trait("strongman")
    print(f"Выбор 'Силач': {message}")
    points_after_strongman = traits_system.get_development_points()
    print(f"Очки после 'Силач': {points_after_strongman}")
    
    # Проверяем итоговое количество очков
    # Начальные 10 + 2 (Дохляк) + 2 (Балбес) - 2 (Силач) = 12
    assert points_after_strongman == 12, f"Ожидалось 12 очков, получено {points_after_strongman}"
    print("✓ Комбинированный тест пройден")
    
    print("\nВсе тесты пройдены успешно! ✓")

if __name__ == "__main__":
    test_traits_system() 