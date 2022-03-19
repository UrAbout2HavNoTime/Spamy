import keyboard,time,pyautogui
spam = input('What do you want to spam to your friends >? ')
count = input('How much times before pressing enter>?')
print('Scipt ready and loaded now get on the chat in under 3 seconds')
time.sleep(4)
print('Here we go :D')
counter = 0
while True:
    for letter in spam:
        try:
            pyautogui.press(letter)
        except TypeError:
            print('dang it no work')

        time.sleep(.015)
    time.sleep(0.015)
    keyboard.press('shift')
    keyboard.press('enter')
    keyboard.release('shift')
    counter += 1
    if counter > int(count):
        keyboard.press('enter')
        counter = 0
