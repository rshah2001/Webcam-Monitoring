# Motion Detection and Email Alert System

#### Description:  
This Python-based application detects motion through a webcam, captures frames of the detected motion, and sends an email notification with the captured image. It also includes a folder cleanup mechanism to manage saved images.

---

### Features
1. **Real-Time Motion Detection:**  
   Identifies motion by comparing frames and marking areas of activity with bounding boxes.
   
2. **Email Alerts:**  
   Sends an email with a snapshot of the detected motion for instant notification.

3. **Automated Cleanup:**  
   Automatically deletes saved images to manage storage efficiently.

---

### Setup Instructions
1. Install dependencies:  
   ```
   pip install opencv-python
   ```

2. Ensure you have a valid email setup in the `emailling` module for sending notifications.

3. Run the script:  
   ```
   python motion_detection.py
   ```

---

### Usage
1. Start the program and allow the webcam to initialize.  
2. The system will monitor for motion and create bounding boxes on detected activity.  
3. When motion is detected, an image is captured and saved in the `images` folder.  
4. Once motion stops, an email is sent with the captured image.  
5. To exit, press the `q` key.

---

### Modules Used
- OpenCV: For video capture and image processing.  
- Threading: For parallel execution of email and cleanup tasks.  
- Glob & OS: For managing image files.

---

### Important Notes
- Ensure the `images` directory exists in the project folder.  
- Configure the `emailling` module for your email server settings.  
- Adjust thresholds (e.g., contour area, frame thresholds) to suit your environment.

---
