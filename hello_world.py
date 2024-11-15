import streamlit as st
import random
import time

# Initialize counter for windows
window_count = 0
total_windows = 100  # Increase the total number of windows to cover the screen more effectively
interval = 0.1  # Faster interval for quicker pop-ups

# List of colors to apply to the text
text_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Function to create a new pop-up window
def create_window():
    global window_count
    if window_count < total_windows:  # Only create up to the specified number of windows
        # Create a container for the pop-up message
        message = "CHÚC MỪNG SINH NHẬT CHỊ GÁI!"
        
        # Random positioning across the screen for full screen effect
        screen_width = 800  # Example width of the web page
        screen_height = 600  # Example height of the web page
        x_position = random.randint(0, screen_width - 150)
        y_position = random.randint(0, screen_height - 100)
        
        # Set pop-up message with a color
        text_color = random.choice(text_colors)
        
        # Display the message as a pop-up
        st.markdown(f'<p style="font-size: 20px; color: {text_color}; background-color: pink; padding: 10px; border-radius: 10px; position: absolute; top: {y_position}px; left: {x_position}px;">{message}</p>', unsafe_allow_html=True)
        
        window_count += 1  # Increase the count of created windows

# Function to change the color of the button text each time it's pressed
def change_button_color():
    current_color = button_color
    # Find the next color in the list
    next_color = text_colors[(text_colors.index(current_color) + 1) % len(text_colors)]
    return next_color  # Change the color of the text on the button

# Main app setup
st.title("Popup Creator")

# Initialize button color
button_color = text_colors[0]

# Button to trigger the pop-ups continuously
if st.button("HÃY NHẤN VÀO ĐÂY", key="popup_button"):
    while window_count < total_windows:
        create_window()
        time.sleep(interval)  # Delay between each window creation
        
    # Change button color after pressing
    button_color = change_button_color()

    st.text(f"Button color: {button_color}")  # Display the current button color

