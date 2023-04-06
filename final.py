import cv2
import streamlit as st

# Initialize OpenCV webcam capture outside of the function
cap = cv2.VideoCapture(0)

# Set webcam resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Add a button to start and stop the camera
start_button = st.button("Start Camera")
stop_button = st.button("Stop Camera")
flag = False

if start_button:
    flag = True

while flag:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break
        
    # Flip the frame horizontally for a selfie-view display
    frame = cv2.flip(frame, 1)
    
    # Display the frame in Streamlit
    st.image(frame, channels="BGR")
    

