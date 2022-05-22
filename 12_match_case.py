status = 200

match status:
    case 100:
        print("Continue")
    case 200:
        print("OK")
    case 203:
        print("Non-Authoritative Information")
    case 206:
        print("Partial Content")
    case 300:
        print("Multiple Choices")
    case 400:
        print("Bad Request")
    case _:
        print("This status is not handled.")