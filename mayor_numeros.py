x = input("Dime un numero y te dire si es multiplo de tres:")
def multiplo():
    c= x%3
    if c<1:
        print("Es multiplo de tres")
    else:
        print("no es multiplo de tres")
multiplo()