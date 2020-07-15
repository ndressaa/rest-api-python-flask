from flask import Flask, request
from flask_restful import Resource, Api
from skills import Skills
import json

app = Flask(__name__)
api = Api(app)

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
class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            response = {'status': 'error',
                        'message': 'There is no developer with id {}'.format(id)}
        except Exception:
            response = {'status': 'error',
                        'message': 'Unknown error'}
        return response
    def put(self, id):
        devdata = json.loads(request.data)
        developers[id] = devdata
        return devdata
    def delete(self):
        developers.pop(id)
        return {'status': 'success', 'message': 'Record deleted'}

# returns list of all devs and allows to register a new dev
class DevList(Resource):
    def get(self):
        return developers
    def post(self):
        devdata = json.loads(request.data)
        index = len(developers)
        devdata['id'] = index
        developers.append(devdata)
        return developers[index]

api.add_resource(Developer, '/dev/<int:id>')
api.add_resource(DevList, '/dev')
api.add_resource(Skills, '/skills')

if __name__ == '__main__':
    app.run(debug=True)