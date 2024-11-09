from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserRegister
from .models import *
from django.http import HttpResponse

# Create your views here.
class Game_shop(TemplateView):
    template_name = 'main_page.html'


class Shop_basket(TemplateView):
    template_name = 'basket.html'


def menu_def(request):
    mydict = Game.objects.all()
    context = {
        'mydict': mydict,
    }
    return render(request, 'shop.html', context)


def sign_up_by_html(request):
    mydict = Game.objects.all()
    info = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in mydict:
            info['error'] = 'Пользователь уже существует'
        else:
            return HttpResponse(f'Приветствуем, {username}!')

        print(f"Имя: {username}")
        print(f"Пароль: {password}")
        print(f"Повтор пароля: {repeat_password}")
        print(f"Возраст: {age}")


    return render(request, 'registration_compl.html', info)


def sign_up_by_django(request):
    users = Buyer.objects.all()
    usernames = [i.name for i in users]
    i = 0
    info = {'error': []}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in usernames and password == repeat_password and int(age) >= 18:
                Buyer.objects.create(name=username, balance=0, age=age)
                context = {'username': username}
                return render(request, 'registration_compl.html', context)
            elif username in usernames:
                i += 1
                info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
                print(info[f'error {i}'])
                return HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
            elif password != repeat_password:
                i += 1
                info[f'error {i}'] = HttpResponse('Пользователь уже существует', status=400, reason='repeated login')
                print(info[f'error {i}'])
                return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            elif int(age) < 18:
                i += 1
                info[f'error {i}'] = HttpResponse(
                    f'Вы должны быть старше 18', status=400, reason='insufficient age')

                return HttpResponse(
                    f'Вы должны быть старше 18', status=400, reason='insufficient age')
    else:

        form = UserRegister()
        context = {'info': info, 'form': form}
        return render(request, 'registration_page.html', context)



def main_page_def(request):
    return render(request, 'main_page.html')



