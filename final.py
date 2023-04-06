import cv2
import streamlit as st

# Initialize OpenCV webcam capture
try:
    cap = cv2.VideoCapture(0)
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

def main():
    st.title("Webcam Feed")
    
    while cap.isOpened():
        # Read frame from webcam
        ret, frame = cap.read()
        if not ret:
            st.error("Error reading from webcam")
            break
            
        # Flip the frame horizontally for a selfie-view display
        frame = cv2.flip(frame, 1)
        
        # Display the frame in Streamlit
        st.image(frame, channels="BGR")

if __name__ == '__main__':
    main()
