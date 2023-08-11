from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from django.http import HttpResponse ,  JsonResponse
data={}
def hello(request):
    return HttpResponse("Welcome to greetings app!")

def hello1(request,username):
    return HttpResponse(f"hello {username}")
def hello2(request,username):
    return HttpResponse(f"Goodbye {username}")


#@api_view(['POST','GET'])
def create(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        data[key]=value
        print(data)
        return JsonResponse({"message":"data added to dictionary"})
    
    return render(request, 'index.html')
 
#@api_view(['GET'])
def readdata(request):
    return render(request, 'read.html',{'data': data})

#@api_view(['PATCH'])
def UpdateData(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        if key in data:
            data[key] = value
            return JsonResponse({"message":"Key-Value pair updated successfully."})
        else:
            return JsonResponse({"message":"key you want to update do not exist in dictionary"})
    return render(request, 'update.html')


def DeleteData(request):
    if request.method == 'POST':
        key = request.POST['key']
        if key in data:
            del data[key]
            return JsonResponse({"message":"Key-Value pair deleted successfully."})
        else:
            return JsonResponse({"message":"key you want to delete doesn't exist"})
    return render(request, 'delete.html')
        
def Home(request):
    return render(request, 'home.html')


    
    


