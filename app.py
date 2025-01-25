from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/user", methods=['GET', 'POST', 'DELETE', 'PUT'])
def users():
    return jsonify({'payload':'success'})


@app.route("/api/v1/users", methods=['GET'])
def v1_users():
    request.method == 'GET'
    return jsonify({'payload': []})


@app.route("/api/v1/users", methods=['POST'])
def v1_create_users():
    email = request.args.get('email')
    nombre = request.args.get('nombre')
    
    return jsonify ({'payload':{'email': email, 'nombre': nombre,}})

    
@app.route("/api/v1/user/add", methods=['POST'])
def v1_add_user():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    user_id = request.form.get('id')
    
    return jsonify ({'payload':{'email': email, 'nombre': nombre, 'id': user_id}})


@app.route("/api/v1/user/create", methods=['POST'])
def v1_create_user():
    
    data = request.get_json()
    
    nombre = data.get('nombre')
    email = data.get('email')
    user_id = data.get('id')
    
    return jsonify ({'payload':{'email': email, 'nombre': nombre, 'id': user_id}})


if __name__ == '__main__':
    app.run(debug=True)