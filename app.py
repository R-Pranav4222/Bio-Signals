from flask import Flask, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename  # Import secure_filename
import backend

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'mov', 'avi', 'mkv'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def process_video(file_path):
    print(f"Processing video: {file_path}")
    unusual_behavior_detected = backend.entry_exit(os.path.basename(file_path))  # Pass only the filename

    if unusual_behavior_detected:
        return render_template('alertDetected.html')
    else:
        return render_template('safe.html')
@app.route("/home",methods=["GET"])
def home():
    return render_template("index.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("upload_file"))
    return render_template("signin.html")
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'video' not in request.files:
            return redirect(request.url)
        file = request.files['video']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) 
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result_message = process_video(file_path)
            return result_message
    return render_template('adminDashboard.html')
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)
