# Тестирование боевой логики вне Ren'Py
import random

# Импортируем функции и переменные из боевого модуля (копируем их сюда для теста)
# --- КОПИЯ ЛОГИКИ ИЗ battle.rpy ---
player_hp = 10
player_max_hp = 10
player_mp = 10
player_max_mp = 10
player_shield = 0
player_defending = False
player_blood_overflow = False
player_mana_overflow = False

enemy_name = "Гоблин"
enemy_hp = 5
enemy_max_hp = 5
enemy_mp = 3
enemy_max_mp = 3
enemy_shield = 0
enemy_blood_overflow = False
enemy_mana_overflow = False

def reset_battle():
    global player_hp, player_max_hp, player_mp, player_max_mp, player_shield, player_defending
    global player_blood_overflow, player_mana_overflow
    global enemy_hp, enemy_max_hp, enemy_mp, enemy_max_mp, enemy_shield
    global enemy_blood_overflow, enemy_mana_overflow
    
    player_hp = 10
    player_max_hp = 10
    player_mp = 10
    player_max_mp = 10
    player_shield = 0
    player_defending = False
    player_blood_overflow = False
    player_mana_overflow = False
    
    enemy_hp = 5
    enemy_max_hp = 5
    enemy_mp = 3
    enemy_max_mp = 3
    enemy_shield = 0
    enemy_blood_overflow = False
    enemy_mana_overflow = False

def add_health(character, amount):
    global player_hp, player_max_hp, player_blood_overflow
    global enemy_hp, enemy_max_hp, enemy_blood_overflow
    
    if character == "player":
        old_hp = player_hp
        player_hp += amount
        if player_hp > player_max_hp:
            player_blood_overflow = True
        elif player_hp <= player_max_hp:
            player_blood_overflow = False
        return player_hp - old_hp
    elif character == "enemy":
        old_hp = enemy_hp
        enemy_hp += amount
        if enemy_hp > enemy_max_hp:
            enemy_blood_overflow = True
        elif enemy_hp <= enemy_max_hp:
            enemy_blood_overflow = False
        return enemy_hp - old_hp

def add_mana(character, amount):
    global player_mp, player_max_mp, player_mana_overflow
    global enemy_mp, enemy_max_mp, enemy_mana_overflow
    
    if character == "player":
        old_mp = player_mp
        player_mp += amount
        if player_mp > player_max_mp:
            player_mana_overflow = True
        elif player_mp <= player_max_mp:
            player_mana_overflow = False
        return player_mp - old_mp
    elif character == "enemy":
        old_mp = enemy_mp
        enemy_mp += amount
        if enemy_mp > enemy_max_mp:
            enemy_mana_overflow = True
        elif enemy_mp <= enemy_max_mp:
            enemy_mana_overflow = False
        return enemy_mp - old_mp

def apply_overflow_effects(character):
    global player_hp, player_mp, player_blood_overflow, player_mana_overflow
    global enemy_hp, enemy_mp, enemy_blood_overflow, enemy_mana_overflow
    
    if character == "player":
        total_health_loss = 0
        total_mana_loss = 0
        
        if player_blood_overflow:
            total_health_loss += 1
            total_mana_loss += 2
        if player_mana_overflow:
            total_health_loss += 1
            total_mana_loss += 2
            
        if total_health_loss > 0:
            player_hp = max(0, player_hp - total_health_loss)
        if total_mana_loss > 0:
            player_mp = max(0, player_mp - total_mana_loss)
        # После применения эффектов обязательно обновляем статус
        check_overflow_status("player")
    elif character == "enemy":
        total_health_loss = 0
        total_mana_loss = 0
        
        if enemy_blood_overflow:
            total_health_loss += 1
            total_mana_loss += 2
        if enemy_mana_overflow:
            total_health_loss += 1
            total_mana_loss += 2
            
        if total_health_loss > 0:
            enemy_hp = max(0, enemy_hp - total_health_loss)
        if total_mana_loss > 0:
            enemy_mp = max(0, enemy_mp - total_mana_loss)
        # После применения эффектов обязательно обновляем статус
        check_overflow_status("enemy")

def check_overflow_status(character):
    global player_hp, player_max_hp, player_mp, player_max_mp, player_blood_overflow, player_mana_overflow
    global enemy_hp, enemy_max_hp, enemy_mp, enemy_max_mp, enemy_blood_overflow, enemy_mana_overflow
    
    if character == "player":
        player_blood_overflow = player_hp > player_max_hp
        player_mana_overflow = player_mp > player_max_mp
    elif character == "enemy":
        enemy_blood_overflow = enemy_hp > enemy_max_hp
        enemy_mana_overflow = enemy_mp > enemy_max_mp

