while True:
    while True:
     try:
        uyt =str(input("user name: "))
        break
     except ValueError:
          print("please try agen")

    while True:
      try:
       wlcom=float(input("passawaerd: "))
       break
      except ValueError:
       print("please try agen")
    if uyt in ("CH210000", "Ch210000", "cH210000", "ch210000"):
        result = True
    else:
        result = False

    while True:
           repeat = input("do you want sin up (yea/no): ")
           if repeat == "yes":
              print("thank for sin up")
           else:
               print("thank you")
           break
    if result == True:
        print("welcome to web")
    if result == False:
        print("please try agen")
    break