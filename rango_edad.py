x=int(input("dime tu edad:"))
def edad():
    if x<18:
        print("eres menor de edad")
    else:
        if x<35:
            print("eres adulto")
        else:
            if x<60:
                print("eres un adulto mayor")
            else:
                print("eres anciano")
edad()