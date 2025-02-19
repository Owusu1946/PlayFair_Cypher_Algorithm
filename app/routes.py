from flask import Blueprint, render_template, request, jsonify
from app.cipher import PlayfairCipher

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    operation = data.get('operation')
    text = data.get('text', '')
    key = data.get('key', '')

    try:
        cipher = PlayfairCipher(key)
        matrix = cipher.matrix
        
        if operation == 'encrypt':
            result = cipher.encrypt(text)
        else:
            result = cipher.decrypt(text)

        return jsonify({
            'success': True,
            'result': result,
            'matrix': matrix
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400 