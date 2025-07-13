# Экраны для создания персонажа

# Экран выбора особенностей
screen traits_selection():
    modal True
    
    frame:
        style_prefix "traits"
        xfill True
        yfill True
        
        # Кнопка "Следующий этап" в правом верхнем углу
        textbutton "Следующий этап" action Return("next_stage") style "traits_next_button" xalign 1.0 yalign 0.0 xoffset -20 yoffset 20
        
        vbox:
            spacing 20
            
            # Заголовок
            text "Выбор особенностей персонажа" style "traits_title"
            
            # Информация об очках развития
            frame:
                style_prefix "traits_info"
                xfill True
                
                hbox:
                    spacing 20
                    
                    text "Очки развития: [traits_system.get_development_points()]"
                    text "Выбрано особенностей: [len(traits_system.selected_traits)]"
            
            # Список особенностей
            frame:
                style_prefix "traits_list"
                xfill True
                yfill True
                
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    
                    vbox:
                        spacing 10
                        
                        # Защита от ошибок: проверяем структуру trait_data
                        for trait_id, trait_data in traits_system.get_all_traits().items():
                            frame:
                                style_prefix "trait_item"
                                xfill True
                                
                                hbox:
                                    spacing 15
                                    
                                    # Кнопка выбора/отмены
                                    if trait_id in traits_system.selected_traits:
                                        textbutton "✓" action [Function(traits_system.deselect_trait, trait_id), Play("sound", "audio/sfx/click.ogg")]
                                    else:
                                        textbutton "○" action [Function(traits_system.select_trait, trait_id), Play("sound", "audio/sfx/click.ogg")]
                                    
                                    # Информация об особенности
                                    vbox:
                                        spacing 5
                                        
                                        text trait_data["name"] style "trait_name"
                                        text (trait_data["description"] if "description" in trait_data else "Нет описания") style "trait_description"
                                    
                                    # Стоимость
                                    frame:
                                        style_prefix "trait_cost"
                                        if "cost" in trait_data and trait_data["cost"] > 0:
                                            text "+[trait_data['cost']]" color "#00FF00"
                                        else:
                                            text "[trait_data['cost']]" color "#FF0000"
            
            # Кнопки управления (только Сбросить и Отмена)
            frame:
                style_prefix "traits_buttons"
                xfill True
                
                hbox:
                    spacing 20
                    
                    textbutton "Сбросить" action Function(traits_system.reset_selection)
                    textbutton "Отмена" action Return("cancel")

# Экран предварительного просмотра выбранных особенностей
screen traits_preview():
    modal True
    
    frame:
        style_prefix "traits_preview"
        xfill True
        yfill True
        
        vbox:
            spacing 20
            
            text "Выбранные особенности" style "traits_preview_title"
            
            frame:
                style_prefix "traits_preview_list"
                xfill True
                yfill True
                
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    
                    vbox:
                        spacing 10
                        
                        for trait in traits_system.get_selected_traits():
                            frame:
                                style_prefix "trait_preview_item"
                                xfill True
                                
                                vbox:
                                    spacing 5
                                    
                                    text trait["name"] style "trait_preview_name"
                                    text (trait["description"] if "description" in trait else "Нет описания") style "trait_preview_description"
                                    text "Стоимость: [trait['cost']]" style "trait_preview_cost"
            
            frame:
                style_prefix "traits_preview_buttons"
                xfill True
                
                hbox:
                    spacing 20
                    
                    textbutton "Назад" action Return("back")
                    textbutton "Подтвердить" action Return("confirm")

# Стили для экранов создания персонажа
style traits_title:
    size 32
    color "#FFFFFF"
    align (0.5, 0.0)
    outlines [(2, "#000000", 0, 0)]

style traits_info_text:
    size 18
    color "#FFFFFF"
    outlines [(1, "#000000", 0, 0)]

style trait_name:
    size 20
    color "#FFFFFF"
    bold True
    outlines [(1, "#000000", 0, 0)]

style trait_description:
    size 16
    color "#CCCCCC"
    outlines [(1, "#000000", 0, 0)]

style trait_cost_text:
    size 18
    bold True
    outlines [(1, "#000000", 0, 0)]

style traits_preview_title:
    size 28
    color "#FFFFFF"
    align (0.5, 0.0)
    outlines [(2, "#000000", 0, 0)]

style trait_preview_name:
    size 18
    color "#FFFFFF"
    bold True
    outlines [(1, "#000000", 0, 0)]

style trait_preview_description:
    size 14
    color "#CCCCCC"
    outlines [(1, "#000000", 0, 0)]

style trait_preview_cost:
    size 14
    color "#FFFF00"
    outlines [(1, "#000000", 0, 0)]

# Стили для фреймов
style traits_frame:
    background "#2A2A2A"
    padding (20, 20)
    margin (20, 20)

style traits_info_frame:
    background "#3A3A3A"
    padding (15, 10)
    margin (0, 10)

style traits_list_frame:
    background "#2A2A2A"
    padding (15, 15)
    margin (0, 10)

style trait_item_frame:
    background "#3A3A3A"
    padding (10, 10)
    margin (0, 5)

style trait_cost_frame:
    background "#4A4A4A"
    padding (5, 5)
    margin (0, 0)

style traits_buttons_frame:
    background "#2A2A2A"
    padding (15, 10)
    margin (0, 10)

style traits_next_button:
    background "#4A4A4A"
    hover_background "#5A5A5A"
    padding (20, 10)
    margin (5, 5)

style traits_next_button_text:
    size 16
    color "#FFFFFF"
    hover_color "#FFFF00"
    bold True
    outlines [(1, "#000000", 0, 0)]

style traits_preview_frame:
    background "#2A2A2A"
    padding (20, 20)
    margin (20, 20)

style traits_preview_list_frame:
    background "#3A3A3A"
    padding (15, 15)
    margin (0, 10)

style trait_preview_item_frame:
    background "#4A4A4A"
    padding (10, 10)
    margin (0, 5)

style traits_preview_buttons_frame:
    background "#2A2A2A"
    padding (15, 10)
    margin (0, 10)

# Стили для кнопок
style traits_button:
    background "#4A4A4A"
    hover_background "#5A5A5A"
    padding (20, 10)
    margin (5, 5)

style traits_button_text:
    size 16
    color "#FFFFFF"
    hover_color "#FFFF00"
    outlines [(1, "#000000", 0, 0)] 