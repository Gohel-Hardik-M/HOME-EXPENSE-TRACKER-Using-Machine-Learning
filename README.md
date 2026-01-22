#                                                                                 Home Expense Tracker Using Machine Larning 


  

# About : 
                  This is an Home Expense Tracker which stores the home expenses and also has functionality to analyse the expense  of user selected Month & Year  also predicts next 3 Months Expected Expenses               so users can plan their trips or events based on that.

# What's New/Unique About This Project :

                           - Tips & Recommendations For Better Expense Management Using Machine Learning Model (Created By Me) Based on The Expenses Of the Months 
                           - Expense Predictions For Next Months Using Machine Learning Models (Created By Me)
                  
# Functionalities :

                         - Expenses Management 
                         - Expenses Analysis
                         - Expense Predictions For Next Months Using Machine Learning Models (Created By Me)
                         - Tips & Recommendations For Better Expense Management Using Machine Learning Model (Created By Me) Based on The Expenses Of the Months 
                         - Report Download Option 


# Technolgied Used :      
                         
                         - Python   :
                                        => Core Programming Language Used for Backend Logic and Machine Leaning Implementation
                        - Flask (Python Library)  :
                                        => used as the web Framework to build the backend , handle routes and connects frontend logic to backend logic.
                        - Scikit-Learn (Python Library)  :     
                                        => Used to create and Train Machine Learning Models to predict future Expenses or Category Wise Expenses
                        - Pickel (Python Library)  :         
                                        => Used to save and load machine learning Models to use in application without retraining them.
                        - Pandas (Python Library) :
                                        => Used for data processing , manipulation , and formating for analysis and ML predictions and Training.
                        - Matplotlib (Python Library) :
                                        => Used to generate visulizations like pie charts for expense analysis.
                        - MySQL :
                                        => Used as the database to store the user expenses.
                        - HTML / CSS  / JQuery :
                                        => Used to create and style the user interface for the application.

# View :





![image](https://github.com/user-attachments/assets/9c8068e0-0c4c-4a08-8e91-243128035b7b)


![image](https://github.com/user-attachments/assets/6a16d2ae-98d0-4217-be08-216e47df84d7)


![image](https://github.com/user-attachments/assets/30b15804-ea59-4d69-abf3-d117cb248877)




 
## ⚙️ How to Use


#### 📝 Step : 1️⃣
### 🗄️ Database Setup

This project requires a MySQL database.  
A ready‑to‑use SQL dump file (**`home_tracker.sql`**) is included in the repository at : **`Database - MYSQL/home_tracker.sql`**

You can import it in two ways:

### Option 1: Using phpMyAdmin (XAMPP)
1. Start **XAMPP** and run **Apache** + **MySQL** modules.
2. Open [http://localhost/phpmyadmin](http://localhost/phpmyadmin) in your browser.
3. Go to the **Import** tab.
4. Select the uploaded file (`home_tracker.sql`) at **`Database - MYSQL/    home_tracker.sql`** and click **Go**.
5. The tables will be created automatically.

### Option 2: Using MySQL Command Line
```bash
# Log in to MySQL
mysql -u root -p

# Create a new database
CREATE DATABASE home_tracker;

# Exit MySQL and run the import
mysql -u root -p home_tracker < database.sql

```
#### 📝 Step : 2️⃣

### Run the Web App 
You can directly run this project by running the Flask app:

```bash
# ⚙️ Clone the repository

# 👉 Install dependencies
pip install -r requirements.txt

# 🚀 Run the app
python app.py
```


                            
                        

