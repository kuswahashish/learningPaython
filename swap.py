n1 = input("Enter number 1 : ")
n2 = input("Enter number 2 : ")
n1,n2 = n2,n1
print("-: method 1 :-")
print('no1 : '+n1+'\nno2 : '+n2)
print("-: method 2 :-")
temp = n1
n1 = n2
n2 = temp
print('no1 : '+n1+'\nno2 : '+n2)
