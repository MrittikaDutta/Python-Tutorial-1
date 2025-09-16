while(True):
    try:
        userdata=int(input())
        num=int(userdata)
    except ValueError:
        print("Not a number.Try again")
    else:
        break
