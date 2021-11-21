import datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

fruit_info = [
        {'type':'Apple', 'image_path':'img/apple.png'},
        {'type':'Blackberry', 'image_path':'img/blackberry.png'},
        {'type':'Raspberry', 'image_path':'img/raspberry.png'},
        {'type':'Strawberry', 'image_path':'img/strawberry.png'},
    ]

@app.route('/')         
def index():
    return render_template("index.html", fruit_info = fruit_info)

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    total = 0
    fruits = [i['type'] for i in fruit_info]
    checkout_time = datetime.datetime.now().strftime("%A, %B %d, %Y at %m:%M%p")
    for x in request.form:
        if x in fruits:
            total += int(request.form[x])
    print('Charging ' + request.form["first_name"] + ' ' + request.form['last_name'] + ' for ' + str(total) + ' fruits')
    return render_template("checkout.html", fruit_info = fruit_info, total = total, checkout_time = checkout_time)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html", fruit_info = fruit_info)

if __name__=="__main__":   
    app.run(debug=True)