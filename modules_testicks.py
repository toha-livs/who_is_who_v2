import json
import random


class InfoObject():
    rounde = 0
    __key = ['rounde', 'game', 'user', 'list_choice']

    def __init__(self, game_id, user_info):
        self.game = game_id
        self.user = user_info

    def __setattr__(self, key, value):
        if key in InfoObject.__key:
            self.__dict__[key] = value
        else:
            raise AttributeError


class SpivveryUser(InfoObject):
    def list_choice(self, user_sum):
        a = []
        while True:
            choice = random.randint(1, user_sum)
            if choice == self.user.id:
                pass
            elif choice in a:
                pass
            else:
                a.append(choice)
            if len(a) == 5:
                break
        self.var_list_choice = a
        self.var_list_choice_json = json.dumps(a)
        return json.dumps(a)

    def get_variation(self):
        roundeX = self.rounde - 1
        u_sex = UserInfo.objects.get(user_id=self.var_list_choice[roundeX])
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