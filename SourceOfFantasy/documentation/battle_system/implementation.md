# Боевая система - Детали реализации

## Архитектура

### Файловая структура

- **`game/systems/battle_system.rpy`** - Вся логика боя
- **`game/script.rpy`** - Сценарии игры (только вызовы `start_battle()`)
- **`game/screens.rpy`** - Интерфейс боя
- **`tests/test_battle_renpy.py`** - Тесты

### Принципы

- Вся боевая логика в `battle_system.rpy`
- Сценарии только вызывают бой с указанием противника
- Интерфейс отображает состояние из `battle_system.rpy`

## Переменные

### Структура переменных персонажа

Каждый персонаж (игрок и противник) имеет:

- **hp/max_hp**: Текущее/максимальное здоровье
- **mp/max_mp**: Текущая/максимальная мана
- **shield**: Количество щитов (изначально 0)
- **defending**: Флаг уклонения (изначально False)
- **blood_overflow**: Флаг переполнения кровью (изначально False)
- **mana_overflow**: Флаг переполнения маной (изначально False)
- **stream_attack_is_active**: Флаг "Атака Потоком" (изначально False)
- **stream_attack_turns**: Счетчик ходов "Атаки Потоком" (изначально 0)

### Переменные игрока

- **player_hp**: 10 (изначально)
- **player_max_hp**: 10 (изначально)
- **player_mp**: 10 (изначально)
- **player_max_mp**: 10 (изначально)
- **player_shield**: 0 (изначально)
- **player_defending**: False (флаг уклонения, изначально)
- **player_blood_overflow**: False (изначально)
- **player_mana_overflow**: False (изначально)
- **player_stream_attack_is_active**: False (изначально)
- **player_stream_attack_turns**: 0 (изначально)

### Переменные противника

- **enemy_name**: Имя противника
- **enemy_hp/enemy_max_hp**: Здоровье противника
- **enemy_mp/enemy_max_mp**: Мана противника
- **enemy_shield**: 0 (изначально)
- **enemy_blood_overflow**: False (изначально)
- **enemy_mana_overflow**: False (изначально)
- **enemy_stream_attack_is_active**: False (изначально)
- **enemy_stream_attack_turns**: 0 (изначально)

## Механики

### Атака Снарядом

```python
def player_projectile_attack():
    # Требует 1 MP, урон 1
    # Щит противника блокирует урон
```

**Условия**: MP ≥ 1, противник жив, не под "Атакой Потоком"

### Атака Потоком

```python
def player_stream_attack():
    # Требует 2 MP, активирует статус на 3 хода
```

**Условия**: MP ≥ 2, противник жив, не под "Атакой Потоком"

### Уклонение

```python
def player_defend():
    # Бесплатно, только устанавливает флаг уклонения
    self.player_defending = True
```

**Условия**: Противник жив, не под "Атакой Потоком"
**Эффект**: Блокирует следующую атаку противника, не создает щит

### Статус "Атака Потоком"

- **Длительность**: 3 хода
- **Эффект**: Автоматический урон 1 за ход
- **Ограничения**: Нельзя выполнять другие действия
- **Интерфейс**:
  - Показывается кнопка "Продолжить атаку потоком"
  - Можно кликнуть в любое место экрана для продолжения
- **Снятие**: Автоматически после 3 ходов

### Атака противника

```python
def enemy_turn():
    # Случайный выбор: атака снарядом/потоком, щит, лечение
```

**Приоритет**: "Атака Потоком" 30%, остальные по 23.3% (если достаточно маны)

### Система переполнения

- **Переполнение кровью**: HP > max_HP → потеря 1 HP и 2 MP за ход
- **Переполнение маной**: MP > max_MP → потеря 1 HP и 2 MP за ход
- **Суммирование**: При обоих статусах - потеря 2 HP и 4 MP за ход
- **Снятие**: Автоматически при нормализации значений

## Функции

### Управление боем

- **start_battle(enemy_type)** — инициализация боя
- **reset_battle()** — сброс переменных
- **is_battle_over()** — проверка окончания
- **get_battle_result()** — результат боя

