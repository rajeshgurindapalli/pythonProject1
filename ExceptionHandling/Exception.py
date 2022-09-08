while True:
    try:
        n=int(input("please enter an integer"))
        break
    except IOError:
        print("not an integer! please again")
    except ValueError:
        print("not an integer! please again")
    else:
        print("you successfully entered an integer")
