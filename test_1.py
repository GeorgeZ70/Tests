import pytest
def solve(todo_list: list, workday: float = 8):
    worktime = 0.0
    for el in todo_list: 
        worktime += el[1]
    return workday - worktime


    
    
@pytest.mark.parametrize(
    'l, expected',
    [([
        ["Разобрать почту", 1],
        ["Обзвонить клиентов", 2],
        ["Запланировать дела на завтра", 0.6],
        ["Сделать презентацию", 3],
        ["Созвон с командой", 0.5]], 0.9),
      ([
        ["Разобрать почту", 0.5],
        ["Обзвонить клиентов", 2],
        ["Запланировать дела на завтра", 0.5],
        ["Сделать презентацию", 3]], 2.0),
      ([
        ["Разобрать почту", 1],
        ["Обзвонить клиентов", 2],
        ["Запланировать дела на завтра", 0.4],
        ["Сделать презентацию", 2],
        ["Созвон с командой", 1]], 1.6)
    ]
)
def test_solve(l, expected):
    result = solve(l,8)
    result = round(result, 1)
    assert result == expected