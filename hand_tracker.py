# Import necessary libraries
# - mediapipe for hand tracking
# - numpy for image operations
# - cv2 for camera and drawing

# Define HandTracker class
    # Initialize hand tracker settings
        # Set mode, max hands, detection confidence, etc.
        # Setup MediaPipe hands and drawing utils

    # Detect hands in the image
        # Convert image to RGB
        # Process hands
        # If hands found, draw landmarks (if draw is True)
        # Return updated image

    # Get landmark positions for one hand
        # Get landmarks and convert to pixel coordinates
        # Return list of (x, y) positions

    # Check which fingers are up
        # Use landmark positions
        # Check thumb, index, middle, ring, pinky
        # Return list of True/False for each finger

# Define ColorRect class to create buttons
    # Initialize button with position, size, color, etc.
    # Draw the rectangle with optional text
    # Draw a colored box with transparency and text

