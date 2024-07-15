started = False
while True:
    initial_command = input(">")
    if initial_command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit""")
    elif initial_command == "start":
        if started:
            print("car is already started...")
        else:
            started = True
            print("Car started... Ready to go! ")
    elif initial_command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif initial_command == "quit":
        break
    else:
        print("I don't understand that...")

#  if you start a loop with "While True" it will run undefinitely until you explicitly give a command to terminate loop