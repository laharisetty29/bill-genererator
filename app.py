from flask import Flask,render_template,request,redirect
import mysql.connector
from config import bill_config

app=Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(**bill_config)
@app.route("/")
def home():
    return render_template("home.html")

@app.route('/index.html',methods=['GET','POST'])
def feedback():
    if request.method=='POST':
        name=request.form['name']
        item=request.form['item']
        quantity=request.form['quantity']
        price=request.form['price']

        conn=get_db_connection()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO feedback(customer_name,item,quantity,price) VALUES (%s,%s,%s,%s)",(name,item,quantity,price))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)