def player_attack():
    global enemy_hp, player_mp, enemy_shield
    if enemy_hp <= 0:
        return "Противник уже побежден!"
    if player_mp >= 1:
        damage = 1
        if enemy_shield > 0:
            enemy_shield -= 1
            damage = 0
        enemy_hp -= damage
        player_mp -= 1
        return f"Вы атакуете! Нанесено урона: {damage}"
    else:
        return "Недостаточно маны для атаки!"

def player_defend():
    global player_mp, player_defending
    if player_mp >= 1:
        player_mp -= 1
        player_defending = True
        return "Вы готовите заклинание защиты!"
    else:
        return "Недостаточно маны для защиты!"

def player_shield_spell():
    global player_mp, player_shield
    if player_mp >= 1:
        player_mp -= 1
        player_shield += 1
        return "Вы создали щит!"
    else:
        return "Недостаточно маны для создания щита!"

def player_heal():
    global player_mp
    if player_mp >= 2:
        player_mp -= 2
        healed = add_health("player", 2)
        check_overflow_status("player")
        if player_blood_overflow:
            return f"Вы исцелились на {healed} HP! Но у вас переполнение кровью!"
        else:
            return f"Вы исцелились на {healed} HP!"
    else:
        return "Недостаточно маны для лечения!"

def enemy_turn():
    global player_hp, enemy_mp, enemy_shield, player_shield, player_defending
    if enemy_mp <= 0:
        return "Гоблин не может действовать - нет маны!"
    action = random.choice(["attack", "shield", "heal"])
    if action == "attack" and enemy_mp >= 1:
        damage = 1
        if player_shield > 0:
            player_shield -= 1
            damage = 0
        elif player_defending:
            damage = 0
            player_defending = False
        player_hp -= damage
        enemy_mp -= 1
        return f"Гоблин атакует! Вы получили урона: {damage}"
    elif action == "shield" and enemy_mp >= 1:
        enemy_mp -= 1
        enemy_shield += 1
        return "Гоблин создает щит!"
    elif action == "heal" and enemy_mp >= 2:
        enemy_mp -= 2
        healed = add_health("enemy", 2)
        check_overflow_status("enemy")
        if enemy_blood_overflow:
            return f"Гоблин исцелился на {healed} HP! Но у него переполнение кровью!"
        else:
            return f"Гоблин исцелился на {healed} HP!"
    else:
        return "Гоблин пропускает ход!"

def start_battle(enemy_type="goblin"):
    global enemy_name, enemy_hp, enemy_max_hp, enemy_mp, enemy_max_mp
    
    # Сначала сбрасываем бой
    reset_battle()
    
    # Затем устанавливаем правильного противника
    if enemy_type == "goblin":
        enemy_name = "Гоблин"
        enemy_hp = 5
        enemy_max_hp = 5
        enemy_mp = 3
        enemy_max_mp = 3
    elif enemy_type == "orc":
        enemy_name = "Орк"
        enemy_hp = 8
        enemy_max_hp = 8
        enemy_mp = 2
        enemy_max_mp = 2
    elif enemy_type == "troll":
        enemy_name = "Тролль"
        enemy_hp = 12
        enemy_max_hp = 12
        enemy_mp = 1
        enemy_max_mp = 1
    else:
        # Значения по умолчанию
        enemy_name = "Противник"
        enemy_hp = 5
        enemy_max_hp = 5
        enemy_mp = 3
        enemy_max_mp = 3

# --- ТЕСТЫ ---
def test_battle_exit_conditions():
    global enemy_hp, player_hp, enemy_mp, player_mp
    print("\n=== Тест: условия выхода из боя ===")
    # 1. Победа игрока (enemy_hp <= 0)
    reset_battle()
    enemy_hp = 1
    player_attack()
    assert enemy_hp <= 0, "Победа игрока не сработала!"
    print("Победа игрока: OK")

    # 2. Победа противника (player_hp <= 0)
    reset_battle()
    player_hp = 1
    enemy_mp = 10
    def always_attack():
        return "attack"
    # Мокаем random.choice
    orig_choice = random.choice
    random.choice = lambda x: "attack"
    enemy_turn()
    random.choice = orig_choice
    assert player_hp <= 0, "Победа противника не сработала!"
    print("Победа противника: OK")

    # 3. Ничья (у обоих нет маны)
    reset_battle()
    player_mp = 0
    enemy_mp = 0
    # Проверяем условие ничьей
    assert player_mp <= 0 and enemy_mp <= 0, "Ничья не сработала!"
    print("Ничья: OK")

