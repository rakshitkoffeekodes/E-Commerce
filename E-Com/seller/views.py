import os

from django.conf import settings
from django.core.files.storage import default_storage
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


@api_view(['POST'])
def add_product(request):
    product_category = request.POST['Product Category']
    product_items = request.POST['Product Item']
    product_images = request.FILES.getlist('Product Images')
    SKU = request.POST['SKU ID']
    product_name = request.POST['Product Name']
    product_price = request.POST['Product Price']
    product_sale_price = request.POST['Product Sale Price']
    product_quantity = request.POST['Product Quantity']
    product_branding = request.POST['Product Brand']
    product_tags = request.POST['Product Tags']
    product_size = request.POST['Product Size']
    product_color = request.POST['Product Color']
    product_fabric = request.POST['Product Fabric']
    product_description = request.POST['Product Description']

    try:
        seller_user = Register.objects.get(email=request.session['email'])
        product_add = Product()
        product_add.product_category = product_category.upper()
        product_add.product_items = product_items.upper()
        product_add.product_images = [
            default_storage.save(os.path.join(settings.MEDIA_ROOT, 'document', image.name.replace(' ', '_')), image)
            for image in product_images]
        print(product_add.product_images)
        product_add.SKU = SKU
        product_add.product_name = product_name
        product_add.product_price = product_price
        product_add.product_sale_price = product_sale_price
        product_add.product_quantity = product_quantity
        product_add.product_branding = product_branding
        product_add.product_tags = product_tags
        product_add.product_size = product_size
        product_add.product_color = product_color
        product_add.product_fabric = product_fabric
        product_add.product_description = product_description
        product_add.product_seller = seller_user
        product_add.save()
        return JsonResponse({'message': 'Product Add Successfully.'})

    except Exception as e:
        return JsonResponse({'Message': e.__str__()})


@api_view(['GET'])
def view_all_product(request):
    try:
        seller_user = Register.objects.get(email=request.session['email'])
        all_product = Product.objects.filter(product_seller=seller_user)
        all_product_list = []
        for i in all_product:
            path = request.META['HTTP_HOST']
            path1 = ['http://' + path + '/media/' + i for i in i.product_images]
            i.product_images = path1
            products = {
                'product_images': i.product_images,
                'SKU': i.SKU,
                'product_name': i.product_name,
                'product_price': i.product_price,
                'product_sale_price': i.product_sale_price,
                'product_quantity': i.product_quantity,
                'product_category': i.product_category,
                'product_items': i.product_items,
                'product_branding': i.product_branding,
                'product_tags': i.product_tags,
                'product_size': i.product_size,
                'product_color': i.product_color,
                'product_fabric': i.product_fabric,
                'product_description': i.product_description,
            }
            all_product_list.append(products)
        return JsonResponse({'Products': all_product_list})

    except Exception as e:
        return JsonResponse({'Message': e.__str__()})


@api_view(['POST'])
def update_product(request):
    primary_key = request.POST['ID']
    product_category = request.POST.get('Product Category')
    product_items = request.POST.get('Product Item')
    product_images = request.FILES.getlist('Product Images')
    SKU = request.POST.get('SKU ID')
    product_name = request.POST.get('Product Name')
    product_price = request.POST.get('Product Price')
    product_sale_price = request.POST.get('Product Sale Price')
    product_quantity = request.POST.get('Product Quantity')
    product_branding = request.POST.get('Product Brand')
    product_tags = request.POST.get('Product Tags')
    product_size = request.POST.get('Product Size')
    product_color = request.POST.get('Product Color')
    product_fabric = request.POST.get('Product Fabric')
    product_description = request.POST.get('Product Description')
    try:
        seller_user = Register.objects.get(email=request.session['email'])
        update = Product.objects.get(product_seller=seller_user, id=primary_key)
        if len(product_images) != 0:
            if not product_category == '':
                update.product_category = product_category
            if not product_items == '':
                update.product_items = product_items
            if not product_images == '':
                update.product_images = [
                    default_storage.save(os.path.join(settings.MEDIA_ROOT, 'document', image.name.replace(' ', '_')),
                                         image) for image in product_images]
            if not SKU == '':
                update.SKU = SKU
            if not product_name == '':
                update.product_name = product_name
            if not product_price == '':
                update.product_price = product_price
            if not product_sale_price == '':
                update.product_sale_price = product_sale_price
            if not product_quantity == '':
                update.product_quantity = product_quantity
            if not product_branding == '':
                update.product_branding = product_branding
            if not product_tags == '':
                update.product_tags = product_tags
            if not product_size == '':
                update.product_size = product_size
            if not product_color == '':
                update.product_color = product_color
            if not product_fabric == '':
                update.product_fabric = product_fabric
            if not product_description == '':
                update.product_description = product_description
        else:
            if not product_category == '':
                update.product_category = product_category
            if not product_items == '':
                update.product_items = product_items
            if not SKU == '':
                update.SKU = SKU
            if not product_name == '':
                update.product_name = product_name
            if not product_price == '':
                update.product_price = product_price
            if not product_sale_price == '':
                update.product_sale_price = product_sale_price
            if not product_quantity == '':
                update.product_quantity = product_quantity
            if not product_branding == '':
                update.product_branding = product_branding
            if not product_tags == '':
                update.product_tags = product_tags
            if not product_size == '':
                update.product_size = product_size
            if not product_color == '':
                update.product_color = product_color
            if not product_fabric == '':
                update.product_fabric = product_fabric
            if not product_description == '':
                update.product_description = product_description
        update.save()
        return JsonResponse({'Message': 'Update Product Successfully.'})
    except Exception as e:
        return JsonResponse({'Message': e.__str__()})


@api_view(['POST'])
def delete_product(request):
    primary_key = request.POST['Product ID']
    try:
        seller_user = Register.objects.get(email=request.session['email'])
        delete = Product.objects.get(product_seller=seller_user, id=primary_key)
        delete.delete()
        return JsonResponse({'Message': 'Delete Product Successfully.'})

    except Exception as e:
        return JsonResponse({'Message': e.__str__()})
