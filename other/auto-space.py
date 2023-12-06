# This script doesn't work on Chromebooks because of the keyboard library and permissions.

import time
import keyboard

try:
    userNumber = input("How many times will spacebar be executed? \nAfter you input this number, the process will start in 5 seconds. \nPress esc or ctrl+c to stop.\nNumber of times: ")
    userNumber = int(userNumber)
    if userNumber < 1:
        raise ValueError("The number must be 1 or higher.")

    print("Starting in 5 seconds.  Get ready...")
    time.sleep(5)

    counter = 0
    while (counter < userNumber):
        # Check for esc key press
        if keyboard.is_pressed('esc'):
            print("Escape key pressed. Stopping...")
            break

        # Simulate space key press and short pause
        keyboard.send('space')
        time.sleep(.5)
        counter += 1
        print(counter)

except ValueError:
    print("Please enter a valid number.")
except KeyboardInterrupt:
    print("\nProcess interrupted by user.")
except Exception as e:
    print(f"An error occurred: {e}")

print("Process completed.")

