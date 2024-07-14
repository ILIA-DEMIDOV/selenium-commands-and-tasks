# Использование Assert для проверки , и если совпадает  = то вывести текст

def test_input_text(expected_result, actual_result):
    assert (expected_result == actual_result) , f'expected {expected_result}, got {actual_result}'
    # проверить что одно число ранво равно другому

def test_substring(full_string, substring):
    assert (substring in full_string), f"expected '{substring}' to be substring of '{full_string}'"
    # проверить что часть текста входит в строку
