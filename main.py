from flask import Flask, request, jsonify
import json
import logging

app = Flask(__name__)
logging.basicConfig(level='DEBUG')
LOG = logging.getLogger('api')

"""
@learning-python-api intents to create new api using Flask
1) API with a Create / Update / Delete tasks with ID, Title and Description.
2) All data will be persisted on Json file (data.json)
"""


def get_data_file():
    with open('data.json', 'r') as f:
        tasks = json.load(f)
        return tasks


def update_data_file(content):
    with open('data.json', 'w') as outfile:
        json.dump(content, outfile, indent=4)


@app.route('/tasks', methods=['GET'])
def get_task():
    """
    Get task by id (request.arg)
    """
    if request.args.get('id'):
        task_id = int(request.args.get('id'))
    else:
        task_id = None
        
    tasks = get_data_file()
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)

    return jsonify(
        {
            "error": f"task id {task_id} not found!"
        }
    )


@app.route('/tasks', methods=['PUT'])
def create_task():
    """
    Add new task using this payload
    {
        "title": "bla",
        "description": "bla-blup"
    }
    """
    tasks = get_data_file()
    task = {}
    data = json.loads(request.data)
    
    task['id'] = tasks[-1]['id'] + 1
    task['title'] = data['title']
    task['description'] = data['description']
    
    tasks.append(task)
    update_data_file(tasks)
    return jsonify(tasks)


app.run(debug=True)
