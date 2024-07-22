from flask import Flask, request, jsonify
from retinaface import RetinaFace
import numpy as np
from PIL import Image
from deepface import DeepFace

app = Flask(__name__)

def detect_faces(image):
    detections = RetinaFace.detect_faces(image)
    return detections

@app.route('/detect', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    image = request.files['file']
    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    converted = Image.open(image).convert('RGB')
    imgarr = np.array(converted)
    results = detect_faces(imgarr)

    analyze = DeepFace.analyze(imgarr, actions=["emotion", "age", "gender", "race"])
    result = {
        'message': 'Detection complete',
        'faces_detected': len(results),
        'analysis': analyze
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