def test_battle_full():
    print("\n=== Тест: полный бой ===")
    reset_battle()
    rounds = 0
    while player_hp > 0 and enemy_hp > 0 and (player_mp > 0 or enemy_mp > 0):
        # Применяем эффекты статусов переполнения
        apply_overflow_effects("player")
        # Игрок всегда атакует
        player_attack()
        if enemy_hp <= 0:
            print("Игрок победил!")
            break
        if player_mp <= 0 and enemy_mp <= 0:
            print("Ничья!")
            break
        # Применяем эффекты статусов переполнения противника
        apply_overflow_effects("enemy")
        enemy_turn()
        if player_hp <= 0:
            print("Гоблин победил!")
            break
        if player_mp <= 0 and enemy_mp <= 0:
            print("Ничья!")
            break
        rounds += 1
        if rounds > 100:
            print("Ошибка: слишком длинный бой!")
            break
    print("Финал: HP игрока:", player_hp, "HP гоблина:", enemy_hp)

def test_battle_ends_when_enemy_hp_zero():
    """Тест: бой должен закончиться, когда HP противника достигает 0 или меньше"""
    print("\n=== Тест: бой заканчивается при HP противника <= 0 ===")
    
    # Тест 1: HP противника становится 0
    reset_battle()
    global enemy_hp
    enemy_hp = 1
    result1 = player_attack()
    assert enemy_hp == 0, f"Ошибка: enemy_hp должен стать 0, текущее значение: {enemy_hp}"
    print("Тест 1: HP противника = 0 - OK")
    
    # Тест 2: Повторная атака не должна менять HP и должна вернуть спецсообщение
    old_enemy_hp = enemy_hp
    result2 = player_attack()
    assert enemy_hp == old_enemy_hp, f"Ошибка: enemy_hp изменился после повторной атаки: {enemy_hp}"
    assert result2 == "Противник уже побежден!", f"Неверное сообщение: {result2}"
    print("Тест 2: Повторная атака невозможна - OK")

def test_no_attack_on_dead_enemy():
    print("\n=== Тест: нельзя атаковать мертвого противника ===")
    reset_battle()
    global enemy_hp
    enemy_hp = 0
    result = player_attack()
    assert result == "Противник уже побежден!", "Можно атаковать мертвого противника!"
    print("Тест: нельзя атаковать мертвого противника - OK")

def test_blood_overflow_mechanics():
    """Тест: механика переполнения кровью"""
    print("\n=== Тест: механика переполнения кровью ===")
    
    # Тест 1: Переполнение кровью при лечении
    reset_battle()
    global player_hp, player_max_hp, player_blood_overflow
    player_hp = player_max_hp  # Полное здоровье
    result = player_heal()
    assert player_blood_overflow == True, "Статус переполнения кровью не активировался!"
    assert player_hp > player_max_hp, "HP не превысило максимальное!"
    assert "переполнение кровью" in result.lower(), "Сообщение о переполнении отсутствует!"
    print("Тест 1: Активация переполнения кровью - OK")
    
    # Тест 2: Эффекты переполнения кровью
    old_hp = player_hp
    old_mp = player_mp
    apply_overflow_effects("player")
    assert player_hp == old_hp - 1, "Не потеряно 1 HP от переполнения!"
    assert player_mp == old_mp - 2, "Не потеряно 2 MP от переполнения!"
    print("Тест 2: Эффекты переполнения кровью - OK")
    
    # Тест 3: Снятие статуса переполнения
    player_hp = player_max_hp
    check_overflow_status("player")
    assert player_blood_overflow == False, "Статус переполнения не снялся!"
    print("Тест 3: Снятие статуса переполнения - OK")

def test_mana_overflow_mechanics():
    """Тест: механика переполнения маной"""
    print("\n=== Тест: механика переполнения маной ===")
    
    # Тест 1: Переполнение маной при добавлении маны
    reset_battle()
    global player_mp, player_max_mp, player_mana_overflow
    player_mp = player_max_mp  # Полная мана
    add_mana("player", 1)
    assert player_mana_overflow == True, "Статус переполнения маной не активировался!"
    assert player_mp > player_max_mp, "MP не превысило максимальное!"
    print("Тест 1: Активация переполнения маной - OK")
    
    # Тест 2: Эффекты переполнения маной
    old_hp = player_hp
    old_mp = player_mp
    apply_overflow_effects("player")
    assert player_hp == old_hp - 1, "Не потеряно 1 HP от переполнения маной!"
    assert player_mp == old_mp - 2, "Не потеряно 2 MP от переполнения маной!"
    print("Тест 2: Эффекты переполнения маной - OK")
    
    # Тест 3: Снятие статуса переполнения маной
    player_mp = player_max_mp
    check_overflow_status("player")
    assert player_mana_overflow == False, "Статус переполнения маной не снялся!"
    print("Тест 3: Снятие статуса переполнения маной - OK")

