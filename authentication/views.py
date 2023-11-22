import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login successful!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account deactivated."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, check your password or email."
        }, status=401)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout Successful!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout Failed."
        }, status=401)
    
@csrf_exempt
def register(request):
    if request.method == "POST":
        input = json.loads(request.body)
        # print(input)
        username = input['username']
        password = input['password']
        password_confirmation = input['confirmPassword']

        if password != password_confirmation:
            return JsonResponse({
                "status": "Failed",
                "message": "Password does not match."
            }, status=401)
        
        user = User.objects.create_user(username = username, password = password)
        user.save()
        
        return JsonResponse({
            "status": "Successful",
            "message": "Regristration successful!"
        }, status=200)

    return JsonResponse({
        "status": "Failed",
        "message": "Regristration failed."
    }, status=401)