# -*- coding: utf-8 -*-


import datetime
import random
from django.contrib.auth.models import User
from who_is.models import UserInfo, GameRound, Game
import json
from datetime import timezone, datetime


class GameProperty():
    def __init__(self, request):
        self.list_u_choice = json.loads(request.POST.get('list_ch_usr'))
        self.last_latter = request.POST.get('last_letter')
        self.game_id = request.POST.get('game_id')
        self.user = request.user

    def update_rounde(self):
        self.rounde = GameRound.objects.filter(game=self.game_id).count()

    def reg_game(self):
        game = Game(id=self.game_id, date=datetime.datetime.now(), user=self.user)
        game.save()

    def reg_game_round(self):
        if self.last_latter == 'e':
            result = 1
        else:
            result = 0
        game_round = GameRound(result=result, game_id=self.game_id)
        game_round.save()

    def get_variation(self):    #(list_u_choice, rounde, game_id):
        roundeX = self.rounde - 1
        u_sex = UserInfo.objects.get(user_id=self.list_u_choice[roundeX])
        a = [self.list_u_choice[roundeX]]
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
        user_imag = 'user_img{}'.format(self.rounde)
        names = 'names{}'.format(self.rounde)
        rounde = GameRound.objects.filter(game=self.game_id).count()
        context['rounde'] = rounde
        context[user_imag] = {'avatar': image.avatar, 'position': image.position}
        user_test = User.objects.get(id=a[0])
        context[names] = [{'Test': 'True', 'Name': user_test.first_name + ' ' + user_test.last_name},
                          {'Test': 'Truе', 'Name': name1.first_name + ' ' + name1.last_name},
                          {'Test': 'Tru5', 'Name': name2.first_name + ' ' + name2.last_name}
                          ]
        random.shuffle(context[names], random.random)
        return context

    def finish_game(self):
        result_sum = GameRound.objects.filter(game=self.game_id, result=1).count()
        confirm_result = Game.objects.get(id=self.game_id)
        confirm_result.result = result_sum
        confirm_result.save()
        infa = {'rounde': self.rounde}
        return infa


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


class GetAllResult():
    def __init__(self):
        self.result_l = []
        self.results = Game.objects.all().order_by('-date')[:5]
        self.kuy = {'11': 'день', '12': 'дня', '13': 'дней', '21': 'час',
                    '22': 'часа', '23': 'часов', '31': 'минута', '32': 'минуты',
                    '33': 'минут', '41': 'секунда', '42': 'секунды', '43': 'секунд'}

    def get_all(self):
        for res in self.results:
            user_id = UserInfo.objects.get(user_id=res.user)
            self.result_l.append(dict(time=str(self.test_get_all_res(res.date)),
                                  result=res.result,
                                  name=str(res.user.first_name) + ' ' + str(res.user.last_name),
                                  position=user_id.position))

    def test_get_all_res(self, g):
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
        return self.get_str(all[0]['r'], all[0]['s'])

    def get_str(self, a, info):
        x = str(a)
        if len(x) == 1:
            result = self.get_get(a, info)
        else:
            x_x = str(x[-2])
            if x_x == '1':
                r = '3'
                result = '{} {} назад'.format(a, self.kuy[info + r])
            else:
                result = self.get_get(a, info)
        return result

    def get_get(self, a, info):
        if a == 1:
            r = '1'
            result = '{} {} назад'.format(a, self.kuy[info + r])
        elif a >= 5 or a == 0:
            r = '3'
            result = '{} {} назад'.format(a, self.kuy[info + r])
        else:
            r = '2'
            result = '{} {} назад'.format(a, self.kuy[info + r])
        return result