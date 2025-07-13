# Локации и их описания

init python:
    # Словарь всех локаций в игре
    locations = {
        "town_square": {
            "name": "Городская площадь",
            "description": "Центральная площадь города, где собираются торговцы и путешественники.",
            "available_actions": ["trade", "quest"],
            "connected_locations": ["market", "tavern"]
        },
        "market": {
            "name": "Рынок",
            "description": "Шумный рынок, где можно купить и продать различные товары.",
            "available_actions": ["trade"],
            "connected_locations": ["town_square", "merchant_shop"]
        },
        "tavern": {
            "name": "Таверна",
            "description": "Уютная таверна, где можно отдохнуть и услышать последние новости.",
            "available_actions": ["rest", "quest"],
            "connected_locations": ["town_square", "inn"]
        },

        "forest": {
            "name": "Темный лес",
            "description": "Таинственный лес, полный опасностей и сокровищ.",
            "available_actions": ["battle", "quest"],
            "connected_locations": ["town_square", "cave"]
        },
        "cave": {
            "name": "Пещера",
            "description": "Мрачная пещера, где обитают опасные существа.",
            "available_actions": ["battle"],
            "connected_locations": ["forest"]
        },
        "castle": {
            "name": "Замок",
            "description": "Величественный замок, резиденция местной знати.",
            "available_actions": ["quest"],
            "connected_locations": ["town_square"]
        },
        "merchant_shop": {
            "name": "Лавка торговца",
            "description": "Небольшая лавка с различными товарами.",
            "available_actions": ["trade"],
            "connected_locations": ["market"]
        },
        "inn": {
            "name": "Гостиница",
            "description": "Уютная гостиница для путешественников.",
            "available_actions": ["rest", "quest"],
            "connected_locations": ["tavern"]
        },
        "arena": {
            "name": "Арена",
            "description": "Место для боевых состязаний.",
            "available_actions": ["battle"],
            "connected_locations": ["town_square"]
        }
    }
    
    # Текущая локация игрока
    current_location = "town_square"
    
    def get_location_info(location_id):
        """Возвращает информацию о локации"""
        if location_id in locations:
            return locations[location_id]
        return None
    
    def get_available_actions(location_id):
        """Возвращает доступные действия в локации"""
        if location_id in locations:
            return locations[location_id]["available_actions"]
        return []
    
    def get_connected_locations(location_id):
        """Возвращает связанные локации"""
        if location_id in locations:
            return locations[location_id]["connected_locations"]
        return []
    
    def change_location(new_location):
        """Изменяет текущую локацию игрока"""
        global current_location
        if new_location in locations:
            current_location = new_location
            return True
        return False 