from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        'Contact': "9987644456",
        'Name': 'Raju',
        'done': False,
        'id': 1
    },
    {
        ''Contact': "987654322",
        'Name': 'Rahul',
        'done': False,
        'id': 2
    }
]
@app.route("/add-data", methods=["post"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please Provide The Data"
        }, 400)
    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('description'),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task Added Successfully"
    })
@app.route('/get-data')
def get_task():
    return jsonify({
        "data": tasks
    })
if (__name__ == "__main__"):
    app.run(debug=True)