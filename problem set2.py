
script = input("text:")
new_text = ""

vowels= ["a", "e", "i", "o", "u"]
for i in range(len(script)):
    if script[i].lower()not in vowels:
        new_text += script[i]

print(new_text)
