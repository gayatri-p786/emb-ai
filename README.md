# EmotionDetector Website

This project is part of the final project for one of the modules in the IBM Professional Developer course. It includes a Flask-based web application that utilizes IBM Watson's NLP API to detect emotions in text input.

## Overview

The EmotionDetector Website allows users to input text and receive an analysis of the emotions detected in the text. It uses IBM Watson's EmotionPredict API for the emotion detection process.

### Files Included

- **server.py**: This file contains the Flask application that serves the web interface and handles requests to the emotion detection functionality.
- **index.html**: The HTML template for the web interface where users can input text and trigger the emotion detection process.
- **EmotionDetection/emotion_detection.py**: The Python script that interacts with IBM Watson's API to perform emotion detection based on provided text input.
- **static/mywebscript.js**: JavaScript file (not shown here) that likely contains client-side scripting for the web interface.

## Setup

To set up and run the EmotionDetector Website locally, follow these steps:

1. **Clone the Repository:**
   - Replace `<repository_url>` with the actual URL of your repository.
   - Navigate to the cloned directory in your terminal:
     ``` bash
     git clone <repository_url>
     cd <repository_name>
     ```

2. **Install Dependencies:**
   - Ensure you have Python 3.x installed on your machine.
   - Install required Python packages using pip:
     ``` bash
     pip install Flask requests
     ```

3. **Run the Application:**
   - Start the Flask server to run the web application locally:
     ``` bash
     python server.py
     ```
   - Open a web browser and go to `http://localhost:5000/` to access the EmotionDetector Website.

## Usage

1. **Input Text:**
   - On the home page (`/`), enter text into the input field labeled "Please enter the text to be analyzed".

2. **Run Emotion Detection:**
   - Click the "Run Sentiment Analysis" button to trigger the analysis.

3. **View Results:**
   - The detected emotions will be displayed under "Result of Emotion Detection" on the web page.

## Example

Here's an example of how to use the EmotionDetector Website:

1. Enter the text "I'm feeling excited about this project!" into the input field.
2. Click "Run Sentiment Analysis".
3. The system will respond with the detected emotions and the dominant emotion identified.

## Notes

- Ensure that you have valid API credentials from IBM Watson and update `emotion_detection.py` accordingly if deploying to a production environment.
- Customize the web interface (`index.html`) and JavaScript (`mywebscript.js`) as needed for your specific requirements or branding.
- Error handling and edge cases (such as empty input) should be considered and implemented in both the Flask routes and client-side JavaScript.
