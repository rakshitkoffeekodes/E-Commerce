from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
from .serilizers import *


# Create your views here.


@api_view(['POST'])
def register(request):
    first_name = request.POST['First Name']
    last_name = request.POST['Last Name']
    email = request.POST['Email']
    password = request.POST['Password']
    conform_password = request.POST['Conform Password']
    try:
        if password == conform_password:
            Register.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=make_password(password)
            )
            return JsonResponse({'Message': f'Register Success {first_name}'})
        else:
            return JsonResponse({'Message': 'Password Not Match.'})
    except Exception as e:
        return JsonResponse({'Message': e.__str__()})


@api_view(['POST'])
def login(request):
    email = request.POST['Email']
    password = request.POST['Password']

    try:
        seller_user = Register.objects.get(email=email)
        if check_password(password, seller_user.password):
            request.session['email'] = email
            return JsonResponse({'Message': f'{seller_user.first_name} Login Successfully.'})
        else:
            return JsonResponse({'Message': 'Password Not Match'})
    except Exception as e:
        return JsonResponse({'Message': e.__str__()})


@api_view(['GET'])
def logout(request):
    del request.session['email']
    return JsonResponse({'Message': 'Logout Successfully.'})


@api_view(['GET'])
def profile(request):
    try:
        seller_user = Register.objects.get(email=request.session['email'])
        path = request.META['HTTP_HOST']
        path1 = 'http://' + path + '/media/' + str(seller_user.profile_picture)
        seller_user.profile_picture = path1
        data = {
            'Profile Image': str(seller_user.profile_picture),
            'First Name': seller_user.first_name,
            'Last Name': seller_user.last_name,
            'Email': seller_user.email,
            'Mobile Number': seller_user.mobile_no,
            'Address': seller_user.address
        }
        return JsonResponse({'Profile': data})
    except Exception as e:
        return JsonResponse({'Message': e.__str__()})


@api_view(['POST'])
def update_profile(request):
    profile_picture = request.FILES.get('Profile Image', '')
    first_name = request.POST.get('First name', '')
    last_name = request.POST.get('Last name', '')
    email = request.POST.get('email', '')
    mobile_no = request.POST.get('Mobile Number', '')
    address = request.POST.get('Address', '')

    try:
        seller_user = Register.objects.get(email=request.session['email'])
        if not profile_picture == '':
            seller_user.profile_picture = profile_picture
        if not first_name == '':
            seller_user.first_name = first_name
        if not last_name == '':
            seller_user.last_name = last_name
        if not email == '':
            seller_user.email = email
        if not mobile_no == '':
            seller_user.mobile_no = mobile_no
        if not address == '':
            seller_user.address = address
        seller_user.save()
        return JsonResponse({'Message': 'Profile Update Successfully.'})

    except Exception as e:
        return JsonResponse({'Message': e.__str__()})
