# Main Program Starts

# Setup hand detector
# Setup camera
# Setup drawing canvas
# Setup color and tool buttons (pen, eraser, clear, etc.)
# Set default color and brush size

# Main loop
    # Read frame from camera
    # Flip image and resize

    # Detect hands and get finger positions
    # Check which fingers are up
        # Check if touching any button
        # If touching pen size button → change brush size
        # If touching color button → change brush color
        # If touching clear button → clear the canvas
        # If touching toggle buttons (pen/colors/board) → show/hide menus

        # If finger inside whiteboard:
            # Draw circle and line on canvas
            # Use eraser size if color is black

        # Reset previous drawing point

    # Draw all buttons and menus
    # Merge canvas with camera image
    # Show the result window
    # Break loop if 'q' key is pressed

# Release camera and close windows
