# -*- coding: utf-8 -*-


import uuid
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import UserInfo, Game, GameRound
from django.views.decorators.csrf import csrf_exempt
from . import my_modules
from django.contrib.auth.decorators import login_required


def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'GET':
            return render(request, 'log_in.html')
        elif request.method == 'POST':
            name = request.POST.get('Login')
            password = request.POST.get('Password')
            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context = {'error': 'неправельный логин или пароль'}
                return render(request, 'log_in.html', context)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'GET':
            return render(request, 'sign_up.html')
        elif request.method == 'POST':
            name = request.POST.get('Name')
            login = request.POST.get('Login')
            password = request.POST.get('Password')
            user = User.objects.create_user(username=login, first_name=name, email='privet-ja-email', password=password)
            user.save()
            return redirect('home')


@login_required
def home(request):
    user_info = UserInfo.objects.get(user_id=request.user.id)
    result = my_modules.get_last_u_res(request.user.id)
    result_all = my_modules.get_all_res()
    game_id = uuid.uuid4()
    context = {'game_id': game_id, 'user_info': user_info, 'results': result, 'result_all': result_all}
    return render(request, 'home.html', context)


def logout_to(request):
    logout(request)
    return redirect('log_in')


@login_required
def game(request, game_id):
        user_info = UserInfo.objects.get(user_id=request.user.id)
        list_u_choice = my_modules.get_r_list(request.user.id, User.objects.count())
        context = {}
        context['list_ch_usr'] = list_u_choice
        context['user_in_sys'] = user_info
        context['names0'] = [{'Test': 'True'}, {'Test': 'Truе'}, {'Test': 'Tru5'}]
        return render(request, 'game.html', context)


@csrf_exempt
def test_ajax(request):
    list_u_choice = request.POST.get('list_ch_usr')
    list_u_choice = json.loads(list_u_choice)
    last_latter = request.POST.get('last_letter')
    game_id = request.POST.get('game_id')
    rounde = GameRound.objects.filter(game=game_id).count()
    print(rounde)
    if rounde == 0:
        print(rounde)
        my_modules.reg_game(game_id, request.user)
        my_modules.reg_game_round(last_latter, game_id)
        print(list_u_choice)
        rounde = GameRound.objects.filter(game=game_id).count()
        ver_dict = my_modules.get_variation(list_u_choice, rounde, game_id)
        rounde = GameRound.objects.filter(game=game_id).count()
        print(rounde)
        infa = {}
        infa.update(ver_dict)  # на выходе список
        json.dumps(infa)
        return JsonResponse(infa)
    else:
        my_modules.reg_game_round(last_latter, game_id)
        rounde = GameRound.objects.filter(game=game_id).count()
        if str(rounde) in '12345':
            print(rounde)
            print(list_u_choice)
            rounde = GameRound.objects.filter(game=game_id).count()
            ver_dict = my_modules.get_variation(list_u_choice, rounde, game_id)
            rounde = GameRound.objects.filter(game=game_id).count()
            print(rounde)
            infa = {}
            infa.update(ver_dict)  # на выходе список
            return JsonResponse(infa)
        elif rounde == 6:
            print(rounde)
            result_sum = GameRound.objects.filter(game=game_id, result=1).count()
            confirm_result = Game.objects.get(id=game_id)
            confirm_result.result = result_sum
            confirm_result.save()
            infa = {'rounde': rounde}
            return JsonResponse(infa)
    return None


def get_test(request):
    user = UserInfo.objects.filter(name__in=['Анна']).all()
    print("привет лох")
    context = {'user': user}
    print(user)
    return render(request, 'testt.html', context)


@login_required
def game_stat(request):
    game_result = Game.objects.filter(user=request.user).latest('date')
    return render(request, 'game_stat.html', {'result': game_result})

