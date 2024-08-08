command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started...")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car already stopped...")
        else:
            started = False
            print("Car stopped...")
    elif command == "help":
        print(
            """
type 'start' to start the car
type 'stop' to stop the car
type 'quit' to exit the program
            """
        )
    elif command == "quit":
        break
    else:
        print("I don't understand that...")
