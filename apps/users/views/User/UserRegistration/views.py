from django.shortcuts import redirect, render
from apps.users.models import User

def user_registration_view(request):
    if request.method == 'GET':
        return render(request, 'users/registration.html')
    username = request.POST["username"]
    phone_number = request.POST["phone_number"]
    password = request.POST["password"]
    password2 = request.POST["password2"]
    
    user = User.objects.filter(username=username)
    if user:
        messages = {
            'error': "Bu username allaqachon ro'yxatdan o'tgan"
        }
        return render(request, "users/registration.html", messages)
    elif password != password2 :
        messages = {
            'error': "Parollar mos emas"
        }
        return render(request, "users/registration.html", messages)
    elif User.objects.filter(phone_number=phone_number).exists() :
        messages = {
            'error': "Bunday telefon raqamli foydalanuvchi tizimda mavjud."
        }  
        return render(request, 'users/registration.html', messages)
    else:
        user = User.objects.create(
            username = username,
            phone_number = phone_number,
        )
        user.set_password(password)
        user.save()
        return redirect('login')