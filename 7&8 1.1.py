
#STEPS IN PROGRAMMING

text = "0123456789abcdef"
print(text[5:9])
print(text[0:10])
print(text[:10])
# if you wanna start from 0 if you want you don't need to write it
print(text[10:])
print(text[-6:])

print(text[::2])
print(text[1::2])
print(text[::-1])
# last one it faster from while

# coomparing strings depend on the first letter in the word


print(dir(text))
help(text.isupper)
print(text.isupper())
print("ABC".isupper())
print(text.upper())
print(text.upper().isupper())

new_text = text.upper()
print(text, new_text)
print("banananananana".count("n"))
#count the number of n
print("banabanabanabanana".count("ana"))
print("banabanabanabanana".replace("ana","XXYYZ"))

sentence = "Hello, kind-sir; how may! I be of service today?"
punctuation = ".,;!?-"
for p in punctuation:
    sentence = sentence.replace(p, " ")
print(sentence)

print("this is a sentence and I want the words".split(" "))

text = "Bob goes to school. Bob likes to play tennis. I am friends with Bob. such a nice guy Bob is"
print(text.find("Bob"))
print(text.rfind("Bob"))
i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
       break
    print(i)
    i += 1

