from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
# Create your views here.


from .models import UserData
from .serializer import UserDataSerializer



@csrf_exempt
def get_all_User_Data(request):
    if request.method == 'GET' :
        users= UserData.objects.all()
        user_serializer=UserDataSerializer(users,many=True)
        return JsonResponse(user_serializer.data,safe=False)


@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        #just fafo with json and what the request method has inside it 
        req_data=json.loads(request)
        print('\n\n\n')
        print(req_data)
        print('\n\n\n')
        
        
        
        New_user=JSONParser().parse(request)
        print(New_user)
        new_user_serializer=UserDataSerializer(data=New_user)
        if new_user_serializer.is_valid():
            new_user_serializer.save()
            return JsonResponse("added succesfully ",safe=False)
        else:
            print(new_user_serializer.data)
            return JsonResponse("failed to add",safe=False)
  
  
      