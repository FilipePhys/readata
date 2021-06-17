from flask import Blueprint
from flask_restplus import Api, fields, Resource
from app_core.models import database

bp_api = Blueprint('api', __name__, url_prefix='/api')

api = Api(bp_api, version='1.0', title='Database API', description='Create')

api_docs = api.model("CustomUser model", {
    'id': fields.Integer(required=True, description="Database primary key"),
    'user': fields.String(required=True, description="User name"),
    'birth': fields.Date(description="Birth date"),
    'image address': fields.String(description="Profile image relative path"),
})


@api.route('/users/')
class UserList(Resource):
    qry_result = database.database_read

    @api.doc(body=api_docs)
    @api.marshal_list_with(api_docs)
    def get(self,):
        toshow = []
        for r in self.qry_result:

            toshow.append({"id": r.id, "user": r.username, "birth": r.birth_date, "image address": r.profile_img})
        return toshow

    @api.expect(api_docs, valitade=True)
    @api.marshal_with(api_docs)
    def post(self):
        response = api
        self.qryresult.append(response)
        return response, 200


# description=Create users and todo items through a REST API.
# 'First of all, begin by registering a new user via the registration form in the web interface.\n'
# 'Or via a `POST` request to the `/Register/` end point',
# decorators=[limiter.limit("50/day", error_message="API request limit has been reached (50 per day)")])
