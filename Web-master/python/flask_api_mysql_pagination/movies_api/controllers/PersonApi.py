from flask import Blueprint
from app import app
from services.PersonService import PersonService
from flask import jsonify
from flask import flash, request

Person_api = Blueprint('person_api', __name__)

person_service = PersonService()

@Person_api.route('/person', methods=['POST'])
def add_Person():
    try:
        _json = request.json
        _name = _json['name']from app import app
        # validate the received values
        if _name and request.method == 'POST':
            lastrowid = person_service.add_Person(_name)
            resp = jsonify({'id': lastrowid})
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)

@Person_api.route('/person', methods=['GET'])
def get_all_Person():
    try:
        page = request.args.get('page', default = 1, type = int)
        name = request.args.get('name', default = None, type = str)
        app.logger.info("page: " + str(page))
        
        pagesize = 2
        rows = person_service.get_all_roles(page, pagesize, name)
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@Person_api.route('/person/<int:id>', methods=['GET'])
def get_person_by_id(id):
    try:
        row = person_service.get_rol_by_id(id)
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@Person_api.route('/person/<int:id>', methods=['PUT'])
def update_person(id):
    try:
        _json = request.json
        _name = _json['name']		
        # validate the received values
        if _name and id and request.method == 'PUT':
            rows_affected = person_service.update_rol(id, _name)
            app.logger.info("PUT update_rol, rows_affected: " + str(rows_affected))
            if rows_affected == 0:
                resp = jsonify({'message': 'Person was not updated!'})
                resp.status_code = 200
            else:
                resp = jsonify({'message': 'Person updated successfully!'})
                resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)

@Person_api.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    try:
        rows_affected = person_service.delete_rol(id)
        if rows_affected == 0:
            resp = jsonify({'message': 'Person was not deleted!'})
            resp.status_code = 200
        else:
            resp = jsonify({'message': 'Person deleted successfully!'})
            resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@Person_api.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp