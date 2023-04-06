import cv2
import streamlit as st

# Initialize OpenCV webcam capture
cap = cv2.VideoCapture(0)

def main():
    st.title("Webcam Feed")
    
    while cap.isOpened():
        # Read frame from webcam
        ret, frame = cap.read()
        if not ret:
            break
            
        # Flip the frame horizontally for a selfie-view display
        frame = cv2.flip(frame, 1)
        
        # Display
