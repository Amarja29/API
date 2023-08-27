from flask import Flask, request,jsonify
import mysql.connector as conn

mydb=conn.connect(host="localhost",user="root",passwd="Shivangi@29")
cursor=mydb.cursor()


app=Flask(__name__)

@app.route("/testfun")
def test():
    get_name=request.args.get("get_name")
    get_number=request.args.get("get_number")
    return "this is my function to get {} {}".format(get_name,get_number)

@app.route("/table")
def create():
    get_dbname=request.args.get("get_dbname")
    get_tablename=request.args.get("get_tablename")
    #cursor.execute(f"create database if not exists {get_dbname}")
    #cursor.execute(f"create table if not exists {get_tablename}")
    cursor.execute(f"select * from amarja.{get_tablename}")
    data=cursor.fetchall()
    mydb.commit()
    return jsonify(data)
if __name__=="__main__":
    app.run()