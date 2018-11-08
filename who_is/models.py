import uuid
from django.db import models
from django.db.models import TextField, ForeignKey, CharField
from django.contrib.auth.models import User
from . import informa


class Gymnastics(models.Model):
    name = TextField(null=True)
    source_img = TextField(null=True)

    def __str__(self):
        return '<Gymnastics name={} source_img={} >'.format(self.name, self.source_img)


class UserInfo(models.Model):
    SEX_CHOICES = ((informa.MALE, 'M'), (informa.FEMALE, 'F'))
    POSITION_CHOICES = (
        (informa.OPERATOR, 'OP'), (informa.SUPERVISOR, 'SV'),
        (informa.RULSGROUP, 'RG'), (informa.OTHER, 'OT'), (informa.QUALITY, 'QC'))
    name = TextField(null=True)
    avatar = TextField(null=True)
    position = CharField(max_length=15, choices=POSITION_CHOICES, default=informa.OPERATOR)
    sex = CharField(max_length=1, choices=SEX_CHOICES)
    user_id = ForeignKey(User, on_delete=models.CASCADE, related_name='user_info')
    best_score = models.IntegerField(null=True)

    def __str__(self):
        return '<Gymnastics name={} avatar={} user_id={} sex={}>'.format(self.name, self.avatar, self.user_id, self.sex)


class Game(models.Model):
    id = models.UUIDField(primary_key=True)
    time = models.TimeField(null=True)
    date = models.DateTimeField(null=False)
    result = models.IntegerField(null=True)
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='game', null=True)

    def __str__(self):
        return '<Gymnastics time={} date={} result={}>'.format(self.time, self.date, self.result)


class GameRound(models.Model):
    result = models.IntegerField(null=True)
    game = ForeignKey(Game,  on_delete=models.CASCADE, related_name='game_round', null=True)