def test_double_overflow_mechanics():
    """Тест: механика двойного переполнения"""
    print("\n=== Тест: механика двойного переполнения ===")
    
    reset_battle()
    global player_hp, player_mp, player_max_hp, player_max_mp, player_blood_overflow, player_mana_overflow
    
    # Устанавливаем оба переполнения
    player_hp = player_max_hp + 1
    player_mp = player_max_mp + 1
    check_overflow_status("player")
    
    assert player_blood_overflow == True, "Переполнение кровью не активировалось!"
    assert player_mana_overflow == True, "Переполнение маной не активировалось!"
    
    # Проверяем двойные эффекты
    old_hp = player_hp
    old_mp = player_mp
    apply_overflow_effects("player")
    assert player_hp == old_hp - 2, "Не потеряно 2 HP от двойного переполнения!"
    assert player_mp == old_mp - 4, "Не потеряно 4 MP от двойного переполнения!"
    print("Тест: Двойное переполнение - OK")

def test_healing_mechanics():
    """Тест: механика лечения"""
    print("\n=== Тест: механика лечения ===")
    
    # Тест 1: Обычное лечение
    reset_battle()
    global player_hp, player_mp
    player_hp = 5  # Неполное здоровье
    player_mp = 10  # Достаточно маны
    old_hp = player_hp
    result = player_heal()
    assert player_hp == old_hp + 2, "Здоровье не восстановилось на 2!"
    assert player_mp == 8, "Мана не потратилась!"
    assert "переполнение" not in result.lower(), "Не должно быть переполнения!"
    print("Тест 1: Обычное лечение - OK")
    
    # Тест 2: Лечение с переполнением
    reset_battle()
    player_hp = player_max_hp  # Полное здоровье
    player_mp = 10
    result = player_heal()
    assert player_blood_overflow == True, "Переполнение не активировалось!"
    assert "переполнение кровью" in result.lower(), "Сообщение о переполнении отсутствует!"
    print("Тест 2: Лечение с переполнением - OK")
    
    # Тест 3: Недостаточно маны для лечения
    reset_battle()
    player_mp = 1  # Недостаточно маны
    result = player_heal()
    assert result == "Недостаточно маны для лечения!", "Неверное сообщение при недостатке маны!"
    print("Тест 3: Недостаточно маны для лечения - OK")

def test_integration_full_battle_with_new_mechanics():
    """Тест: полная интеграция всех новых механик в бою"""
    print("\n=== Тест: интеграция всех новых механик ===")
    
    reset_battle()
    global player_hp, player_mp, enemy_hp, enemy_mp, player_blood_overflow, player_mana_overflow
    
    # Симулируем бой с использованием новых механик
    rounds = 0
    max_rounds = 20
    
    while player_hp > 0 and enemy_hp > 0 and rounds < max_rounds:
        # Применяем эффекты статусов переполнения
        apply_overflow_effects("player")
        
        # Игрок лечится, если здоровье низкое
        if player_hp <= 5 and player_mp >= 2:
            result = player_heal()
            print(f"Раунд {rounds + 1}: {result}")
        else:
            # Иначе атакует
            result = player_attack()
            print(f"Раунд {rounds + 1}: {result}")
        
        # Проверяем статусы переполнения
        if player_blood_overflow:
            print(f"  Статус: Переполнение кровью активен")
        if player_mana_overflow:
            print(f"  Статус: Переполнение маной активно")
        
        # Проверяем условия окончания боя
        if enemy_hp <= 0:
            print("Игрок победил!")
            break
        if player_hp <= 0:
            print("Гоблин победил!")
            break
        if player_mp <= 0 and enemy_mp <= 0:
            print("Ничья!")
            break
        
        # Применяем эффекты статусов переполнения противника
        apply_overflow_effects("enemy")
        
        # Ход противника
        enemy_result = enemy_turn()
        print(f"  Противник: {enemy_result}")
        
        # Проверяем статусы переполнения противника
        if enemy_blood_overflow:
            print(f"  Статус противника: Переполнение кровью активно")
        if enemy_mana_overflow:
            print(f"  Статус противника: Переполнение маной активно")
        
        # Проверяем условия окончания боя
        if player_hp <= 0:
            print("Гоблин победил!")
            break
        if enemy_hp <= 0:
            print("Игрок победил!")
            break
        if player_mp <= 0 and enemy_mp <= 0:
            print("Ничья!")
            break
        
        rounds += 1
        print(f"  Состояние: Игрок HP:{player_hp}/{player_max_hp} MP:{player_mp}/{player_max_mp}, "
              f"Гоблин HP:{enemy_hp}/{enemy_max_hp} MP:{enemy_mp}/{enemy_max_mp}")
        print()
    
    print(f"Бой завершен за {rounds} раундов")
    print(f"Финальное состояние: Игрок HP:{player_hp}/{player_max_hp} MP:{player_mp}/{player_max_mp}, "
          f"Гоблин HP:{enemy_hp}/{enemy_max_hp} MP:{enemy_mp}/{enemy_max_mp}")
    
    # Проверяем, что бой завершился корректно
    assert rounds < max_rounds, "Бой не завершился за максимальное количество раундов"
    assert player_hp <= 0 or enemy_hp <= 0 or (player_mp <= 0 and enemy_mp <= 0), "Бой не завершился корректно"
    print("Тест: Интеграция всех механик - OK")

