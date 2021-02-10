def code_str(some_str):
    """
    возвращает строку с транслитерацией
    например: 'кто-то_world 77'   'kto-to_world 77'
    """
    length = len(some_str)
    if length > 80:
        some_str = some_str[:81]
    return some_str.translate(str.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                                            "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"))
