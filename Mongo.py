from flask import Flask, request, jsonify
import pymongo

app=Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://indapwaramarja:Manu292104@cluster0.ddhbgrl.mongodb.net/?retryWrites=true&w=majority")
database = client['taskdb']
collections=database['taskcollection']

@app.route('/add',methods=['POST'])
def insert():
    if request.method=='POST':
        name=request.json['name']
        id_val=request.json['id']
        collections.insert_one({"name":name, "id":id_val})
        return jsonify(str("Record Inserted Successfully!"))


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        try:
            get_name = request.json['get_name']
            record = collections.find_one({"name": get_name})

            if record is not None:
                id_new = record.get("id", 0) + 10
                collections.update_one({"name": get_name}, {'$set': {"id": id_new}})
                return jsonify({'message': 'Record Updated Successfully!'}), 200
            else:
                return jsonify({'message': 'Record not found'}), 404
        except Exception as e:
            print("Error:", str(e))
            return jsonify({'error': str(e)}), 500


@app.route('/delete',methods=["POST"])
def delete():
    if request.method=='POST':
        del_name=request.json['del_name']
        collections.delete_one({"name":del_name})
        return jsonify(str("Record Deleted Successfully!"))

@app.route('/get',methods=['GET'])
def get():
    if request.method=='GET':
        rec=collections.find()
        l=[]
        for i in rec:
            l.append(i)
        return jsonify(str(l))


if __name__=='__main__':
    app.run(port=5001)