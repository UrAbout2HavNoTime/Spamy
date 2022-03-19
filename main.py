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
            if letter in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '~', ':', '"', '{', '}', '|', '<', '>', '?', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']:
                pyautogui.press(letter)
            else:
                keyboard.press(letter)
                time.sleep(.01)
        except TypeError:
            print('dang it no work')
    keyboard.press('shift')
    keyboard.press('enter')
    keyboard.release('shift')
    counter += 1
    if counter > int(count):
        keyboard.press('enter')
        counter = 0
