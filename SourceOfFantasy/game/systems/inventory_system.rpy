# Система инвентаря
init python:
    class InventorySystem:
        def __init__(self):
            # Инвентарь игрока
            self.inventory = {}
            self.max_inventory_size = 20
            
            # Экипировка
            self.equipment = {
                "weapon": None,
                "armor": None,
                "accessory": None
            }
            
            # Золото
            self.gold = 100
            
            # Словарь всех предметов в игре
            self.all_items = {
                # Оружие
                "rusty_sword": {
                    "name": "Ржавый меч",
                    "type": "weapon",
                    "rarity": "common",
                    "attack": 3,
                    "value": 50,
                    "description": "Старый, но все еще острый меч"
                },
                "iron_sword": {
                    "name": "Железный меч",
                    "type": "weapon",
                    "rarity": "uncommon",
                    "attack": 5,
                    "value": 150,
                    "description": "Надежный железный меч"
                },
                "magic_staff": {
                    "name": "Магический посох",
                    "type": "weapon",
                    "rarity": "rare",
                    "attack": 2,
                    "magic_attack": 8,
                    "value": 300,
                    "description": "Посох, усиливающий магию"
                },
                
                # Броня
                "leather_armor": {
                    "name": "Кожаная броня",
                    "type": "armor",
                    "rarity": "common",
                    "defense": 2,
                    "value": 80,
                    "description": "Легкая кожаная броня"
                },
                "iron_armor": {
                    "name": "Железная броня",
                    "type": "armor",
                    "rarity": "uncommon",
                    "defense": 4,
                    "value": 200,
                    "description": "Надежная железная броня"
                },
                
                # Аксессуары
                "charm_ring": {
                    "name": "Кольцо очарования",
                    "type": "accessory",
                    "rarity": "rare",
                    "charisma": 3,
                    "value": 250,
                    "description": "Кольцо, увеличивающее харизму"
                },
                "health_potion": {
                    "name": "Зелье здоровья",
                    "type": "consumable",
                    "rarity": "common",
                    "heal": 20,
                    "value": 30,
                    "description": "Восстанавливает здоровье"
                },
                "mana_potion": {
                    "name": "Зелье маны",
                    "type": "consumable",
                    "rarity": "common",
                    "mana": 15,
                    "value": 25,
                    "description": "Восстанавливает ману"
                },

            }
        
        def add_item(self, item_id, quantity=1):
            """Добавляет предмет в инвентарь"""
            if len(self.inventory) >= self.max_inventory_size and item_id not in self.inventory:
                return "Инвентарь полон!"
            
            if item_id in self.all_items:
                if item_id in self.inventory:
                    self.inventory[item_id]["quantity"] += quantity
                else:
                    self.inventory[item_id] = {
                        "quantity": quantity,
                        "item_data": self.all_items[item_id].copy()
                    }
                return f"Получен предмет: {self.all_items[item_id]['name']} x{quantity}"
            else:
                return "Неизвестный предмет!"
        
        def remove_item(self, item_id, quantity=1):
            """Удаляет предмет из инвентаря"""
            if item_id in self.inventory:
                if self.inventory[item_id]["quantity"] <= quantity:
                    del self.inventory[item_id]
                else:
                    self.inventory[item_id]["quantity"] -= quantity
                return f"Предмет удален: {self.all_items[item_id]['name']} x{quantity}"
            else:
                return "Предмет не найден в инвентаре!"
        
        def use_item(self, item_id):
            """Использует предмет"""
            if item_id not in self.inventory:
                result = "Предмет не найден в инвентаре!"
                renpy.notify(result)
                return result
            
            item_data = self.all_items[item_id]
            item_type = item_data["type"]
            
            if item_type == "consumable":
                # Используем расходник
                if item_id == "health_potion":
                    heal_amount = item_data["heal"]
                    actual_heal = battle_system.add_health("player", heal_amount)
                    self.remove_item(item_id, 1)
                    
                    if battle_system.player_blood_overflow:
                        result = f"Здоровье восстановлено на {actual_heal}! Переполнение кровью!"
                    else:
                        result = f"Здоровье восстановлено на {actual_heal}!"
                    renpy.notify(result)
                    return result
                
                elif item_id == "mana_potion":
                    mana_amount = item_data["mana"]
                    actual_mana = battle_system.add_mana("player", mana_amount)
                    self.remove_item(item_id, 1)
                    
                    if battle_system.player_mana_overflow:
                        result = f"Мана восстановлена на {actual_mana}! Переполнение маной!"
                    else:
                        result = f"Мана восстановлена на {actual_mana}!"
                    renpy.notify(result)
                    return result
                
                else:
                    self.remove_item(item_id, 1)
                    result = f"Использован предмет: {item_data['name']}"
                    renpy.notify(result)
                    return result

            
            elif item_type in ["weapon", "armor", "accessory"]:
                # Экипируем предмет
                return self.equip_item(item_id)
            
            result = "Этот предмет нельзя использовать!"
            renpy.notify(result)
            return result
        
        def equip_item(self, item_id):
            """Экипирует предмет"""
            if item_id not in self.inventory:
                result = "Предмет не найден в инвентаре!"
                renpy.notify(result)
                return result
            
            item_data = self.all_items[item_id]
            item_type = item_data["type"]
            
            if item_type in self.equipment:
                # Снимаем предыдущую экипировку
                if self.equipment[item_type]:
                    old_item = self.equipment[item_type]
                    self.add_item(old_item, 1)
                
                # Экипируем новый предмет
                self.equipment[item_type] = item_id
                self.remove_item(item_id, 1)
                result = f"Экипирован: {item_data['name']}"
                renpy.notify(result)
                return result
            
            result = "Этот предмет нельзя экипировать!"
            renpy.notify(result)
            return result
        
        def unequip_item(self, slot):
            """Снимает экипированный предмет"""
            if slot in self.equipment and self.equipment[slot]:
                item_id = self.equipment[slot]
                self.add_item(item_id, 1)
                self.equipment[slot] = None
                result = f"Снят: {self.all_items[item_id]['name']}"
                renpy.notify(result)
                return result
            else:
                result = "В этом слоте ничего не экипировано!"
                renpy.notify(result)
                return result
        
        def get_equipment_bonuses(self):
            """Возвращает бонусы от экипировки"""
            bonuses = {
                "attack": 0,
                "magic_attack": 0,
                "defense": 0,
                "charisma": 0
            }
            
            for slot, item_id in self.equipment.items():
                if item_id and item_id in self.all_items:
                    item_data = self.all_items[item_id]
                    for stat, value in item_data.items():
                        if stat in bonuses:
                            bonuses[stat] += value
            
            return bonuses
        
        def add_gold(self, amount):
            """Добавляет золото"""
            self.gold += amount
            return f"Получено золота: {amount}"
        
        def spend_gold(self, amount):
            """Тратит золото"""
            if self.gold >= amount:
                self.gold -= amount
                return f"Потрачено золота: {amount}"
            else:
                return "Недостаточно золота!"
        
        def get_inventory_list(self):
            """Возвращает список предметов в инвентаре"""
            items = []
            for item_id, item_info in self.inventory.items():
                item_data = item_info["item_data"]
                items.append({
                    "id": item_id,
                    "name": item_data["name"],
                    "quantity": item_info["quantity"],
                    "type": item_data["type"],
                    "rarity": item_data["rarity"],
                    "description": item_data["description"]
                })
            return items
        
        def get_equipment_list(self):
            """Возвращает список экипированных предметов"""
            equipment = {}
            for slot, item_id in self.equipment.items():
                if item_id:
                    equipment[slot] = {
                        "id": item_id,
                        "name": self.all_items[item_id]["name"],
                        "description": self.all_items[item_id]["description"]
                    }
                else:
                    equipment[slot] = None
            return equipment

init python:
    inventory_system = InventorySystem() 