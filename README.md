# Face Recognition Attendance System

This project is a **Face Recognition Attendance System** built with Python. It uses Streamlit for a user-friendly web interface, captures images from a camera, registers faces, and maintains attendance records in a database. The system allows users to check attendance and is designed for easy deployment and use.

## Features

- **Face Registration**: Capture and register user faces using a camera.
- **Face Recognition**: Recognize and authenticate registered faces.
- **Attendance Tracking**: Record attendance of recognized users and store data in a database.
- **Attendance Check**: Users can view their attendance records.
- **Streamlit Interface**: Provides an interactive web interface for users.

## Technologies Used

- **Python**: Core programming language used.
- **OpenCV**: For capturing and processing images.
- **Face Recognition Library**: Used for detecting and recognizing faces.
- **Streamlit**: For building a web-based user interface.
- **SQLite/MySQL**: For storing attendance records.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/face-recognition-attendance-system.git
   cd face-recognition-attendance-system
2. **Install Dependencies**: Ensure you have Python installed, then install the required libraries:

   ```bash
   pip install opencv-python face-recognition streamlit
   
3. **Run the Application:**

   After cloning the repository and installing all the necessary libraries, run the following command to start the Streamlit app:
   ``` bash
   streamlit run main.py
   
**Home Page**: Below is a screenshot of the Streamlit app homepage showcasing the face registration, attendance tracking, and mark attendance features.
   ![Home](https://github.com/user-attachments/assets/da751a0c-22cd-4d24-9518-e7a4d37213f7)

