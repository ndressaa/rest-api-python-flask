from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {
        'id': 0,
        'name': 'Andressa',
        'skills': ['PHP', 'Python']
     },
    {
        'id': 1,
        'name': 'Dorothy',
        'skills': ['Java', 'SQL']
    },
    {
        'name': 'Bolt',
        'skills': ['JavaScript', 'Ruby']
    }
]

# returns dev info by their id, also edits and/or deletes dev data
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            response = {'status': 'error',
                        'message': 'There is no developer with id {}'.format(id)}
        except Exception:
            response = {'status': 'error',
                        'message': 'Unknown error'}
        return response
    elif request.method == 'PUT':
        devdata = json.loads(request.data)
        developers[id] = devdata
        return devdata
    elif request.method == 'DELETE':
        developers.pop(id)
        return {'status': 'success', 'message': 'Record deleted'}

# returns list of all devs and allows to register a new dev
@app.route('/dev', methods=['POST', 'GET'])
def devlist():
    if request.method == 'POST':
        devdata = json.loads(request.data)
        index = len(developers)
        devdata['id'] = index
        developers.append(devdata)
        return developers[index]
    elif request.method == 'GET':
        return jsonify(developers)

if __name__ == '__main__':
    app.run(debug=True)