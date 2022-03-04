import keyboard,pyautogui,time
spam = input('What do you want to spam to your friends >? ')
count = input('How much times before pressing enter>?')
print('got it my dude get ready for the fur 2 fly')
time.sleep(3)
counter = 0
while True:
    for letter in spam:
        try:
            keyboard.press(letter)
        except TypeError:
            print('dang it no work')
        time.sleep(.01)
    time.sleep(.1)
    keyboard.press('shift')
    keyboard.press('enter')
    keyboard.release('shift')
    counter += 1
    if counter > int(count):
        keyboard.press('enter')
