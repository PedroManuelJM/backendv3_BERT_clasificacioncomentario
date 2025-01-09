import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/pedrojm/modelv2_clasificacioncomentario"
HUGGINGFACE_TOKEN = "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"

headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

@app.route('/')
def home():
    return "Servidor funcionando", 200


@app.route('/clasificar', methods=['POST'])
def clasificar():
    try:
        data = request.json
        user_comment = data.get('user_comment')
        if not user_comment:
            return jsonify({"error": "Falta el comentario del usuario"}), 400

        payload = {"inputs": user_comment}
        response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            return jsonify({"error": "Error en la API de Hugging Face"}), 500

        # Procesar la respuesta de la API
        api_result = response.json()
        print("Respuesta de la API:", api_result)  # Depuración: verifica el formato

        # Verificar y acceder al primer nivel de la respuesta
        if isinstance(api_result, list) and len(api_result) > 0 and isinstance(api_result[0], list):
            first_result_set = api_result[0]  # Primer conjunto de resultados
        else:
            return jsonify({"error": "Respuesta inesperada de la API"}), 500

        # Seleccionar la etiqueta con el mayor puntaje
        if len(first_result_set) > 0:
            top_prediction = max(first_result_set, key=lambda x: x.get('score', 0))
            predicted_class = top_prediction.get('label', 'Desconocido')
        else:
            return jsonify({"error": "Sin resultados en la API"}), 500

        # Retornar los resultados
        return jsonify({
            "user_comment":user_comment,
            "classification": predicted_class
            }), 200

    except Exception as e:
        return jsonify({"error": f"Error procesando la solicitud: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()