### Действия игрока

- **player_projectile_attack()** — атака снарядом
- **player_stream_attack()** — атака потоком
- **player_defend()** — уклонение
- **player_shield_spell()** — создание щита
- **player_heal()** — лечение

### Действия противника

- **enemy_turn()** — ход противника

### Управление статусами

- **apply_overflow_effects(character)** — эффекты переполнения
- **check_overflow_status(character)** — проверка переполнения
- **add_mana(character, amount)** — добавление маны
- **add_health(character, amount)** — добавление здоровья
- **apply_stream_attack_effect(character)** — эффект "Атака Потоком"
- **check_stream_attack_status(character)** — проверка "Атака Потоком"

## Правила именования

### Статус "Атака Потоком"

**ВАЖНО**: Избегать конфликтов имен:

- **player_stream_attack_is_active** - флаг статуса (bool)
- **enemy_stream_attack_is_active** - флаг статуса (bool)
- **player_stream_attack_turns** - счетчик ходов (int)
- **enemy_stream_attack_turns** - счетчик ходов (int)
- **player_stream_attack()** - метод активации
- **enemy_stream_attack()** - метод активации

**НЕ ИСПОЛЬЗОВАТЬ**:

- `player_stream_attack` как атрибут
- `enemy_stream_attack` как атрибут

**ИСПРАВЛЕНО**: В экранах и сценариях теперь используется правильное имя переменной `player_stream_attack_is_active` вместо `player_stream_attack`.

## Противники

### Гоблин (goblin)

```python
{
    "name": "Гоблин",
    "hp": 5, "max_hp": 5,
    "mp": 3, "max_mp": 3
}
```

### Орк (orc)

```python
{
    "name": "Орк",
    "hp": 8, "max_hp": 8,
    "mp": 2, "max_mp": 2
}
```

### Тролль (troll)

```python
{
    "name": "Тролль",
    "hp": 12, "max_hp": 12,
    "mp": 1, "max_mp": 1
}
```

## Обработчики (Ren'Py)

- Отдельный label для каждого действия игрока
- Проверка окончания боя после каждого действия
- Применение эффектов статусов в начале хода
- Блокировка действий под "Атакой Потоком"

## Использование в сценариях

```renpy
label battle_scene:
    python:
        start_battle("goblin")
    scene bg BG
    "Вы попадаете на поле боя!"
    "Перед вами появляется [enemy_name]!"
    jump battle_loop
```

## API

### Основные методы

```python
start_battle(enemy_type)     # Начать бой
reset_battle()               # Сбросить бой
is_battle_over()             # Проверить окончание
get_battle_result()          # Получить результат
```

### Действия игрока

```python
player_projectile_attack()   # Атака снарядом
player_stream_attack()       # Атака потоком
player_defend()              # Защита
player_shield_spell()        # Создание щита
player_heal()                # Лечение
```

### Обработчики действий (Ren'Py)

```renpy
player_action_projectile_attack    # Обработчик атаки снарядом
player_action_stream_attack        # Обработчик атаки потоком
player_action_continue_stream      # Обработчик продолжения атаки потоком
player_action_defend               # Обработчик защиты
player_action_shield               # Обработчик создания щита
player_action_heal                 # Обработчик лечения
player_action_escape               # Обработчик побега
player_action_use_item             # Обработчик использования предмета
```

### Управление статусами

```python
apply_overflow_effects(character)     # Эффекты переполнения
check_overflow_status(character)      # Проверка переполнения
apply_stream_attack_effect(character) # Эффект "Атака Потоком"
check_stream_attack_status(character) # Проверка "Атака Потоком"
```

### Доступ к данным

```python
battle_system.player_hp                    # HP игрока
battle_system.player_stream_attack_is_active # Статус "Атака Потоком"
battle_system.player_stream_attack_turns   # Оставшиеся ходы
battle_system.enemy_name                   # Имя противника
battle_system.enemy_stream_attack_is_active # Статус противника
battle_system.enemy_stream_attack_turns    # Ходы противника
battle_system.enemies                      # Словарь противников
```
