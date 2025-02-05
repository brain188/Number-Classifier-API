from flask import Blueprint, request, jsonify
from app.utils import is_prime, is_perfect, get_fun_fact, classify_number

classify_blueprint = Blueprint('classify', __name__)

@classify_blueprint.route('/classify-number', methods = ['GET'])
def classify():
    number = request.args.get('number')
    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": number, "error": True}), 400
        
    number = int(number)
    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": classify_number(number),
        "digit_sum": sum(int(d) for d in str(abs(number))),
        "fun_fact": get_fun_fact(number)
    }
    
    return jsonify(result)
    
