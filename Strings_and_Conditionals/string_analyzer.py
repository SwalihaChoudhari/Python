word=input("Enter your string: ")
if(len(word)<6):
    print("short string!")
else:
    print("long string!")
    
if word[0] in 'aeiou':
    print("Starts with a vowel!")
else:
    print("Doest'n start with vowel!")
    
print(f"Middle part: {word[1:-1]}")
   
    