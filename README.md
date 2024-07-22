# Face Detection and Analysis API

This Flask application detects faces in an image using RetinaFace and analyzes emotions, age, gender, and race using DeepFace.

## Setup

1. Clone the repository:
   
    git clone https://github.com/yourusername/face-detection-api.git
    cd face-detection-api
    

2. Create and activate a virtual environment:
    
    python -m venv venv
    source venv\Scripts\activate  
    

3. Install the dependencies:
    
    pip install -r requirements.txt
    

## Running the Application

1. Start the Flask server:
    
    python app.py
    

2. Send a POST request to `/detect` endpoint with an image file:
    - URL: `http://127.0.0.1:5000/detect`
    - Method: `POST`
    - Form-data: `file` (choose an image file)

## Example Response

{
    "analysis": [
        {
            "age": 23,
            "dominant_emotion": "happy",
            "dominant_gender": "Woman",
            "dominant_race": "white",
            "emotion": {
                "angry": 1.5592378096573238e-05,
                "disgust": 4.969993116304387e-09,
                "fear": 1.7791402834497946e-05,
                "happy": 98.06563842687837,
                "neutral": 1.929672922472532,
                "sad": 0.0046187148679492545,
                "surprise": 3.5771144979933305e-05
            },
            "face_confidence": 0.89,
            "gender": {
                "Man": 9.258131967726513e-05,
                "Woman": 99.99990463256836
            },
            "race": {
                "asian": 3.435780826510637e-09,
                "black": 2.692588719262895e-11,
                "indian": 9.71296099105956e-09,
                "latino hispanic": 0.00790729172877036,
                "middle eastern": 0.0038503745599882677,
                "white": 99.9882459640503
            },
            "region": {
                "h": 338,
                "left_eye": [435,249],
                "right_eye": [306,247],
                "w": 338,
                "x": 204,
                "y": 115
            }
        }
    ],
    "faces_detected": 1,
    "message": "Detection complete"
}
