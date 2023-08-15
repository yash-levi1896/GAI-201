from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json
import os
# Create your views here.
def menushow(request):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(base_dir, 'db.json')
    with open(json_file_path,'r') as file:
        data=json.loads(file.read())
        return render(request,'index.html',{'dishes':data["menu"]})

def addDish(request):
    if request.method=='POST':
        dish_id=request.POST["id"]
        name=request.POST['name']
        price=request.POST['price']
        availability=request.POST['availability']

        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(base_dir, 'db.json')
        with open(json_file_path,'r') as file:
            data=json.loads(file.read())
            data["menu"].append({"ID":int(dish_id),"Name":name,"Price":int(price),"Availability":availability})

        with open(json_file_path,'w') as file:
            file.write(json.dumps(data,indent=4))
        #return HttpResponse("data added successfully!")
        return redirect('menu')
    return render(request, 'add.html')


def DeleteDish(request,id):
    if request.method=='POST':
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(base_dir, 'db.json')
        with open(json_file_path,'r') as file:
            data=json.loads(file.read())
            for i in data["menu"]:
                 if i["ID"]==int(id):
                      data["menu"].remove(i)
                      break
    
        with open(json_file_path,'w') as file:
         
         file.write(json.dumps(data,indent=4))
         return redirect('menu')
        
def UpdateDish(request,id):
    if request.method=='POST':
         name=request.POST['name']
         price=request.POST['price']
         availability=request.POST['availability']
         base_dir = os.path.dirname(os.path.abspath(__file__))
         json_file_path = os.path.join(base_dir, 'db.json')
         with open(json_file_path,'r') as file:
            data=json.loads(file.read())
            for dish in data["menu"]:
                if dish["ID"]==id:
                    dish["ID"]=id
                    dish["Name"]=name
                    dish["Price"]=price
                    dish["Availability"]=availability
                    break
         with open(json_file_path,'w') as file:
         
          file.write(json.dumps(data,indent=4))
          return redirect('menu')
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(base_dir, 'db.json')
        with open(json_file_path,'r') as file:
            data=json.loads(file.read())
            for dish in data["menu"]:
                if dish["ID"]==id:
                    x=dish
                    break
        return render(request, 'update.html',{'dish':x})
    
def TakeOrder(request):
    if request.method=='POST':
        name=request.POST['customer_name']
        selected_dishes = request.POST.getlist('selected_dishes')
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(base_dir, 'db.json')
        orderedDish=[]
        with open(json_file_path,'r') as file:
           data=json.loads(file.read())
           for i in selected_dishes:
               for dish in data["menu"]:
                   if dish["ID"]==int(i):
                       orderedDish.append(dish)
            
        placedOrder={}
        placedOrder["OrderID"]=len(data["order"])+1
        placedOrder["CustomerName"]=name
        placedOrder["Dishes"]=orderedDish
        placedOrder["Status"]='received'
        data["order"].append(placedOrder)
        with open(json_file_path,'w') as file:
         
         file.write(json.dumps(data,indent=4))
        return redirect('menu')

    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(base_dir, 'db.json')
        with open(json_file_path,'r') as file:
            data=json.loads(file.read())
            Available_items=[snacks for snacks in data["menu"] if snacks["Availability"]=="yes"]
        return render(request,'placeorder.html',{'dishes':Available_items})


def reviewOrder(request):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(base_dir, 'db.json')
    with open(json_file_path,'r') as file:
        data=json.loads(file.read())
        return render(request,'order.html',{'orders':data["order"]})
    
def UpdateStatus(request,orderID):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(base_dir, 'db.json')
    with open(json_file_path,'r') as file:
          data=json.loads(file.read())
    if request.method=='POST':
        stat=request.POST["status"]
        
        for i,order in enumerate(data["order"]):
              if order["OrderID"]==orderID:
                  data["order"][i]["Status"]=stat
                  break
        with open(json_file_path,'w') as file:
         file.write(json.dumps(data,indent=4))
        return redirect('order')       
       
    with open(json_file_path,'r') as file:
          data=json.loads(file.read())
          for order in data["order"]:
           if order["OrderID"]==orderID:
               return render(request,'updateorder.html',{'order':order})
    
    
               

           



    
         
    





        