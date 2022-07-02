import pyjokes
from ai import AI


alf = AI()

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    alf.say(funny)

command = ""
while True and command != "goodbye":
    command = alf.listen()
    print("Command was: ", command)

    if command == "tell me a joke":
        joke()



alf.say("Going to sleep")
