from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello_world():
    mydb = mysql.connector.connect(
      host="localhost",
      user="app",
      password="app"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT name FROM tarot.card")

    myresult = mycursor.fetchall()
    var1 = "cards > "
    for x in myresult:
        var1 = var1 + x[0]
    
    return var1