import pyautogui
import time

# Get the message and count from the user
msg = input("Enter the message: ")
n = int(input("How many times?: "))
delay = float(input("Delay between messages (seconds): "))

# Countdown before starting, so you can click the input field
print("Bot starting in...")
count = 5
while count != 0:
    print(count)
    time.sleep(1)
    count -= 1
print("Fire in the hole!!!")

# Loop to type and send the message
for i in range(n):
    pyautogui.typewrite(msg)
    pyautogui.press("enter")
    time.sleep(delay)   # delay added here
