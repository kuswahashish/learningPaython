message = input(">")
words = message.split(" ")
emojis = {
    ":)" : "Happy",
    ":(" : "SaD"
}
output = " "
for word in words :
    output += emojis.get(word,word) + " "
print(output)

