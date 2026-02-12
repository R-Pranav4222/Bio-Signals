# BioSignals: Natural Disaster Prediction through Animal Behavior Analysis

**BioSignals** is an innovative web application designed to predict potential natural disasters by analyzing video footage of animal behavior. It is a long-observed phenomenon that animals often exhibit unusual patterns of behavior in the hours or days leading up to seismic events like earthquakes. This project leverages modern technology to capture and analyze these "biosignals" to provide early warnings.

The system allows users to upload video clips, which are then processed by a backend machine learning model to detect anomalies. If unusual behavior is detected, the system flags it and can be configured to send alerts to relevant authorities, providing a potential window for precautionary measures.

---

## 🚀 Features

* **Secure User Authentication:** Sign-in system for registered users to access the platform.
* **Video Upload & Management:** Simple interface for users to upload video files for analysis.
* **Anomaly Detection Engine:** A Python-based backend processes videos to identify abnormal animal behaviors that may precede natural disasters.
* **Real-time Alert System:** A dedicated alerts page that displays warnings in real-time when a potential threat is detected.
* **Admin Dashboard:** A dashboard for administrators to monitor uploaded content and system status.
* **Responsive Frontend:** A clean and intuitive user interface built with HTML, CSS, and JavaScript.

---

## 🛠️ Tech Stack

This project is built with a combination of Python for the core machine learning logic and Node.js for handling web services, ensuring a robust and scalable architecture.

* **Backend:**
    * **Primary Logic:** Python with Flask
    * **Web Server/API:** Node.js with Express.js
    * **Database:** MySQL
    * **Password Hashing:** bcrypt
* **Frontend:**
    * HTML5
    * CSS3 (including SASS)
    * JavaScript
    * jQuery
* **Machine Learning (Core of `backend.py`):**
    * It is expected that a library such as **OpenCV** is used for video processing.
    * A deep learning framework like **TensorFlow**, **Keras**, or **PyTorch** would be used for the anomaly detection model.

---

## ⚙️ Setup and Installation

To get a local copy up and running, follow these steps.

### Prerequisites

* Python 3.8+
* Node.js 14+
* MySQL Server

### Quickstart (Run Locally)

1. **Clone & install Node dependencies**
   ```sh
   git clone https://github.com/R-Pranav4222/Bio-Signals.git
   cd Bio-Signals
   npm install
   ```

2. **Create and activate a Python virtual environment, then install deps**
   ```sh
   python -m venv .venv
   .venv\Scripts\activate
   pip install flask opencv-python imutils
   ```

3. **Create the MySQL database + table**
   ```sql
   CREATE DATABASE biosignals;
   USE biosignals;

   CREATE TABLE users (
     user_id VARCHAR(255) PRIMARY KEY,
     password VARCHAR(255) NOT NULL
   );
   ```

4. **Configure environment variables**

   Copy `.env.example` to `.env` in the project root, then edit values as needed:
   ```sh
   copy .env.example .env
   ```

   Your `.env` should look like:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=
   DB_DATABASE=biosignals
   PORT=3000
   ```

---

## ▶️ How to Run

1. **Start the Node.js API (login endpoint)**
   ```sh
   npm start
   ```
   Runs at `http://localhost:3000`.

2. **Start the Flask app (UI + video upload/anomaly detection)**
   ```sh
   python app.py
   ```
   Runs at `http://127.0.0.1:5000`.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📧 Contact

Project Link: [https://github.com/your-username/BioSignals](https://github.com/your-username/BioSignals)
