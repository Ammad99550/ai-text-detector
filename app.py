from flask import Flask, render_template, request, jsonify
from model.detection_model import TextDetectionModel

app = Flask(__name__)

# Initialize the detection model
detection_model = TextDetectionModel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_text():
    content = request.json.get('content')
    
    # Use the detection model to analyze the text
    detection_result = detection_model.detect(content)
    
    return jsonify({'result': detection_result})

if __name__ == '__main__':
    app.run(debug=True)
