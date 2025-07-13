# Правила использования Python в проекте

## Вызов Python в Windows

### ✅ Правильно
Используйте команду `py` для вызова Python в Windows:

```bash
py --version
py -m pip install package_name
py script.py
py -c "print('Hello World')"
```

### ❌ Неправильно
Не используйте команду `python` в Windows:

```bash
python --version  # Неправильно
python -m pip install package_name  # Неправильно
python script.py  # Неправильно
```

## Настройка Cursor

### Настройка Python Interpreter в Cursor

В Cursor необходимо настроить правильный Python interpreter:

1. **Откройте Command Palette** (`Ctrl+Shift+P`)
2. **Выберите** "Python: Select Interpreter"
3. **Выберите** интерпретатор, который использует `py` команду

### Альтернативный способ настройки

Создайте файл `.vscode/settings.json` в корне проекта:

```json
{
    "python.pythonPath": "py",
    "python.defaultInterpreterPath": "py",
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}"
    }
}
```

### Проверка настройки

В терминале Cursor выполните:
```bash
py --version
```

Если команда работает, значит настройка правильная.

## Обоснование

- `py` - это Python Launcher для Windows, который автоматически выбирает правильную версию Python
- `py` работает более надежно в Windows среде
- `py` поддерживает виртуальные окружения лучше
- `py` является рекомендуемым способом запуска Python в Windows

## Примеры использования

### Установка пакетов
```bash
py -m pip install -r requirements.txt
```

### Запуск скриптов
```bash
py test_battle.py
py test_battle_renpy.py
```

### Создание виртуального окружения
```bash
py -m venv venv
```

### Активация виртуального окружения
```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows Command Prompt
.\venv\Scripts\activate.bat
```

## Исключения

В некоторых случаях может потребоваться использовать полный путь к Python:
```bash
C:\Python39\python.exe script.py
```

Но в большинстве случаев `py` является предпочтительным выбором. 