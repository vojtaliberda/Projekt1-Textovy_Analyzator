"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Vojtěch Liberda
email: vojtech.liberda@gmail.com
discord: vojtaliberda#0829
"""

# +------+-------------+
# | user |   password  |
# +------+-------------+
# | bob  |     123     |
# | ann  |   pass123   |
# | mike | password123 |
# | liz  |   pass123   |
# +------+-------------+

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

oddelovac = "-" * 50

prihlasovaci_udaje = {"bob" : "123", "ann" : "pass123", "mike" : "password", "liz" : "pass123"}

uzivatel = input("Username: ")

if uzivatel not in prihlasovaci_udaje:
    print("Unregistered user, terminating the program...")
    quit()

heslo = input("Password: ")

print(oddelovac)

if heslo == prihlasovaci_udaje.get(uzivatel):
    print(f"Welcome to the app, {uzivatel} \nWe have 3 texts to be analyzed.")
else:
    print("Unregistered user, terminating the program...")
    quit()

print(oddelovac)

cislo_textu = input("Enter a number between 1 and 3 to select: ")

if cislo_textu.isnumeric() == False:
    print("User did not pick from given texts, terminating the program...")
    quit()

if int(cislo_textu) <= 1 and int(cislo_textu) >= 3:
    print("User did not pick from given texts, terminating the program...")
    quit()

print(oddelovac)

for text in TEXTS:
    text_number = int(cislo_textu) - 1
    text = TEXTS[text_number]
    list_slov = text.split()
    pocet_slov = len(list_slov)
    print(f"There are {pocet_slov} words in selected text.")
    break

for text in TEXTS:
    text_number = int(cislo_textu) - 1
    text = TEXTS[text_number]
    list_slov = text.split()
    titlecase = 0
    for word in list_slov:
        if word.istitle():
            titlecase += 1
    print(f"There are {titlecase} titlecase words in selected text.")
    break

for text in TEXTS:
    text_number = int(cislo_textu) - 1
    text = TEXTS[text_number]
    list_slov = text.split()
    uppercase = 0
    for word in list_slov:
        if word.isupper() and word.isalpha():
            uppercase += 1
    print(f"There are {uppercase} uppercase words in selected text.")
    break

for text in TEXTS:
    text_number = int(cislo_textu) - 1
    text = TEXTS[text_number]
    list_slov = text.split()
    lowercase = 0
    for word in list_slov:
        if word.islower():
            lowercase += 1
    print(f"There are {lowercase} lowercase words in selected text.")
    break

for text in TEXTS:
    text_number = int(cislo_textu) - 1
    text = TEXTS[text_number]
    list_slov = text.split()
    numbers = 0
    for number in list_slov:
        if number.isnumeric():
            numbers += 1
    print(f"There are {numbers} numerical strings. ")
    break

for text in TEXTS:
    text_number = int(cislo_textu) - 1
    text = TEXTS[text_number]
    list_slov = text.split()
    numbers = []
    for number in list_slov:
        if number.isnumeric():
            numbers.append(int(number))
        total_sum = 0
        for num in numbers:
            total_sum += num
    print(f"The sum of all numbers in selected text is {total_sum}.")
    break

print(oddelovac)
le = "LEN"
oc = "OCCURENCES"
nr = "NR."
print(f"{le}|{oc.center(15)}|{nr}")
print(oddelovac)

text0 = str(TEXTS[int(cislo_textu) - 1])
char1 = ","
char2 = "."
text1 =  text0.replace(char1, "").replace(char2, "")

def zjisti_delku_slov(text, delka):
    words = text.split()
    count = 0
    for word in words:
        if len(word) == delka:
            count += 1
    return count

res1 = zjisti_delku_slov(text1, 1)
res2 = zjisti_delku_slov(text1, 2)
res3 = zjisti_delku_slov(text1, 3)
res4 = zjisti_delku_slov(text1, 4)
res5 = zjisti_delku_slov(text1, 5)
res6 = zjisti_delku_slov(text1, 6)
res7 = zjisti_delku_slov(text1, 7)
res8 = zjisti_delku_slov(text1, 8)
res9 = zjisti_delku_slov(text1, 9)
res10 = zjisti_delku_slov(text1, 10)
res11 = zjisti_delku_slov(text1, 11)

occ1 = int(res1) * "*"
occ2 = int(res2) * "*"
occ3 = int(res3) * "*"
occ4 = int(res4) * "*"
occ5 = int(res5) * "*"
occ6 = int(res6) * "*"
occ7 = int(res7) * "*"
occ8 = int(res8) * "*"
occ9 = int(res9) * "*"
occ10 = int(res10) * "*"
occ11 = int(res11) * "*"

print(f"{1:>3}|{occ1:<15}|{res1:<3}")
print(f"{2:>3}|{occ2:<15}|{res2:<3}")
print(f"{3:>3}|{occ3:<15}|{res3:<3}")
print(f"{4:>3}|{occ4:<15}|{res4:<3}")
print(f"{5:>3}|{occ5:<15}|{res5:<3}")
print(f"{6:>3}|{occ6:<15}|{res6:<3}")
print(f"{7:>3}|{occ7:<15}|{res7:<3}")
print(f"{8:>3}|{occ8:<15}|{res8:<3}")
print(f"{9:>3}|{occ9:<15}|{res9:<3}")
print(f"{10:>3}|{occ10:<15}|{res10:<3}")
print(f"{11:>3}|{occ11:<15}|{res11:<3}")