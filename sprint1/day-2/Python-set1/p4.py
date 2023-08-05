def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


num_list = []
n = int(input("Enter the number of elements in the list: "))
        
for i in range(n):
            num = float(input(f"Enter element {i+1}: "))
            num_list.append(num)
        
if len(num_list) > 0:
            total_sum = calculate_sum(num_list)
            average = calculate_average(num_list)
            
            print(f"Sum: {total_sum}")
            print(f"Average: {average}")
else:
            print("The list is empty. Please enter some numbers.")
            




