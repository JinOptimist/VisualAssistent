# Раздел создания персонажа
# Создание персонажа

label c0_c02_create:
    $ traits_system.reset_selection()
    scene black
    
    "Добро пожаловать в создание персонажа!"
    "Здесь вы сможете выбрать особенности, которые определят вашего героя."
    "У вас есть 10 очков развития для выбора особенностей."
    
    "Как работает система очков:"
    "- Положительные особенности стоят очки (например, 'Силач' = 2 очка)"
    "- Отрицательные особенности дают дополнительные очки (например, 'Дохляк' = +2 очка)"
    "- Вы можете выбрать любое количество особенностей в рамках доступных очков"
    
    "Совет: Выбор отрицательных особенностей позволит вам получить больше очков для выбора положительных особенностей!"
    jump c0_c02_create_trait

label c0_c02_create_trait:   
    # Отладочная информация
    $ renpy.notify("Система особенностей загружена. Доступно особенностей: " + str(len(traits_system.get_all_traits())))
    
    # Показываем экран выбора особенностей
    call screen traits_selection
    
    # Обрабатываем результат
    if _return == "next_stage":
        # Проверяем, что выбор подтвержден
        $ success, message = traits_system.confirm_selection()
        if success:
            "Отлично! Ваши особенности выбраны."
            jump c0_c03_character_ready
            
            # # Показываем предварительный просмотр
            # call screen traits_preview
            
            # if _return == "confirm":
            #     "Персонаж создан! Переходим к игре..."
            #     jump c0_c03_character_ready
            # else:
            #     # Возвращаемся к выбору особенностей
            #     jump c0_c02_create_trait
        else:
            $ renpy.notify(message)
            jump c0_c02_create_trait
    elif _return == "cancel":
        "Создание персонажа отменено."
        return
    else:
        # Неожиданный результат - возвращаемся к выбору
        jump c0_c02_create_trait

# Метка для готового персонажа
label c0_c03_character_ready:
    "Ваш персонаж готов к приключениям!"
    
    "Выбранные особенности:"
    $ _traits = traits_system.get_selected_traits()
    if len(_traits) == 0:
        "Особенности не выбраны."
    else:
        $ _i = 1
        while _i <= len(_traits):
            $ _trait = _traits[_i-1]
            "[str(_i)]. [ _trait['name'] ]: [ _trait['description'] ]"
            $ _i += 1
    
    "Очки развития потрачено: [traits_system.get_total_trait_cost()]"
    
    $ positive_traits = [t for t in traits_system.get_selected_traits() if t['cost'] > 0]
    $ negative_traits = [t for t in traits_system.get_selected_traits() if t['cost'] < 0]
    if len(positive_traits) > len(negative_traits):
        "Вы выбрали больше положительных особенностей. Ваш персонаж будет сильным, но с некоторыми недостатками."
    elif len(negative_traits) > len(positive_traits):
        "Вы выбрали больше отрицательных особенностей. Ваш персонаж будет иметь слабости, но может компенсировать их мощными положительными особенностями."
    else:
        "Вы выбрали сбалансированный набор особенностей."
    
    "Теперь вы можете начать свое приключение!"
    # Здесь можно добавить переход к следующей сцене
    # jump next_scene 

    