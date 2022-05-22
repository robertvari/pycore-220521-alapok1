status = 500

if status == 100:
    print("Continue")
elif status == 200:
    print("OK")
elif status == 203:
    print("Non-Authoritative Information")
elif status == 206:
    print("Partial Content")
elif status == 300:
    print("Multiple Choices")
elif status == 400:
    print("Bad Request")
else:
    print("This status is not handled.")
