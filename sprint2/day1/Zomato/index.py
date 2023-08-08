import json

def Displayoptions():
     print("\nMenu:")
     print("1. Add Snack to Inventory")
     print("2. Remove Snack from Inventory")
     print("3. Update Snack Availability")
     print("4. Take Order")
     print("5. Display Available items")
     print("6. Update order status")
     print("7. review Order")
     print("8. Exit")

def addInventory():
     id=int(input("Enter snack id "))
     name=input("Enter snack name ")
     price=int(input("Enter snack price "))
     while True:
          availability=input("availabilty status in yes or no ").lower()
          if availability=="yes" or availability=="no":
               break
          else:
               print("Enter vaild availability in terms of yes or no")
    
     try:
       with open("db.json", "r") as file:
        content = file.read()
        data=json.loads(content)
        data["Inventory"].append({"ID":id,"Name":name,"Price":price,"Availability":availability})
       with open("db.json", "w") as file:

        file.write(json.dumps(data, indent=4))

       print("Snack added to Inventory")
     except FileNotFoundError:
        print("File not found.")
     except Exception as e:
       print("An error occurred:", e)
     

def Remove_snack():
     id=int(input("Enter Id of snack you want to remove: "))
     
     try:
       with open("db.json", "r") as file:
        content = file.read()
        data=json.loads(content)
        
        for i in range(len(data)):
            if data["Inventory"][i]["ID"]==id:
                del data["Inventory"][i]
                break
            
        with open("db.json", "w") as file:

           file.write(json.dumps(data, indent=4))

           print("Snack Removed from Inventory")
     except FileNotFoundError:
        print("File not found.")
     except Exception as e:
       print("An error occurred:", e)

def Update_snack():
     id=int(input("Enter Id of snack you want to update: "))
     try:
       with open("db.json", "r") as file:
        content = file.read()
        data=json.loads(content)
        
        for i in range(len(data)):
            if data["Inventory"][i]["ID"]==id:
                 if data["Inventory"][i]["Availability"]=="yes":
                     data["Inventory"][i]["Availability"]="no"
                     break
                 else:
                     data["Inventory"][i]["Availability"]="yes"
                     break
            
        with open("db.json", "w") as file:

           file.write(json.dumps(data, indent=4))

           print("Snack updated in Inventory")
     except FileNotFoundError:
        print("File not found.")
     except Exception as e:
       print("An error occurred:", e)

def Display():
    try:
       with open("db.json", "r") as file:
        content = file.read()
        data=json.loads(content)
        
        Available_items=[snacks for snacks in data["Inventory"] if snacks["Availability"]=="yes"]
        for snack in Available_items:
            print(f"\nItem Name:{snack['Name']} , Price:{snack['Price']}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
       print("An error occurred:", e)


def TakeOrder():
       customer_name = input("Enter customer name: ")
       dish_ids = input("Enter dish IDs (separated by commas): ").split(",")
       Available=[]
       Unavailabe=[]
       orderIDs=[]
       with open("db.json", "r") as file:
        content = file.read()
        data=json.loads(content)
       for dish_id in dish_ids:
            
              dish_found = False

              for i in range(len(data["Inventory"])):
                if data["Inventory"][i]["ID"] == int(dish_id):
                    if data["Inventory"][i]["Availability"] == 'yes':
                        Available.append(data["Inventory"][i])
                        orderIDs.append(data["Inventory"][i]["ID"])
                        dish_found = True
                    else:
                       Unavailabe.append(data["Inventory"][i])
                       dish_found = True
                       break

              if not dish_found:
                print(f"Dish with ID {dish_id} not found in the menu.")

       if len(Unavailabe) > 0:
        print("The following dishes are unavailable:")
        for dish in Unavailabe:
            print(f"- {dish['Name']}")
       
       if len(Available)>0:
            order_id = len(data['orders']) + 1
            data['orders'].append({"OrderID":order_id,"CustomerName":customer_name,"DishID":orderIDs,"Status":"received"})

            with open("db.json", "w") as file:

              file.write(json.dumps(data, indent=4))

              print("Order processed successfully.")
       else:
           print("can't place the order snack is not available")



def UpdateOrder():
    order_id = int(input("Enter the order ID to update status: "))
    new_status = input("Enter the new status: ")
    updated = False
    with open("db.json", "r") as file:
        content = file.read()
        data=json.loads(content)
    for i in range(len(data["orders"])):
        if data["orders"][i]["OrderID"] == order_id:
            data["orders"][i]["Status"] = new_status
            updated = True
            break

    if updated:
         with open("db.json", "w") as file:
              file.write(json.dumps(data, indent=4))
              print("Order status updated successfully.")
    else:
        print("Order not found.")
    

def ReviewOrder():
    with open("db.json", "r") as file:
        content = file.read()
        data=json.loads(content)
    if len(data["orders"]) == 0:
        print("No orders placed yet.")
    else:
        print("Order Review:")
        for order in data["orders"]:
            print(f"Order ID: {order['OrderID']}")
            print(f"Customer Name: {order['CustomerName']}")
            print("Dishes:")
            for dish_id in order['DishID']:
                dish = next((item for item in data["Inventory"] if item['ID'] == dish_id), None)
                if dish:
                    print(f"- {dish['Name']} - Price:{dish['Price']}")
            print(f"Status: {order['Status']}")
            print()

           







def main():
     print("Welcome to Zomato")
     
     while True:
          Displayoptions()
          choice=int(input("Enter your choice:"))
          
          if choice==1:
               addInventory()
          elif choice==2:
               Remove_snack()
          elif choice==3:
               Update_snack()
          elif choice == 4:
                TakeOrder()
          elif choice == 5:
               Display()
          elif choice == 6:
               UpdateOrder()
          elif choice == 7:
               ReviewOrder()
          elif choice == 8:
            print("Exiting the application. Goodbye!")
            break
          else:
            print("Invalid choice. Please enter a valid option.")

main()