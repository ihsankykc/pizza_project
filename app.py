from flask import Flask, render_template,request, redirect
from datetime import datetime

app = Flask(__name__)
quantity = []
data = []
datas = []
order_number = 101

def generate_order(clock,order_number,order_details):
    global data
    datas.append((clock,order_number,order_details)) 
    data = [clock, order_number, order_details]

@app.route('/')
def welcome():
    return render_template("hello.html")

@app.route('/main')
def main_page():
    return render_template("main.html")
    
@app.route('/create_order')
def create_order():
    return render_template("create_order.html")

@app.route('/register_order', methods = ['POST'] )
def register_order():
    # local variable for selected choice of pizzas
    currentOrders = []
    global order_number

    # get the selected items and quantities from form.html
    selected_pizzas = request.form.getlist('pizza')
    quantity_margherita = request.form.get('quantity_Margherita')
    quantity_Four_Cheese = request.form.get('quantity_Four_Cheese')
    quantity_Pepperoni = request.form.get('quantity_Pepperoni')

    # append the choices into my list as tuples (selected pizza,quantity)
    if 'Margherita' in selected_pizzas and quantity_margherita :
        currentOrders.append(('Pizza Margherita',quantity_margherita))
    if 'Four_Cheese' in selected_pizzas and quantity_Four_Cheese :
        currentOrders.append(('Pizza Four Cheese',quantity_Four_Cheese))
    if 'Pepperoni' in selected_pizzas and quantity_Pepperoni :
        currentOrders.append(('Pizza Pepperoni',quantity_Pepperoni))
    
    # assign date and time of the order
    rightNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    generate_order(rightNow,order_number,currentOrders)
    
    # iterate the order number every time new order is created
    order_number+=1


    return redirect('/view_order')

@app.route('/view_order')
def view_order():
    print(data)
    return render_template('view_order.html',
                           view_order=data)

@app.route('/current_orders')
def show_current_orders():        
    print("view data", data)
    return render_template('order.html',
                           orders=datas
                           )


if __name__ == '__main__':  
    app.run(debug=True)


# py -m flask run -p 5000