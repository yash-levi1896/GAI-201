import json
def Displayoptions():
     print("\nMenu:")
     print("1. Add Snack to Inventory")
     print("2. Remove Snack from Inventory")
     print("3. Update Snack Availability")
     print("4. Record Sale")
     print("5. Display Available items")
     print("6. Total Sales Amount")
     print("7. Exit")
               
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
     
def Record():
      id=int(input("Enter the id of snack to be sold: "))

      try:
       with open("db.json", "r") as file:
        content = file.read()
        data=json.loads(content)
        
        for i in range(len(data)):
            if data["Inventory"][i]["ID"]==id:
                 if data["Inventory"][i]["Availability"]=="yes":
                     data["sales"].append(data["Inventory"][i])
                     del data["Inventory"][i]
                     break
                 else:
                     print("Item is not available for sale")
                     break
            
        with open("db.json", "w") as file:

           file.write(json.dumps(data, indent=4))
           print("Item added in the sales record")
      except FileNotFoundError:
        print("File not found.")
      except Exception as e:
       print("An error occurred:", e)
      pass
def Display():
    try:
       with open("db.json", "r") as file:
        content = file.read()
        data=json.loads(content)
        
        Available_items=[snacks for snacks in data["Inventory"] if snacks["Availability"]=="yes"]
        if len(Available_items)>0:
            for snack in Available_items:
              print(f"Item Name:{snack['Name']} , Price:{snack['Price']}")
        else:
           print("No snack available")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
       print("An error occurred:", e)

def TotalSales():
   with open("db.json", "r") as file:
        content = file.read()
        data=json.loads(content)
        sum=0

        for sale in data["sales"]:
           sum+=sale["Price"]
         
        print("Your Total sales amount:",sum)
   
    
def main():
     print("Welcome to Mumbai Munchies")
     
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
                Record()
          elif choice == 5:
               print("Menu:")
               Display()
          elif choice == 6:
               TotalSales()
          elif choice == 7:
            print("Exiting the application. Goodbye!")
            break
          else:
            print("Invalid choice. Please enter a valid option.")



main()
               
     