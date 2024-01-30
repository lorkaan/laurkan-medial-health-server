from flask import Flask, json, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

FailMsg = "Adding Assignee Failed"
SuccessMsg = "Asignee Added"
InitMsg = "Please Add Assignee."



filename = "./tests/TaskList.json"
assignee_filename = "./tests/assignees.json"
store_task_filename = "./tests/store_tasks.json"

@app.route("/tasklist")
def json_test_file():
    try:
        with open(store_task_filename, 'r') as f:
            data = json.loads(f.read())
    except:
        data = []
    if not isinstance(data, list) or len(data) <= 0:
        with open(filename, 'r') as f:
            data = json.loads(f.read())
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype="application/json"
    )
    return response

@app.route("/store_tasks", methods=['POST'])
def store_tasks():
    """
    Using a file as a makeshift quick and simple NoSQL Database
    for time purposes.
    """
    if not request.is_json:
        response = app.response_class(response=json.dumps({}), status=403, mimetype="application/json")
        return response
    else:
        data = request.json
        new_data = []
        for _, val in data.items():
            new_data.append(val)
        with open(store_task_filename, 'w+') as f:
            f.write(json.dumps(new_data))
        with open(store_task_filename, 'r') as f:
            saved_data = json.loads(f.read())
        if saved_data == new_data:
            response = app.response_class(
                response=json.dumps({'success': 1}),
                status=200,
                mimetype="application/json"
            )
            return response
        else:
            if os.path.exists(store_task_filename) and os.path.isfile(store_task_filename):
                os.remove(store_task_filename)
            response = app.response_class(
                response=json.dumps({'success': 0}),
                status=200,
                mimetype="application/json"
            )
            return response
            

@app.route("/add_assignee", methods=['GET', 'POST'])
def add_assignee():
    if request.method.lower() == 'post':
        name = request.form["name"]
        try:
            with open(assignee_filename, 'r') as f:
                prev_data = json.loads(f.read())
        except:
            prev_data = {}
        if isinstance(prev_data, list) and len(prev_data) > 0:
            prev_data.append({"userId": len(prev_data), "displayName": name})
        elif isinstance(prev_data, dict):
            new_key = len(prev_data.keys())
            prev_data[new_key] = name
        with open(assignee_filename, 'w+') as f:
            f.write(json.dumps(prev_data))
        new_data = {}
        with open(assignee_filename, 'r') as f:
            new_data = json.loads(f.read())
        if prev_data == new_data:
            return render_template('add_assignee.html', msg=SuccessMsg)
        else:
            return render_template('add_assignee.html', msg=FailMsg)
    else:
        # Has to be GET cause only get and post allowed.
        # Render the template
        return render_template('add_assignee.html', msg=InitMsg)

@app.route("/get_assignees")
def get_assignees():
    data = []
    with open(assignee_filename, 'r') as f:
        data = json.loads(f.read())
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype="application/json"
    )
    return response

if __name__ == '__main__':
    app.run(port=5001)