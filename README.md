Hand Gesture to Speech Interpreter

A real-time hand gesture recognition application that uses your webcam to detect specific hand gestures and converts them into spoken messages. Built with OpenCV, MediaPipe, and pyttsx3, it serves as a simple prototype for sign language interpretation and human-computer interaction.
Features

    Real-time detection of hand gestures through a webcam.

    Recognition of multiple phrases such as "Hello", "How are you", and "Nice to meet you".

    Spoken feedback via text-to-speech.

    On-screen display of recognized gestures.

    Easy to extend with new gestures and phrases.

    Cross-platform support (Windows, macOS, Linux).

Requirements

    Python 3.7 to 3.11 (MediaPipe does not support Python 3.12+ as of 2025).

    Webcam connected and accessible.

    Python packages:

        opencv-python

        mediapipe

        numpy

        pyttsx3

Installation

    Clone this repository:

bash
git clone https://github.com/your-username/gesture-speech-interpreter.git
cd gesture-speech-interpreter

(Recommended) Create and activate a virtual environment:

bash
python3.11 -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

Install dependencies:

    bash
    pip install opencv-python mediapipe numpy pyttsx3

Usage

Run the main Python script to start the application:

bash
python gesture_speech_interpreter.py

    A window showing your webcam feed will open.

    Show one of the pre-defined gestures to your webcam (see list below).

    The phrase corresponding to the recognized gesture will be spoken aloud and displayed on the screen.

    Press q to quit the application.

Supported Gestures
Gesture	Description
Hello	Thumb and index fingertips pinched together
How are you	Thumb, index, and middle fingertips all close together
Nice to meet you	Index and middle fingertips close, thumb far away

You can customize or add more gestures by modifying the gesture_to_text() function in the code.
Extending the Project

    Add more complex gestures by defining custom rules in gesture_to_text().

    Integrate machine learning models for accurate and comprehensive sign language interpretation.

    Improve user interface with feedback, GUI controls, and multi-language speech options.

    Port to mobile devices using TensorFlow Lite and mobile-compatible TTS engines.

Troubleshooting

    MediaPipe installation issues: Use Python 3.7 to 3.11. MediaPipe currently does not support later versions.

    Webcam not detected: Verify that your webcam is connected and not used by other applications.

    Audio output missing: Ensure your system audio is enabled and configured correctly.

    For Linux users, install OpenGL libraries if you face errors:

    text
    sudo apt-get install libgl1-mesa-glx

Contributing

Feel free to fork this repo, contribute new gestures, improve recognition accuracy, or suggest enhancements:

    Fork the repo

    Create a feature branch (git checkout -b feature/your-feature)

    Commit your changes (git commit -m 'Add some feature')

    Push the branch (git push origin feature/your-feature)

    Open a Pull Request