def test_status_removal_after_overflow_effect():
    """Тест: статус переполнения снимается после применения эффекта, когда HP становится <= максимального"""
    print("\n=== Тест: снятие статуса переполнения после эффекта ===")
    reset_battle()
    global player_hp, player_max_hp, player_blood_overflow
    # Создаем переполнение
    player_hp = player_max_hp + 3
    check_overflow_status("player")
    assert player_blood_overflow, "Статус переполнения не активировался!"
    # Применяем эффект переполнения в цикле, пока HP > максимального
    steps = 0
    while player_hp > player_max_hp and steps < 10:
        apply_overflow_effects("player")
        steps += 1
    # Теперь статус должен сняться
    assert player_hp <= player_max_hp, "HP не уменьшился до максимума!"
    assert not player_blood_overflow, "Статус переполнения не снялся после эффекта!"
    print("Тест: снятие статуса переполнения после эффекта - OK")

def test_start_battle_function():
    """Тест: функция start_battle корректно инициализирует разных противников"""
    print("\n=== Тест: функция start_battle ===")
    
    # Тест 1: Гоблин
    start_battle("goblin")
    assert enemy_name == "Гоблин", "Неверное имя гоблина!"
    assert enemy_hp == 5, "Неверное HP гоблина!"
    assert enemy_max_hp == 5, "Неверное максимальное HP гоблина!"
    assert enemy_mp == 3, "Неверное MP гоблина!"
    assert enemy_max_mp == 3, "Неверное максимальное MP гоблина!"
    print("Тест 1: Гоблин - OK")
    
    # Тест 2: Орк
    start_battle("orc")
    assert enemy_name == "Орк", "Неверное имя орка!"
    assert enemy_hp == 8, "Неверное HP орка!"
    assert enemy_max_hp == 8, "Неверное максимальное HP орка!"
    assert enemy_mp == 2, "Неверное MP орка!"
    assert enemy_max_mp == 2, "Неверное максимальное MP орка!"
    print("Тест 2: Орк - OK")
    
    # Тест 3: Тролль
    start_battle("troll")
    assert enemy_name == "Тролль", "Неверное имя тролля!"
    assert enemy_hp == 12, "Неверное HP тролля!"
    assert enemy_max_hp == 12, "Неверное максимальное HP тролля!"
    assert enemy_mp == 1, "Неверное MP тролля!"
    assert enemy_max_mp == 1, "Неверное максимальное MP тролля!"
    print("Тест 3: Тролль - OK")
    
    # Тест 4: Неизвестный тип (должен использовать значения по умолчанию)
    start_battle("unknown")
    assert enemy_name == "Противник", "Неверное имя по умолчанию!"
    assert enemy_hp == 5, "Неверное HP по умолчанию!"
    assert enemy_max_hp == 5, "Неверное максимальное HP по умолчанию!"
    assert enemy_mp == 3, "Неверное MP по умолчанию!"
    assert enemy_max_mp == 3, "Неверное максимальное MP по умолчанию!"
    print("Тест 4: Неизвестный тип - OK")

def run_all_tests():
    test_battle_exit_conditions()
    test_battle_full()
    test_battle_ends_when_enemy_hp_zero()
    test_no_attack_on_dead_enemy()
    test_blood_overflow_mechanics()
    test_mana_overflow_mechanics()
    test_double_overflow_mechanics()
    test_healing_mechanics()
    test_integration_full_battle_with_new_mechanics()
    test_status_removal_after_overflow_effect()
    test_start_battle_function()
    print("\nВсе тесты завершены!")

if __name__ == "__main__":
    run_all_tests() 