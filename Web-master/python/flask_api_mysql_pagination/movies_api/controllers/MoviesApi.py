from flask import Blueprint
from app import app
from services.MovieService import MovieService
from flask import jsonify
from flask import flash, request

movie_api = Blueprint('movie_api', __name__)
movie_api
roles_service = MovieService()

@movie_api.route('/movie', methods=['POST'])
def add_movie():
    try:
        _json = request.json
        _name = _json['name']from app import app
        # validate the received values
        if _name and request.method == 'POST':
            lastrowid = roles_service.add_rol(_name)
            resp = jsonify({'id': lastrowid})
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)

@movie_api.route('/movie', methods=['GET'])
def get_all_movies():
    try:
        page = request.args.get('page', default = 1, type = int)
        name = request.args.get('name', default = None, type = str)
        app.logger.info("page: " + str(page))
        
        pagesize = 2
        rows = roles_service.get_all_roles(page, pagesize, name)
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@movie_api.route('/movie/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    try:
        row = roles_service.get_rol_by_id(id)
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@movie_api.route('/movie/<int:id>', methods=['PUT'])
def update_movie(id):
    try:
        _json = request.json
        _name = _json['name']		
        # validate the received values
        if _name and id and request.method == 'PUT':
            rows_affected = roles_service.update_rol(id, _name)
            app.logger.info("PUT update_rol, rows_affected: " + str(rows_affected))
            if rows_affected == 0:
                resp = jsonify({'message': 'Movie was not updated!'})
                resp.status_code = 200
            else:
                resp = jsonify({'message': 'Movie updated successfully!'})
                resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)

@movie_api.route('/movie/<int:id>', methods=['DELETE'])
def delete_movie(id):
    try:
        rows_affected = roles_service.delete_rol(id)
        if rows_affected == 0:
            resp = jsonify({'message': 'Movie was not deleted!'})
            resp.status_code = 200
        else:
            resp = jsonify({'message': 'Movie deleted successfully!'})
            resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
Movie
@movie_api.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp