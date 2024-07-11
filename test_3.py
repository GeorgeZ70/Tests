import pytest
def solve(phrases: list):
    result = [] # список палиндромов    
    for phrase in phrases: # пройдите циклом по всем фразам
        phrase_ = phrase.replace(' ','') # сохраните фразу без пробелов
        if phrase_ == phrase_[::-1]: # сравните фразу с ней же, развернутой наоборот (через [::-1])
           result.append(phrase)
    return result

@pytest.mark.parametrize(
    'l, expected',
    [(["нажал кабан на баклажан", "дом как комод", "рвал дед лавр"], ["нажал кабан на баклажан", "рвал дед лавр"]), (["азот калий и лактоза",
               "а собака боса", "тонет енот"], ["азот калий и лактоза",
               "а собака боса", "тонет енот"]), (["карман мрак", "пуст суп"], ["пуст суп"])]
)
def test_palindromes(l,expected):
    result = solve(l)
    assert result == expected