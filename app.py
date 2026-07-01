from flask import Flask, render_template, jsonify, request
import re
# Main application logic
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')
    
    # Heuristic rules evaluation
    length_ok = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[_@$!%*?&]', password))
    
    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    
    if score <= 2:
        strength = "weak"
    elif score <= 4:
        strength = "medium"
    else:
        strength = "strong"
        
    return jsonify({
        "strength": strength,
        "score": score,
        "details": {
            "length": length_ok,
            "upper": has_upper,
            "lower": has_lower,
            "digit": has_digit,
            "special": has_special
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
