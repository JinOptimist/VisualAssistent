# Шаблоны промптов для SourceOfFantasy

## Быстрые команды

### Тестирование

```bash
# Запуск всех тестов
python tests/test_battle_renpy.py

# Запуск через bat файл
run_tests.bat
```

### Обновление документации

```bash
# После изменения логики обновите соответствующий файл:
# Боевая система
documentation/battle_system_specification.md

# Соблазнение
documentation/seduction_system_specification.md

# Инвентарь
documentation/inventory_system_specification.md

# Прогрессия
documentation/progression_system_specification.md

# Архитектура
documentation/architecture_guide.md

# Общий обзор систем
documentation/systems_overview.md
```

## Шаблоны промптов

### Добавление нового действия

```
Добавь новое действие [название] в боевую систему:
- Стоимость: X маны
- Эффект: [описание]
- Обнови battle.rpy, script.rpy, screens.rpy, тесты и документацию
```

### Исправление бага

```
Исправь баг в [описание проблемы]:
- Опиши проблему
- Предложи решение
- Обнови тесты для проверки исправления
```

### Оптимизация

```
Оптимизируй [компонент]:
- Анализируй производительность
- Предлагай улучшения
- Сохраняй функциональность
- Обновляй тесты
```

### Добавление нового противника

```
Добавь нового противника [название]:
- HP: X/Y, MP: X/Y
- Обнови start_battle() в battle.rpy
- Добавь label в script.rpy
- Напиши тесты
- Обнови documentation/battle_system_specification.md
```

## Пошаговые инструкции

### Добавление нового статуса

1. Добавьте переменную статуса в `battle.rpy`
2. Создайте функцию активации/снятия
3. Обновите `apply_overflow_effects()`
4. Добавьте отображение в `screens.rpy`
5. Напишите тесты в `tests/test_battle_renpy.py`

### Изменение боевой логики

1. Обновите `battle.rpy`
2. Обновите тесты
3. Проверьте интерфейс в `screens.rpy`
4. Обновите `documentation/battle_system_specification.md`
5. Запустите все тесты

### Добавление новой механики

1. Добавьте переменные в соответствующий файл системы
2. Создайте функции для механики
3. Добавьте обработчики в соответствующий файл
4. Обновите интерфейс в `screens.rpy`
5. Напишите тесты
6. Обновите соответствующую документацию:
   - Боевая система → `documentation/battle_system_specification.md`
   - Соблазнение → `documentation/seduction_system_specification.md`
   - Инвентарь → `documentation/inventory_system_specification.md`
   - Прогрессия → `documentation/progression_system_specification.md`

## Контекстные подсказки

### Ren'Py код

- `init python:` для инициализации
- `$` для однострочных Python выражений
- `python:` для многострочных блоков
- Группируйте label'ы логически

### Python код

- `global` для изменения глобальных переменных
- `snake_case` для переменных и функций
- Комментарии на русском языке
- Следуйте PEP 8 где возможно

### Тесты

- `assert` для проверок
- Группируйте тесты по функциональности
- Тестируйте граничные случаи
- Копируйте логику из `battle.rpy` для изоляции

## Частые задачи

### Проверка работоспособности

```python
# В тестах проверяйте:
- Нулевые значения
- Максимальные значения
- Переполнение
- Взаимодействие механик
```

### Обновление интерфейса

```renpy
# В screens.rpy добавьте:
- Новые кнопки действий
- Отображение новых статусов
- Обновление информации о персонаже
```

### Документирование изменений

```markdown
# В соответствующем файле документации:

- Описывайте новые переменные
- Документируйте функции
- Включайте примеры использования
- Обновляйте архитектурные схемы

# Выбор файла документации:

- Боевая система → documentation/battle_system_specification.md
- Соблазнение → documentation/seduction_system_specification.md
- Инвентарь → documentation/inventory_system_specification.md
- Прогрессия → documentation/progression_system_specification.md
- Архитектура → documentation/architecture_guide.md
- Общий обзор → documentation/systems_overview.md
```
