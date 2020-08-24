msg = 'initial'
started = False
print("type help for help")
while msg.upper() != 'EXIT':
    msg = input(">")
    if msg.upper() == 'HELP':
        print("""START : to start car
STOP  : to stop car
EXIT  : to exit !""")
    elif msg.upper() == 'START':
        if started:
            print("Car is already Started.!")
        else:
           print("CAR is Started! Buckel Up")
           started = True
    elif msg.upper() == 'STOP':
            if not started:
                print("Car is already Stopped.!")
            else:
                print("CAR is Stopped..")
                started = False
    elif msg.upper() == 'EXIT':
            break
    else:
        print("Enter valid choice")

