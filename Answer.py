from flask import Flask, request,jsonify
import mysql.connector as conn

app=Flask(__name__)
mydb=conn.connect(host='localhost',user='root',passwd='Shivangi@29')
cursor=mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.task (name varchar(30),id int)")

@app.route('/insert',methods=['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        id = request.json['id']
        cursor.execute("insert into taskdb.task values(%s,%s)",(name,id))
        mydb.commit()
        return jsonify((str("Record Inserted Successfully!")))

@app.route('/update',methods=['POST'])
def update():
    if request.method=='POST':
        get_name = request.json['get_name']
        cursor.execute("update taskdb.task set id = id+20 where name = %s",[get_name])
        mydb.commit()
        return jsonify(str("Record Updated Successfully!"))

@app.route('/delete',methods=['POST'])
def delete():
    if request.method=='POST':
        name_del=request.json['name_del']
        cursor.execute("delete from taskdb.task where name = %s",[name_del])
        mydb.commit()
        return jsonify(str("Record Deleted Successfully!"))

@app.route('/fetch',methods=['GET'])
def fetch():
    cursor.execute("select * from taskdb.task")
    l=[]
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))

if __name__=="__main__":
    app.run()