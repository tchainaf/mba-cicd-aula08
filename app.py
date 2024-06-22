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
                        'type': 'number',
                        'example': 10  # Exemplo do resultado para documentação
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
                    'a': {'type': 'number', 'example': 5},
                    'b': {'type': 'number', 'example': 3}
                },
                'required': ['a', 'b']
            }
        }
    ]
})
def add():
    """
    Endpoint para adicionar dois números.

    ---
    tags:
      - Matemática
    """
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
                        'type': 'number',
                        'example': 2
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
                    'a': {'type': 'number', 'example': 5},
                    'b': {'type': 'number', 'example': 3}
                },
                'required': ['a', 'b']
            }
        }
    ]
})
def subtract():
    """
    Endpoint para subtrair dois números.

    ---
    tags:
      - Matemática
    """
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
                        'type': 'number',
                        'example': 15
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
                    'a': {'type': 'number', 'example': 5},
                    'b': {'type': 'number', 'example': 3}
                },
                'required': ['a', 'b']
            }
        }
    ]
})
def multiply():
    """
    Endpoint para multiplicar dois números.

    ---
    tags:
      - Matemática
    """
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
                        'type': 'number',
                        'example': 2.5
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
                    'a': {'type': 'number', 'example': 10},
                    'b': {'type': 'number', 'example': 4}
                },
                'required': ['a', 'b']
            }
        }
    ]
})
def divide():
    """
    Endpoint para dividir dois números.

    ---
    tags:
      - Matemática
    """
    data = request.get_json()
    result = data['a'] / data['b']
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)