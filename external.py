from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/mock-tax')
def mock_tax():
    # Simulación de respuesta 200
    return jsonify(Tax=15), 200

@app.route('/mock-tax-403')
def mock_tax_403():
    # Simulación de respuesta 403
    return jsonify(error="403"), 403

@app.route('/mock-tax-500')
def mock_tax_500():
    # Simulación de respuesta 500
    return jsonify(error="500"), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
