# count_vowels_and_consonants
# Kutilgan natija: {"unli": 4, "undosh": 5}

def count_vowels_and_consonants(text: str) -> dict:
    txt = text.lower()
    vowel = 0
    cons = 0
    for letter in txt:
        if letter in "aeiou":
            vowel+=1
        elif letter.isalpha():
            cons+=1
    return {"Unli": vowel, "Undosh": cons}

print(count_vowels_and_consonants("Salom Dunyo!"))