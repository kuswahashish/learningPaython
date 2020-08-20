weight = int(input("Enter your Weight : "))
wType = input("(L)bs or (K)g :")
if wType.upper() == 'L':
    weight = weight*0.45
    print("Your weight in KG is ",weight)
elif wType.upper() == 'K':
    weight = weight/0.45
    print("your weight is ",weight,"in Lbs")
else:
    print("Choose right option K or L")
