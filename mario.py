import requests
import json
from datetime import datetime

# main program
print("\n\n*** Mario ***\n")
order = ()
appended_order = []
orders = {}
order_number = int(input("Enter Order Number"))

while True:
    pizza_type = input("Enter Pizza Type: (Enter to Quit)")
    if pizza_type == '':
        
        break

    pizza_quantity = int(input("Enter Pizza Quantity: "))
    
    order = (pizza_type , pizza_quantity)
    appended_order.append(order)
        
    # assign date and time of the order
    rightNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    orders = { "date and time": rightNow ,
                "order number": order_number,
                "order": appended_order }

response = requests.post('http://localhost:5000/mario_register', json = orders)


# out_file = open("sample.json")
# json.dump(orders, out_file, indent=4)
# out_file.close()
# print(orders)


