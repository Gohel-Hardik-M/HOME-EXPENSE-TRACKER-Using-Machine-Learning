from flask import Flask , render_template , request, redirect , flash , url_for
import mysql.connector as myconn
from mysql.connector.errors import ProgrammingError
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle

#for ML Models
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

db = myconn.connect(host='localhost',username = 'root',password='',database='home_tracker')
cursor = db.cursor(dictionary=True)

create_table = """ CREATE TABLE IF NOT EXISTS expenses_pro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE ,
    category VARCHAR(100),
    description TEXT,
    amount DECIMAL(10,2),
    payment_mode VARCHAR(100))"""
    
cursor.execute(create_table)


#----------------------------------------------------------------------HOME PAGE CODES------------------------------------------------------------------------------------------------------

@app.route('/', methods=['GET','POST'])
def index():

    cursor.execute('SELECT * FROM expenses_pro ORDER BY expense_date DESC')
    expenses = cursor.fetchall()
    return render_template('index.html',exp= expenses)


@app.route('/add',methods=['GET','POST'])
def add_expense():
     if request.method == 'POST':
   
        expense_date = request.form['date']
        category = request.form['category']
        amount = request.form['amount']
        description = request.form['description']
        payment_mode = request.form['payment_mode']
          
        insert_query = f"INSERT INTO expenses (expense_date , category , amount , description , payment_mode) values('{expense_date}','{category}',{amount},'{description}','{payment_mode}')"
        cursor.execute("INSERT INTO expenses_pro (expense_date,category,description , amount,payment_mode) values(%s,%s,%s,%s,%s)",(expense_date,category,description,amount,payment_mode))
        db.commit()
        return redirect('/') 
#-------------------------------------------------------------------------ANALYSE CODES--------------------------------------------------------------------------------------------

@app.route('/analyse',methods=['GET','POST'])
def analyse():
    
    
    
    month_query = """SELECT DISTINCT   MONTH(expense_date) AS month FROM  expenses_pro ORDER BY  month DESC;"""
    cursor.execute(month_query)
    mons = cursor.fetchall()
    
    year_query = """SELECT DISTINCT YEAR(expense_date) AS year FROM expenses_pro ORDER BY year DESC;"""
    cursor.execute(year_query)
    yrs = cursor.fetchall()
    return render_template('analyse.html',months = mons,years= yrs)

# ---------ANALYSE RESULT--------------------------
@app.route('/analyse_result',methods=['GET','POST'])
def analyse_result():
    return render_template('analyse_result.html')

#----------ANALYSE ACTION--------------------------

@app.route('/analyse_action',methods=['GET','POST'])
def analyse_action():
    if request.method == 'POST':
        month_ = request.form['month']
        month = int(month_)
        year = request.form['year']
        query = """SELECT category, expense_date, amount, payment_mode FROM expenses_pro WHERE MONTH(expense_date)=%s AND YEAR(expense_date) =%s  ;"""
        cursor.execute(query,(month,year)) 
        df = pd.DataFrame(cursor.fetchall())
        db.commit()    
        
        
        if df.empty:
            msg_alert = "Selected Month & Year Has No Expenses."
            msg_advice = 'Please select right Month & Year'
            return render_template('analyse.html',msg=msg_alert,advice = msg_advice)
        
        # maximum expense price & categort
        max_expense_id = int(df['amount'].idxmax())
        max_expense = df.loc[max_expense_id,['category','amount']]
        # Minimum Expense Price & Category
        min_id = int(df['amount'].idxmin())
        min_expese = df.loc[min_id,['category','amount']]
        
        #ploting here the category & amount
        cat = list(df['category'])
        am =  list(int(i) for i in df['amount'])
        plt.figure(figsize=(6,6))
        plt.pie(am,labels=cat,startangle=140)
        plt.title(f'Expense Analysis - {month}/{year}')
        chart_dir = 'C:/Users/hardi/Downloads/CS(EH)/DS/projects/Home Expenses Tracker/static'
        chart_path = os.path.join(chart_dir,'pie_chart.png')
        os.makedirs(chart_dir, exist_ok=True)
        plt.savefig(chart_path)
        plt.close()
        
        #ML MODELS 
        #1) All Category Predictions
        with open('C:/Users/hardi/Downloads/CS(EH)/DS/projects/Home Expenses Tracker/category_wise_model.pkl','rb') as f:
            category_model = pickle.load(f)
        
        convert_category = { 1:'Utilities',2:'Groceries', 3:'Transportation',4:'Healthcare',5:'Entertainment',6:'Education',7:'Personal Care',8:'Debt Payments', 9:'Savings',10:'Alcohol', 11:'Fruits', 12:'Gym' ,13:'Skincare' ,14:'Books' ,15:'Gifts'}
        category_model_result = []
        for i in range(1,len(convert_category)+1):
            category_model_result.append(i)
           # category_model_result.append(category_model.predict([[i,month+1,year]]))
        
        #2) Next Months Predictions
        with open('C:/Users/hardi/Downloads/CS(EH)/DS/projects/Home Expenses Tracker/expense_model.pkl','rb') as f:
            expense_model = pickle.load(f)
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        months_expenses = []
        
        for i in range(1,4):
            ex =expense_model.predict([[month+i]])
            months_expenses.append(int(ex))
        
        monthly_expenses =months_expenses
        moonths =months[month:month+3]
        
        #3) Tips Model 
        with open('C:/Users/hardi/Downloads/CS(EH)/DS/projects/Home Expenses Tracker/tips_model.pkl','rb') as f:
            tips_model = pickle.load(f)
        with open('C:/Users/hardi/Downloads/CS(EH)/DS/projects/Home Expenses Tracker/le_cat.pkl','rb') as f:
            le_cat = pickle.load(f)
        with open('C:/Users/hardi/Downloads/CS(EH)/DS/projects/Home Expenses Tracker/le_tip.pkl','rb') as f:
            le_tip = pickle.load(f)
            
        encode_category = {'Utilities':16,'Housing':16,'Medical':11,'Groceries':6,'Transportation':15,'Healthcare':9,'Entertainment':3,'Education':2,'Personal Care':12,'Savings':13,'Alcohol':0,'Fruits':4,'Gym':8,'Skincare':14,'Books':1,'Gifts':5}
        category_for_tips = [cat for cat in df['category']]
        expense_for_tips = [ex for ex in df['amount']]
        encoded_category = [encode_category[category_for_tips[i]] for i in range(len(category_for_tips))]
        
        result = []
        for i in range(len(encoded_category)):
           k = tips_model.predict([[encoded_category[i],expense_for_tips[i]]])
           tip = le_tip.inverse_transform(k)
           result.append(tip[0])
            
        return render_template('analyse_result.html',max_expense_price = max_expense, min_expense_ = min_expese,chart_url=chart_path ,monthly_expenses_ = zip(months_expenses,  moonths),tips = result) 



if __name__ == '__main__':
    app.run(debug=True)