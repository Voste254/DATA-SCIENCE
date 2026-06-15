def translate(phrase):
    vowels='aeiou'
    translation=''
    for letter in phrase:
        if letter.lower() in vowels:
            translation += 'k'
        else:
            translation += letter
    return translation
        
print(translate(input("Enter a phrase: ")))