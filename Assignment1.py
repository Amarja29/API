import mysql.connector as conn
from flask import Flask, request, jsonify
mydb=conn.connect(host='localhost',user='root',passwd='Shivangi@29')
cursor=mydb.cursor()
cursor.execute("create table if not exists amarja.assignment(id int(20),name varchar(20) )")
mydb.commit()
app=Flask(__name__)

@app.route('/add',methods=['GET','POST'])
def insert():
    if request.method=="POST":
        ID=request.json['id']
        Name=request.json['name']
        s=f"insert into amarja.assignment values {ID,Name}"
        cursor.execute(s)
        mydb.commit()
        return jsonify((str("message : Record inserted Successfully")))

@app.route('/update',methods=["GET","POST"])
def update():
    if request.method=="POST":
        s="unknown"
        #cursor.execute("set sql_safe_update=0")
        cursor.execute(f"update amarja.assignment set id=0")
        mydb.commit()
        return jsonify((str("Updated Successfully")))

@app.route('/fetch',methods=["GET","POST"])
def fetch():
    if request.method=="GET":
        cursor.execute("select id,name from amarja.assignment")
        l=[]
        for i in cursor.fetchall():
            l.append(i)
        return jsonify((str(l)))

@app.route('/delete/<int:id_del>',methods=['POST','GET'])
def delete(id_del):
    if request.method=='POST':
        #id_del=request.json['id_del']
        cursor.execute("delete from amarja.assignment where id= %s",(id_del,))
        mydb.commit()
        return jsonify(str("Record Deleted Successfully"))

if __name__=='__main__':
    app.run(port=5002)

