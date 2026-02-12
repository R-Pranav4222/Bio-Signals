import os
from imutils.video import VideoStream
import datetime
import imutils
import time
import cv2

def entry_exit(filename, min_area=500, max_occupancy_duration=10, max_changes=3):
    # Construct the full path for the video file in the 'uploads' directory
    video_path = os.path.join("uploads", filename)
    
    if filename == "" or not os.path.exists(video_path):
        print("ERROR: Please enter a valid video file path or live camera feed.")
        return False
    
    # Use live camera feed if 'webcam' is specified
    if filename.lower() == "webcam":
        vs = cv2.VideoCapture(0)
    else:
        vs = cv2.VideoCapture(video_path)

    if not vs.isOpened():
        print("ERROR: Could not open video source.")
        return False

    firstFrame = None
    prev = 0
    t1, t2 = None, None  
    entry_exit_changes = 0  
    unusual_behavior = False  

    while True:
        ret, frame = vs.read()
        if not ret:
            print("End of video stream or error reading frame.")
            break

        text = "Unoccupied"
        alert_text = ""  # To display alerts
        occupied = 0

        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if firstFrame is None:
            firstFrame = gray
            continue

        frameDelta = cv2.absdiff(firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            if cv2.contourArea(c) < min_area:
                continue

            if occupied == 0:
                occupied = 1

            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Occupied"

        cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        # Display alert if unusual behavior is detected
        if prev != occupied:
            entry_exit_changes += 1  
            if occupied == 0:
                t2 = datetime.datetime.now()
                alert_text = "Exit detected at: " + t2.strftime("%I:%M:%S%p")
                if t1 is not None and (t2 - t1).seconds > max_occupancy_duration:
                    alert_text = "ALERT: Prolonged occupancy detected!"
                    unusual_behavior = True
            else:
                t1 = datetime.datetime.now()
                alert_text = "Entry detected at: " + t1.strftime("%I:%M:%S%p")

        if entry_exit_changes > max_changes:
            alert_text = "ALERT: Too many entry/exit changes detected!"
            unusual_behavior = True
        
        # Display the alert text on the frame
        if alert_text:
            cv2.putText(frame, alert_text, (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        prev = occupied

    vs.release()
    # cv2.destroyAllWindows() # Not needed if no windows are shown

    return unusual_behavior
