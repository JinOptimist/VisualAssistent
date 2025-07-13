#!/usr/bin/env python3
"""
Простой скрипт для запуска игры SourceOfFantasy
"""

import os
import sys
import subprocess

def main():
    print("Запуск игры SourceOfFantasy...")
    
    # Проверяем, что мы в правильной директории
    if not os.path.exists("game"):
        print("Ошибка: директория 'game' не найдена!")
        print("Убедитесь, что вы запускаете скрипт из корневой директории проекта.")
        return 1
    
    # Проверяем наличие основных файлов
    required_files = ["game/script.rpy", "game/options.rpy"]
    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"Ошибка: файл {file_path} не найден!")
            return 1
    
    print("Файлы игры найдены.")
    print("Для запуска игры вам нужно установить Ren'Py SDK.")
    print("Скачайте его с официального сайта: https://www.renpy.org/latest.html")
    print("После установки запустите игру через Ren'Py Launcher.")
    
    # Показываем содержимое основного скрипта
    print("\n=== Содержимое основного скрипта игры ===")
    try:
        with open("game/script.rpy", "r", encoding="utf-8") as f:
            content = f.read()
            # Показываем только начало файла
            lines = content.split('\n')[:20]
            for line in lines:
                print(line)
        print("...")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 