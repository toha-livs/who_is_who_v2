# -*- coding: utf-8 -*-


import uuid
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import UserInfo, Game, GameRound
from django.views.decorators.csrf import csrf_exempt
from .my_modules import GameProperty, get_last_u_res, get_r_list, GetAllResult
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
    result = get_last_u_res(request.user.id)
    result_all = GetAllResult()
    result_all.get_all()
    result_all = result_all.result_l
    game_id = uuid.uuid4()
    context = {'game_id': game_id, 'user_info': user_info, 'results': result, 'result_all': result_all}
    return render(request, 'home.html', context)


def logout_to(request):
    logout(request)
    return redirect('log_in')


@login_required
def game(request, game_id):
        user_info = UserInfo.objects.get(user_id=request.user.id)
        list_u_choice = get_r_list(request.user.id, User.objects.count())
        context = {}
        context['list_ch_usr'] = list_u_choice
        context['user_in_sys'] = user_info
        context['names0'] = [{'Test': 'True'}, {'Test': 'Truе'}, {'Test': 'Tru5'}]
        return render(request, 'game.html', context)


@csrf_exempt
def test_ajax(request):
    gamer = GameProperty(request)
    gamer.update_rounde()
    print(gamer.rounde)
    if gamer.rounde == 0:
        print(gamer.rounde)
        gamer.reg_game()
        gamer.reg_game_round()
        print(gamer.list_u_choice)
        gamer.update_rounde()
        response = gamer.get_variation()
        return JsonResponse(response)
    else:
        gamer.reg_game_round()
        gamer.update_rounde()
        if str(gamer.rounde) in '12345':
            gamer.update_rounde()
            response = gamer.get_variation()
            return JsonResponse(response)
        elif gamer.rounde == 6:
            print(gamer.rounde)
            response = gamer.finish_game()
            return JsonResponse(response)
    return None


def get_test(request):
    user = UserInfo.objects.filter(id__in=['1', '3', '7']).all()
    print("привет лох")
    context = {'user': user}
    print(user)
    return render(request, 'testt.html', context)


@login_required
def game_stat(request):
    game_result = Game.objects.filter(user=request.user).latest('date')
    return render(request, 'game_stat.html', {'result': game_result})

