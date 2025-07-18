# Документация Source of Fantasy

Добро пожаловать в документацию игры Source of Fantasy! Этот раздел содержит подробную информацию о всех системах игры, их взаимодействии и технической реализации.

## Структура документации

### 📋 Общие документы

- **[Обзор систем](systems_overview.md)** - Общий обзор всех игровых систем и их взаимодействия
- **[Руководство по архитектуре](architecture_guide.md)** - Подробное описание архитектуры игры
- **[Правила игры](game_rules.md)** - Официальные правила и механики игры

### ⚔️ Системы

- **[Боевая система](battle_system_specification.md)** - Техническое задание боевой системы
- **[Система инвентаря](inventory_system_specification.md)** - Техническое задание системы инвентаря

### 🎮 Сцены

- **[Боевые сцены](scenes/battle_scenes.md)** - Описание боевых сцен

### 📊 Данные

- **[Персонажи](data/characters.md)** - Описание персонажей и их характеристик
- **[Локации](data/locations.md)** - Описание игровых локаций
- **[Предметы](data/items.md)** - Описание всех предметов в игре

## Быстрый старт

### Для разработчиков

1. Изучите **[Руководство по архитектуре](architecture_guide.md)**
2. Ознакомьтесь с **[Обзором систем](systems_overview.md)**
3. Выберите интересующую систему и изучите её спецификацию
4. Изучите соответствующие сцены и данные

### Для игроков

1. Начните с **[Обзора систем](systems_overview.md)**
2. Изучите спецификации интересующих систем
3. Ознакомьтесь с описанием персонажей и локаций

## Основные концепции

### Модульная архитектура

Игра построена на модульной архитектуре, где каждая система работает независимо и взаимодействует с другими через четко определенные интерфейсы.

### Системы

- **Боевая система** - управляет сражениями и переполнением характеристик
- **Система инвентаря** - управляет предметами и экономикой

### Сцены

Сцены используют системы для создания игрового опыта. Они не содержат логики, а только представление и взаимодействие с игроком.

### Данные

Все игровые данные (персонажи, локации, предметы) хранятся в отдельных файлах для легкого редактирования и расширения.

## Техническая информация

### Язык

- **Основной язык**: Python (Ren'Py)
- **Формат данных**: JSON-подобные структуры в Python

### Структура файлов

```
game/
├── systems/           # Игровые системы
├── scenes/            # Игровые сцены
├── data/              # Игровые данные
├── utils/             # Утилиты и помощники
└── script.rpy         # Главный скрипт
```

### Расширение игры

Для добавления нового контента:

1. Добавьте данные в соответствующие файлы в `data/`
2. Создайте новые сцены в `scenes/` (если необходимо)
3. Обновите системы в `systems/` (если необходимо)
4. Обновите документацию

## Поддержка

### Сообщения об ошибках

При обнаружении ошибок в документации или игре:

1. Проверьте, не описана ли ошибка в документации
2. Создайте issue с подробным описанием проблемы
3. Укажите версию игры и шаги для воспроизведения

### Предложения

Для предложений по улучшению:

1. Изучите существующую документацию
2. Создайте issue с описанием предложения
3. Обоснуйте необходимость изменений

## Версии

### Текущая версия

- **Версия игры**: 1.0.0
- **Дата обновления**: 2024
- **Статус**: В разработке

### История изменений

- **v1.0.0** - Базовая версия с боевой системой и системой инвентаря
- **v0.9.0** - Альфа-версия с базовой функциональностью
- **v0.8.0** - Прототип с боевой системой

## Лицензия

Данная документация распространяется под лицензией MIT. См. файл LICENSE для подробностей.

---

**Примечание**: Эта документация постоянно обновляется. Следите за изменениями в репозитории.
