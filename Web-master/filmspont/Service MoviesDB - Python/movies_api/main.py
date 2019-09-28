from app import app
from controllers.RolesApi import roles_api
from controllers.MoviesApi import movies_api

# Register each api here
app.register_blueprint(roles_api)
app.register_blueprint(movies_api)

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')