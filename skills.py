from flask_restful import Resource

skills = ['JavaScript', 'Python', 'PHP', 'C#', 'Ruby']

class Skills(Resource):
    def get(self):
        return skills