from datetime import timezone, datetime


kuy = {'11': 'день', '12': 'дня', '13': 'дней', '21': 'час',
       '22': 'часа', '23': 'часов', '31': 'минута', '32': 'минуты',
       '33': 'минут', '41': 'секунда', '42': 'секунды', '43': 'секунд'}


def test_get_all_res(g):
    h = datetime.now(timezone.utc)
    timer = h - g
    day = timer.days
    hou = timer.seconds // 60 // 60
    min = timer.seconds // 60 % 60
    sec = timer.seconds % 60
    all = [dict(s='1', r=day), dict(s='2', r=hou), dict(s='3', r=min), dict(s='4', r=sec)]
    count = 0
    deletes = []
    for i in all:
        if i['r'] == 0:
            deletes.append(count)
        count += 1
    deletes.reverse()
    for dele in deletes:
        all.pop(dele)
    return get_str(all[0]['r'], all[0]['s'])


def get_str(a, info):
    x = str(a)
    if len(x) == 1:
        result = get_get(a, info)
    else:
        x_x = str(x[-2])
        if x_x == '1':
            r = '3'
            result = '{} {} назад'.format(a, kuy[info + r])
        else:
            result = get_get(a, info)
    return result


def get_get(a, info):
    if a == 1:
        r = '1'
        result = '{} {} назад'.format(a, kuy[info + r])
    elif a >= 5 or a == 0:
        r = '3'
        result = '{} {} назад'.format(a, kuy[info + r])
    else:
        r = '2'
        result = '{} {} назад'.format(a, kuy[info + r])
    return result
