import datetime
from . import my_mod_res
import random
from django.contrib.auth.models import User
from who_is.models import UserInfo, GameRound, Game
import json


def get_r_list(user_id, user_count):
    a = []
    while True:
        choice = random.randint(1, user_count)
        if choice == user_id:
            pass
        elif choice in a:
            pass
        else:
            a.append(choice)
        if len(a) == 5:
            break
    return json.dumps(a)


def get_variation(list_u_choice, rounde, game_id):
    roundeX = rounde - 1
    u_sex = UserInfo.objects.get(user_id=list_u_choice[roundeX])
    a = [list_u_choice[roundeX]]
    l_f_s = UserInfo.objects.filter(sex=u_sex.sex).values('user_id')
    list_of_users = []
    for i in l_f_s:
        list_of_users.append(i['user_id'])
    while True:
        var = random.choice(list_of_users)
        if var in a:
            pass
        else:
            a.append(var)
        if len(a) == 3:
            break
    context = {}
    name1 = User.objects.get(id=a[1])
    name2 = User.objects.get(id=a[2])
    image = UserInfo.objects.get(user_id=a[0])
    user_imag = 'user_img{}'.format(rounde)
    names = 'names{}'.format(rounde)
    rounde = GameRound.objects.filter(game=game_id).count()
    context['rounde'] = rounde
    context[user_imag] = {'avatar': image.avatar, 'position': image.position}
    user_test = User.objects.get(id=a[0])
    context[names] = [{'Test': 'True', 'Name': user_test.first_name + ' ' + user_test.last_name},
                      {'Test': 'Truе', 'Name': name1.first_name + ' ' + name1.last_name},
                      {'Test': 'Tru5', 'Name': name2.first_name + ' ' + name2.last_name}
                      ]
    random.shuffle(context[names], random.random)
    return context


def reg_game(game_id, user):
    game = Game(id=game_id, date=datetime.datetime.now(), user=user)
    game.save()


def reg_game_round(last_latter, game_id):
    if last_latter == 'e':
        result = 1
    else:
        result = 0
    game_round = GameRound(result=result, game_id=game_id)
    game_round.save()


def eng_str(g):
    g = str(g)
    g = g.replace('[', '')
    g = g.replace(']', '')
    g = g.replace(' ', '')
    return g


def dec_str(g):
    g = g.split(',')
    print(g)
    h = []
    for i in g:
        h.append(int(i))
    g = h
    return g


def get_last_u_res(user_id):
    results_l = []
    results = Game.objects.filter(user=user_id).order_by('-date')[:4]
    for res in results:
        results_l.append(dict(date=str(res.date)[:19], result=res.result))
    return results_l


def get_all_res():
    results_l = []
    results = Game.objects.all().order_by('-date')[:5]
    for res in results:
        user_id = UserInfo.objects.get(user_id=res.user)
        results_l.append(dict(time=str(my_mod_res.test_get_all_res(res.date)),
                              result=res.result,
                              name=str(res.user.first_name) + ' ' + str(res.user.last_name),
                              position=user_id.position))
    return results_l







