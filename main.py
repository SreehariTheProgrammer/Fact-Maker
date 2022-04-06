import randfacts
from time import sleep as wait
import pyttsx3

r = pyttsx3.init()

x = randfacts.get_fact()
print(x)

r.say(x)
r.runAndWait()

while True:
    x2 = randfacts.get_fact() # Each loop will make a new random fact,
    # If I don't do it,
    #  the same fact in the variable "x"will be shown always
    wait(15)
    print(x2)
    r.say(x2)
    r.runAndWait()