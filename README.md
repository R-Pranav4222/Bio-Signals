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

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.8+
* Node.js v14+
* MySQL Server

### Installation Steps

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/BioSignals.git](https://github.com/your-username/BioSignals.git)
    cd BioSignals
    ```

2.  **Setup the Node.js Backend:**
    Install the required npm packages.
    ```sh
    npm install
    ```

3.  **Setup the Python Backend:**
    It's recommended to use a virtual environment.
    ```sh
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

    # Install Python dependencies (Note: A requirements.txt should be created)
    # You will need to manually install Flask and other required libraries.
    pip install Flask mysql-connector-python numpy opencv-python tensorflow
    ```
    *(Note: The list of Python packages is inferred and may need adjustment.)*

4.  **Database Setup:**
    * Ensure your MySQL server is running.
    * Create a new database for the project.
        ```sql
        CREATE DATABASE biosignals;
        ```
    * You will need to create the necessary tables (e.g., for `users`, `videos`, `alerts`). An SQL script should be created for this.

5.  **Configure Environment Variables:**
    Create a `.env` file in the root directory by copying the example and fill in your database details.
    ```env
    # Environment variables for the application
    DB_HOST=localhost
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_DATABASE=biosignals
    PORT=3000
    ```

---

## ▶️ How to Run

1.  **Start the Node.js Server:**
    This server handles user interactions, API requests, and serves some parts of the application.
    ```sh
    node server.js
    ```

2.  **Start the Flask (Python) Server:**
    This server runs the main application logic, including video processing.
    ```sh
    flask run
    # or
    python app.py
    ```

3.  **Access the Application:**
    Open your web browser and navigate to `http://127.0.0.1:5000` (or the port specified by Flask). The Node.js server typically runs on the port defined in your `.env` file (e.g., 3000).

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
