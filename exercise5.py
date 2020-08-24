#basic way to do print f using x and array values
# value = [5,2,5,2,2]
#
# for item in range(len(value)):
#     print('x'*value[item])

numbers = [5,2,5,2,2]
#change value to print different values

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output = output + 'x'
    print(output)