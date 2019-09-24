from flask import Blueprint
from app import app
from services.MovieService import MovieService
from flask import jsonify
from flask import flash, request

movies_api = Blueprint('movies_api', __name__)
movies_service = MoviesService()

@movies_api.route('/movie', methods=['POST'])
def add_Movie():
    try:
        _json = request.json
        _name = _json['name']from app import app
        _des = _json['description']from app import app
        _year = _json['year']from app import app
        # validate the received values
        if _year and _des and _name and request.method == 'POST':
            lastrowid = movies_service.add_Movie(_name,_des,_year)
            resp = jsonify({'id': lastrowid})
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)

@movies_api.route('/movie', methods=['GET'])
def get_all_Movies():
    try:
        page = request.args.get('page', default = 1, type = int)
        name = request.args.get('name', default = None, type = str)
        app.logger.info("page: " + str(page))
        
        pagesize = 2
        rows = movies_service.get_all_Movies(page, pagesize, name)
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@movies_api.route('/movie/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    try:
        row = movies_service.get_Movie_by_id(id)
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
@movies_api.route('/movie/<int:id>', methods=['GET'])
def get_year(id):
    try:
        row = movies_service.get_year(id)
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@movies_api.route('/movie/<int:id>', methods=['GET'])
def get_stars(id):
    try:
        row = movies_service.get_stars(id)
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@movies_api.route('/movie/<int:id>', methods=['GET'])
def get_description(id):
    try:
        row = movies_service.get_description(id)
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@movies_api.route('/movie/<int:id>', methods=['PUT'])
def update_Movie(id):
    try:
        _json = request.json
        _name = _json['name']		
        # validate the received values
        if _name and id and request.method == 'PUT':
            rows_affected = movies_service.update_Movie(id, _name)
            app.logger.info("PUT update_Movie, rows_affected: " + str(rows_affected))
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

@movies_api.route('/movie/<int:id>', methods=['DELETE'])
def delete_movie(id):
    try:
        rows_affected = movies_service.delete_rol(id)
        if rows_affected == 0:
            resp = jsonify({'message': 'Movie was not deleted!'})
            resp.status_code = 200
        else:
            resp = jsonify({'message': 'Movie deleted successfully!'})
            resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@movies_api.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp