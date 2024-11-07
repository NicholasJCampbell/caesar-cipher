# add your code here
cypher = {"a": "f", "b": "g", "c": "h", "d": "i", 
          "e": "j", "f": "k", "g": "l", "h": "m",
          "i": "n", "j": "o", "k": "p", "l": "q",
          "m": "r", "n": "s", "o": "t", "p": "u",
          "q": "v", "r": "w", "s": "x", "t": "y",
          "u": "z", "v": "a", "w": "b", "x": "c", "y": "d", "z": "e"}

answer = input("Please enter a sentence: ")
answer = answer.lower()
print(answer)
code = ""
for letter in answer:
    if letter in cypher:
        letter = cypher[letter]
    # else
    #     print("Invalid format")
    code += letter
print("The encrypted sentence is: " + code)

