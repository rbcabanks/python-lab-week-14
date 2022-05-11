

def menu():
    """
    prints the menu
    """
    print()
    print("---------------------------------------")
    print("Yoda's Wormhole Calculator")
    print("---------------------------------------")
    print("[w] calculates the number of wormholes")
    print("[q] quits")
    print("---------------------------------------")


def do_nothing():
    """
    does nothing
    """
    print("Does nothing...")


def wormhole(speed):
    num_of_wormholes=0
    if (speed<=0):
        num_of_wormholes=1
    else:
        num_of_wormholes=wormhole(speed-3)+wormhole(speed-17)

    return num_of_wormholes


def handle_wormhole_input():
    """
    handle the user input, then calls a recursive function to calculate wormholes
    """

    speed = input("Enter the speed of the starship: ")
    speed_val = int(speed)
    if speed_val < 0 or speed_val > 100:
        print()
        print("Yoda says there are no eta class fighters that travel at the speed of %d" % (
            speed_val))
        print()
    else:
        num = wormhole(speed_val)
        print()
        print(
            "Yoda says %d wormholes can be traversed at the speed of %d" % (num, speed_val))
        print()


def main():
    """
    main function for the app
    """

    # loop until user types q
    user_quit = False
    while (not user_quit):

        # menu
        menu()

        # get first character of input
        user_input = input("Enter a command: ")
        lower_input = user_input.lower()
        first_char = lower_input[0:1]
        print()

        # menu choices, use a switch-like if-elif control structure
        if first_char == 'q':
            print("Thank you for using Yoda's App!")
            user_quit = True
        elif first_char == 'w':
            # student should write code to
            # get the speed of the shuttle from the user, then call the function
            # "wormhole" to calculate the number of wormholes, then print the result
                
            handle_wormhole_input()

        else:
            print("ERROR: no such command")


main()
