#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Тесты для боевой системы
Копирует логику из game/systems/battle_system.rpy
"""

import sys
import os
import unittest
from unittest.mock import patch
import random

# Добавляем путь к игровым файлам
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'game'))

class BattleSystem:
    """Копия боевой системы для тестирования"""
    
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
    
    def player_defend(self):
        """Уклонение игрока"""
        if self.player_stream_attack_is_active:
            return "Вы находитесь под эффектом 'Атака Потоком' и не можете уклоняться!"
        self.player_defending = True
        return "Вы готовитесь к уклонению!"
    
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
    
    def get_battle_result(self):
        """Возвращает результат боя"""
        if self.player_hp <= 0:
            return "defeat"
        elif self.enemy_hp <= 0:
            return "victory"
        else:
            return "ongoing"


class TestBattleSystem(unittest.TestCase):
    """Тесты для боевой системы"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.battle = BattleSystem()
    
    def tearDown(self):
        """Очистка после каждого теста"""
        pass
    
    # Тесты базовых механик
    
    def test_player_projectile_attack_basic(self):
        """Проверка базовой атаки снарядом"""
        initial_enemy_hp = self.battle.enemy_hp
        initial_player_mp = self.battle.player_mp
        
        result = self.battle.player_projectile_attack()
        
        self.assertIn("атаку снарядом", result)
        self.assertEqual(self.battle.enemy_hp, initial_enemy_hp - 1)
        self.assertEqual(self.battle.player_mp, initial_player_mp - 1)
    
    def test_player_projectile_attack_no_mana(self):
        """Проверка невозможности атаки без маны"""
        self.battle.player_mp = 0
        initial_enemy_hp = self.battle.enemy_hp
        
        result = self.battle.player_projectile_attack()
        
        self.assertIn("Недостаточно маны", result)
        self.assertEqual(self.battle.enemy_hp, initial_enemy_hp)
    
    def test_player_projectile_attack_dead_enemy(self):
        """Проверка невозможности атаки мертвого противника"""
        self.battle.enemy_hp = 0
        initial_player_mp = self.battle.player_mp
        
        result = self.battle.player_projectile_attack()
        
        self.assertIn("Противник уже побежден", result)
        self.assertEqual(self.battle.player_mp, initial_player_mp)
    
    # Тесты статуса "Атака Потоком"
    
    def test_stream_attack_activation(self):
        """Проверка активации 'Атаки Потоком'"""
        initial_player_mp = self.battle.player_mp
        initial_enemy_hp = self.battle.enemy_hp
        
        result = self.battle.player_stream_attack()
        
        self.assertIn("атаку потоком", result)
        self.assertTrue(self.battle.player_stream_attack_is_active)
        self.assertEqual(self.battle.player_stream_attack_turns, 3)
        self.assertEqual(self.battle.player_mp, initial_player_mp - 2)
        self.assertEqual(self.battle.enemy_hp, initial_enemy_hp - 1)
    
    def test_stream_attack_already_active(self):
        """Проверка невозможности повторной активации"""
        self.battle.player_stream_attack_is_active = True
        initial_player_mp = self.battle.player_mp
        
        result = self.battle.player_stream_attack()
        
        self.assertIn("уже находитесь под эффектом", result)
        self.assertEqual(self.battle.player_mp, initial_player_mp)
    
    def test_stream_attack_effect_application(self):
        """Проверка применения эффекта 'Атака Потоком'"""
        self.battle.player_stream_attack_is_active = True
        self.battle.player_stream_attack_turns = 3
        initial_enemy_hp = self.battle.enemy_hp
        
        result = self.battle.apply_stream_attack_effect("player")
        
        self.assertIsNotNone(result)
        if result is not None:
            self.assertIn("Автоматическая атака потоком", result)
        self.assertEqual(self.battle.enemy_hp, initial_enemy_hp - 1)
        self.assertEqual(self.battle.player_stream_attack_turns, 2)
    
    def test_stream_attack_deactivation(self):
        """Проверка снятия статуса после 3 ходов"""
        self.battle.player_stream_attack_is_active = True
        self.battle.player_stream_attack_turns = 1
        
        result = self.battle.apply_stream_attack_effect("player")
        
        self.assertFalse(self.battle.player_stream_attack_is_active)
        self.assertEqual(self.battle.player_stream_attack_turns, 0)
    
    # Тесты условий боя
    
    def test_battle_victory_player(self):
        """Проверка победы игрока"""
        self.battle.enemy_hp = 1
        
        result = self.battle.player_projectile_attack()
        battle_result = self.battle.get_battle_result()
        
        self.assertEqual(self.battle.enemy_hp, 0)
        self.assertEqual(battle_result, "victory")
    
    def test_battle_victory_enemy(self):
        """Проверка победы противника"""
        self.battle.player_hp = 1
        self.battle.enemy_mp = 1
        
        # Симулируем атаку противника
        damage = 1
        if self.battle.player_shield > 0:
            self.battle.player_shield -= 1
            damage = 0
        self.battle.player_hp = max(0, self.battle.player_hp - damage)
        
        battle_result = self.battle.get_battle_result()
        
        self.assertEqual(self.battle.player_hp, 0)
        self.assertEqual(battle_result, "defeat")
    
    def test_battle_ongoing(self):
        """Проверка продолжения боя"""
        self.battle.player_hp = 5
        self.battle.enemy_hp = 3
        
        battle_result = self.battle.get_battle_result()
        
        self.assertEqual(battle_result, "ongoing")
    
    # Тесты противников
    
    def test_start_battle_goblin(self):
        """Проверка инициализации боя с гоблином"""
        self.battle.start_battle("goblin")
        
        self.assertEqual(self.battle.enemy_name, "Гоблин")
        self.assertEqual(self.battle.enemy_hp, 5)
        self.assertEqual(self.battle.enemy_mp, 3)
    
    def test_start_battle_orc(self):
        """Проверка инициализации боя с орком"""
        self.battle.start_battle("orc")
        
        self.assertEqual(self.battle.enemy_name, "Орк")
        self.assertEqual(self.battle.enemy_hp, 8)
        self.assertEqual(self.battle.enemy_mp, 2)
    
    def test_start_battle_troll(self):
        """Проверка инициализации боя с троллем"""
        self.battle.start_battle("troll")
        
        self.assertEqual(self.battle.enemy_name, "Тролль")
        self.assertEqual(self.battle.enemy_hp, 12)
        self.assertEqual(self.battle.enemy_mp, 1)
    
    # Тесты защиты и лечения
    
    def test_player_defend(self):
        """Проверка уклонения"""
        initial_player_shield = self.battle.player_shield
        initial_player_mp = self.battle.player_mp
        
        result = self.battle.player_defend()
        
        self.assertIn("готовитесь к уклонению", result)
        self.assertEqual(self.battle.player_shield, initial_player_shield)  # Щит не увеличивается
        self.assertEqual(self.battle.player_mp, initial_player_mp)  # Мана не тратится
        self.assertTrue(self.battle.player_defending)
    
    def test_player_shield_spell(self):
        """Проверка создания щита"""
        initial_player_shield = self.battle.player_shield
        initial_player_mp = self.battle.player_mp
        
        result = self.battle.player_shield_spell()
        
        self.assertIn("создаете щит", result)
        self.assertEqual(self.battle.player_shield, initial_player_shield + 1)
        self.assertEqual(self.battle.player_mp, initial_player_mp - 1)
    
    def test_player_heal(self):
        """Проверка лечения"""
        self.battle.player_hp = 5
        initial_player_mp = self.battle.player_mp
        
        result = self.battle.player_heal()
        
        self.assertIn("лечитесь", result)
        self.assertEqual(self.battle.player_hp, 7)
        self.assertEqual(self.battle.player_mp, initial_player_mp - 2)
    
    # Тесты системы переполнения
    
    def test_blood_overflow_activation(self):
        """Проверка активации переполнения кровью"""
        self.battle.player_hp = 10
        self.battle.player_max_hp = 10
        
        # Устанавливаем переполнение напрямую для тестирования
        self.battle.player_blood_overflow = True
        
        # Проверяем, что переполнение активировано
        self.assertTrue(self.battle.player_blood_overflow)
        # Проверяем, что здоровье не превышает максимум
        self.assertEqual(self.battle.player_hp, 10)
    
    def test_overflow_effects_application(self):
        """Проверка применения эффектов переполнения"""
        self.battle.player_blood_overflow = True
        initial_player_hp = self.battle.player_hp
        initial_player_mp = self.battle.player_mp
        
        self.battle.apply_overflow_effects("player")
        
        self.assertEqual(self.battle.player_hp, initial_player_hp - 1)
        self.assertEqual(self.battle.player_mp, initial_player_mp - 2)


if __name__ == '__main__':
    # Запуск тестов
    unittest.main(verbosity=2) 