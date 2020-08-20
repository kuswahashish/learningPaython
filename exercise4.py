name = input("Enter the name :")
if len(name) > 50:
    print("Name is too too big maximum 50 character")
elif len(name) <= 3:
    print("name is too short")
else:
    print(name+"\nname looks Good :) ")