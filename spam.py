import pyautogui, time
spam = input("Enter what you want to spam: ")
time.sleep(5)
while True:
    pyautogui.typewrite(spam)
    pyautogui.press("enter")


