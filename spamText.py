import pyautogui, time
text = input("Enter the text you want to spam: ")
delay = int(input("Enter the delay you want between each message"))
while True:
    time.sleep(delay)
    pyautogui.typewrite(text)
    pyautogui.press("enter")