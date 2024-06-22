from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/add', methods=['POST'])
@swag_from({
    'responses': {
        200: {
            'description': 'Addition result',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {
                        'type': 'number'
                    }
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'data',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'a': {'type': 'number'},
                    'b': {'type': 'number'}
                },
                'required': ['a', 'b']
            }
        }
    ]
})
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify(result=result)

@app.route('/subtract', methods=['POST'])
@swag_from({
    'responses': {
        200: {
            'description': 'Subtraction result',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {
                        'type': 'number'
                    }
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'data',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'a': {'type': 'number'},
                    'b': {'type': 'number'}
                },
                'required': ['a', 'b']
            }
        }
    ]
})
def subtract():
    data = request.get_json()
    result = data['a'] - data['b']
    return jsonify(result=result)

@app.route('/multiply', methods=['POST'])
@swag_from({
    'responses': {
        200: {
            'description': 'Multiplication result',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {
                        'type': 'number'
                    }
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'data',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'a': {'type': 'number'},
                    'b': {'type': 'number'}
                },
                'required': ['a', 'b']
            }
        }
    ]
})
def multiply():
    data = request.get_json()
    result = data['a'] * data['b']
    return jsonify(result=result)

@app.route('/divide', methods=['POST'])
@swag_from({
    'responses': {
        200: {
            'description': 'Division result',
            'schema': {
                'type': 'object',
                'properties': {
                    'result': {
                        'type': 'number'
                    }
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'data',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'a': {'type': 'number'},
                    'b': {'type': 'number'}
                },
                'required': ['a', 'b']
            }
        }
    ]
})
def divide():
    data = request.get_json()
    result = data['a'] / data['b']
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
