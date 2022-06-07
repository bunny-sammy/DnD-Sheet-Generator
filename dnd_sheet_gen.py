import random, webbrowser
from dnd_lists import * # importa informações do arquivo dnd_lists.py
from tkinter import Y

# Essa é sua ficha; ela será imprimida e salva em um .txt ao fim da execução
sheet = []

# Função para imprimir opções
def print_options (list):
    for i in range(0, len(list)):
        print(f'[{i}] {list[i]}')

# Função para escolher de uma array descondierando o random
def random_value (list):
    random_id = random.choice(range(1, len(list)))
    value = list[random_id]
    return value

# Função para especificar classe
def specify_type (list, type_text):
    if choose == True:
        print(f'Specify your {type_text}:')
        print_options(list)
        spec_selection = int(input())
    else:
        spec_selection = 0
    if spec_selection == 0:
        return random_value(list)
    else:
        return list[spec_selection]

# Função que calcula modificador de stat
def stat_modifier (stat):
    if stat < 1:
        return -5
    elif stat >= 2 and stat <= 3:
        return -4
    elif stat >= 4 and stat <= 5:
        return -3
    elif stat >= 6 and stat <= 7:
        return -2
    elif stat >= 8 and stat <= 9:
        return -1
    elif stat >= 10 and stat <= 11:
        return 0
    elif stat >= 12 and stat <= 13:
        return 1
    elif stat >= 14 and stat <= 15:
        return 2
    elif stat >= 16 and stat <= 17:
        return 3
    elif stat >= 18 and stat <= 19:
        return 4
    else:
        return 5

# Escolher entre random ou não
print("Would you like to choose your parameters?")
print("[Y]es, choose parameters.")
print("[N]o, randomize everything.")
str_selection = str(input())
if str_selection[0].lower() == 'y':
    choose = True
elif str_selection[0].lower() == 'n':
    choose = False
else:
    print("Error")#placeholder

# Escolha de gênero do personagem
gender_list = ['Random', 'Male', 'Female', 'Custom']
if choose == True:
    print("Choose your character's gender:")
    print_options(gender_list)
    selection = int(input())
else:
    selection = 0
if selection == 0:
    char_gender = random.choice(['Male', 'Female'])
elif selection == 3:
    char_gender = input('Specify your gender:')
else:
    char_gender = gender_list[selection]

# Escolher raça do personagem
if choose == True:
    print("Choose your character's race:")
    print_options(race_list)
    selection = int(input())
else:
    selection = 0
if selection == 0:
    selection = random_value(race_list)
if selection == 2:
    char_race = specify_type(Dra, 'race')
elif selection == 3:
    char_race = specify_type(Dwf, 'race')
elif selection == 4:
    char_race = specify_type(Elf, 'race')
elif selection == 5:
    char_race = specify_type(Gen, 'race')
elif selection == 6:
    char_race = specify_type(Gno, 'race')
elif selection == 9:
    char_race = specify_type(Hlf, 'race')
elif selection == 11:
    char_race = specify_type(Hum, 'race')
else:
    char_race = race_list[race_list.index(selection)]
race_id = race_list.index(char_race)

# Definição de linguagemm, peso e altura das raças
Aara = " Aarakocra,"
Drac = " Draconic,"
Dwarvi = " Dwarvish,"
Elvi = " Elvish,"
Gian = " Giant,"
Gnom = " Gnomish,"
Gobl = " Goblin,"
Hafl = " Hafling,"
Orc = " Orc,"
Aura = " Auran,"
Infe = " Infernal,"
Prim = " Primordial,"
Slang = [Aara, Dwarvi, Elvi, Gian, Gobl, Hafl, Orc]
Rlang2 = random.choice(Slang)
Hilang = ""
if race_id == 1:
    Hmo1 = random.randint(1, 4)
    Hmo2 = random.randint(1, 4)
    Hmod = Hmo1 + Hmo2
    Hbase = 58
    Wmo1 = random.randint(1, 10)
    Wmo2 = random.randint(1, 10)
    Wbase = 80
    Rlang = Aara + Aura
    Hilang = ""
if race_id == 2:
    Hmo1 = random.randint(1, 10)
    Hmo2 = random.randint(1, 10)
    Hmod = Hmo1 + Hmo2
    Hbase = 66
    Wmo1 = random.randint(1, 6)
    Wmo2 = random.randint(1, 6)
    Wbase = 175
    Rlang = Drac
    Hilang = ""
if race_id == 3:
    if char_race == "Mountain Dwarf":
        Hmo1 = random.randint(1, 4)
        Hmo2 = random.randint(1, 4)
        Hmod = Hmo1 + Hmo2
        Hbase = 48
        Wmo1 = random.randint(1, 6)
        Wmo2 = random.randint(1, 6)
        Wbase = 115
    elif char_race == "Hill Dwarf":
        Hmo1 = random.randint(1, 4)
        Hmo2 = random.randint(1, 4)
        Hbase = 44
        Wmo1 = random.randint(1, 6)
        Wmo2 = random.randint(1, 6)
        Wbase = 115
    Rlang = Dwarvi
    Hilang = ""
if race_id == 4:
    if char_race == "Dark Elf":
        Hmo1 = random.randint(1, 6)
        Hmo2 = random.randint(1, 6)
        Hbase = 44
        Wmo1 = random.randint(1, 6)
        Wmo2 = random.randint(1, 6)
        Wbase = 75
        Hilang = ""
    elif char_race == "Ground Elf":
        Hmo1 = random.randint(1, 4)
        Hmo2 = random.randint(1, 4)
        Hbase = 60
        Wmo1 = random.randint(1, 4)
        Wmo2 = random.randint(1, 4)
        Wbase = 100
        Hilang = ""
    elif char_race == "High Elf":
        Hmo1 = random.randint(1, 10)
        Hmo2 = random.randint(1, 10)
        Hbase = 90
        Wmo1 = random.randint(1, 4)
        Wmo2 = random.randint(1, 4)
        Wbase = 100
        Hilang = Rlang2
    elif char_race == "Wood Elf":
        Hmo1 = random.randint(1, 10)
        Hmo2 = random.randint(1, 10)
        Hbase = 90
        Wmo1 = random.randint(1, 4)
        Wmo2 = random.randint(1, 4)
        Wbase = 100
        Hilang = ""
    Rlang = Elvi
if race_id == 5:
    Hmo1 = random.randint(1, 10)
    Hmo2 = random.randint(1, 10)
    Hbase = 56
    Wmo1 = random.randint(1, 4)
    Wmo2 = random.randint(1, 4)
    Wbase = 110
    Rlang = Prim
    Hilang = ""
if race_id == 6:
    Hmo1 = random.randint(1, 4)
    Hmo2 = random.randint(1, 4)
    Hbase = 31
    Wmo1 = 1
    Wmo2 = 0
    Wbase = 35
    Rlang = Gnom
    Hilang = ""
if race_id == 7:
    Hmo1 = random.randint(1, 6)
    Hmo2 = random.randint(1, 6)
    Hbase = 84
    Wmo1 = random.randint(1, 4)
    Wmo2 = random.randint(1, 4)
    Wbase = 140
    Rlang = Gian
    Hilang = ""
if race_id == 8:
    Hmo1 = random.randint(1, 8)
    Hmo2 = random.randint(1, 8)
    Hbase = 57
    Wmo1 = random.randint(1, 4)
    Wmo2 = random.randint(1, 4)
    Wbase = 110
    Rlang = Elvi
    Hilang = ""
if race_id == 9:
    Hmo1 = random.randint(1, 6)
    Hmo2 = random.randint(1, 6)
    Hbase = 28
    Wmo1 = 1
    Wmo2 = 0
    Wbase = 35
    Rlang = Hafl
    Hilang = ""
if race_id == 10:
    Hmo1 = random.randint(1, 10)
    Hmo2 = random.randint(1, 10)
    Hbase = 58
    Wmo1 = random.randint(1, 6)
    Wmo2 = random.randint(1, 6)
    Wbase = 140
    Rlang = Orc
    Hilang = ""
if race_id == 11:
    Hmo1 = random.randint(1, 10)
    Hmo2 = random.randint(1, 10)
    Hbase = 56
    Wmo1 = random.randint(1, 4)
    Wmo2 = random.randint(1, 4)
    Wbase = 110
    Rlang = Rlang2
    Hilang = ""
if race_id == 12:
    Hmo1 = random.randint(1, 8)
    Hmo2 = random.randint(1, 8)
    Hbase = 57
    Wmo1 = random.randint(1, 4)
    Wmo2 = random.randint(1, 4)
    Wbase = 110
    Rlang = Infe
    Hilang = ""
if Rlang in Slang:
    Slang.remove(Rlang)
if Hilang in Slang:
    Slang.remove(Hilang)
Randl = random.choice(Slang)
Slang.remove(Randl)
Rand2 = random.choice(Slang)
Randl2 = str(Rand2)
Hmod = Hmo1 + Hmo2
Wmod = Wmo1 + Wmo2
tl = Hmod + Hbase
Wemod = Wmod*Hmod
hy = Wbase + Wemod
char_height = str(tl)
char_weight = str(hy)

# Escolha classe do personagem
if choose == True:
    print("Choose your character's class:")
    print_options(class_list)
    selection = int(input())
else:
    selection = 0
if selection == 0:
    char_class = random_value(class_list)
else:
    char_class = class_list[selection]
char_arc = specify_type(arc_list[class_list.index(char_class)], 'archetype')

# Escolha o background do personagem
if choose == True:
    print("Choose your character's background:")
    print_options(bg_list)
    selection = int(input())
else:
    selection = 0
if selection == 0:
    char_bg = random_value(bg_list)
else:
    char_bg = bg_list[selection]

sheet.append(f"You are a {char_gender.lower()} {char_race}.")
sheet.append(f"Your height is {char_height} inches.")
sheet.append(f"Your weight is {char_weight} pounds.")
sheet.append(f"Your class is {char_class}.")
sheet.append(f"Your class's archetype is {char_arc}.")
sheet.append(f"Your background is {char_bg}.")

# Calcular atributos
char_stats = []
stat_modifs = []
char_ac = 10
for i in range(0, 6):
    Value1 = random.randint(1, 6)
    Value2 = random.randint(1, 6)
    Value3 = random.randint(1, 6)
    Value4 = random.randint(1, 6)
    value = (Value1, Value2, Value3, Value4)
    Value = sorted(value)
    del Value[0]
    sum = 0
    for k in range(len(Value)):
        sum += Value[k]
    char_stats.append(int(sum))
    modif = stat_modifier(sum)
    if i == 1:# add dex modifier to ac
        char_ac += modif
    if modif >= 0:
        str_modif = '+' + str(modif)
    else:
        str_modif = str(modif)
    stat_modifs.append(str_modif)

sheet.append('')
sheet.append('Your stats:')
sheet.append(f'Strength: {char_stats[0]} ({stat_modifs[0]})')
sheet.append(f'Dexterity: {char_stats[1]} ({stat_modifs[1]})')
sheet.append(f'Constitution: {char_stats[2]} ({stat_modifs[2]})')
sheet.append(f'Intelligence: {char_stats[3]} ({stat_modifs[3]})')
sheet.append(f'Wisdom: {char_stats[4]} ({stat_modifs[4]})')
sheet.append(f'Charisma: {char_stats[5]} ({stat_modifs[5]})')
sheet.append(f'Your armor class: {char_ac}')
sheet.append('')

# Decidir coisas ideais, trinket e etc
if char_bg == "Acolyte":
    Trait = random.choice(Ac_PTR)
    Ideal = random.choice(Ac_IDE)
    Bond = random.choice(Ac_BND)
    Flaw = random.choice(Ac_FLA)
    BGL = 15
elif char_bg == "Charlatan":
    Scam = random.choice(Ch_SCM)
    Trait = random.choice(Ch_PTR)
    Ideal = random.choice(Ch_IDE)
    Bond = random.choice(Ch_BND)
    Flaw = random.choice(Ch_FLA)
    BGL = 15
    sheet.append("Your favored scam: " + Scam)
elif char_bg == "Criminal":
    Specialty = random.choice(Cr_SPC)
    Trait = random.choice(Cr_PTR)
    Ideal = random.choice(Cr_IDE)
    Bond = random.choice(Cr_BND)
    Flaw = random.choice(Cr_FLA)
    BGL = 15
    sheet.append("Your criminal speciality: " + Specialty)
elif char_bg == "Entertainer":
    Routine = random.choice(En_ROU)
    Trait = random.choice(En_PTR)
    Ideal = random.choice(En_IDE)
    Bond = random.choice(En_BND)
    Flaw = random.choice(En_FLA)
    BGL = 15
    sheet.append("Your entertainer routine: " + Routine)
elif char_bg == "Folk Hero":
    Event = random.choice(Fo_DEF)
    Trait = random.choice(Fo_PTR)
    Ideal = random.choice(Fo_IDE)
    Bond = random.choice(Fo_BND)
    Flaw = random.choice(Fo_FLA)
    BGL = 10
    sheet.append("Your defining event: " + Event)
elif char_bg == "Guild Artisan":
    Business = random.choice(Gu_BUS)
    Trait = random.choice(Gu_PTR)
    Ideal = random.choice(Gu_IDE)
    Bond = random.choice(Gu_BND)
    Flaw = random.choice(Gu_FLA)
    BGL = 15
    sheet.append("Your Guild Business: " + Business)
elif char_bg == "Hermit":
    Seclusion = random.choice(He_SEC)
    Trait = random.choice(He_PTR)
    Ideal = random.choice(He_IDE)
    Bond = random.choice(He_BND)
    Flaw = random.choice(He_FLA)
    BGL = 5
    sheet.append("Your life of seclusion: " + Seclusion)
elif char_bg == "Noble":
    Trait = random.choice(No_PTR)
    Ideal = random.choice(No_IDE)
    Bond = random.choice(No_BND)
    Flaw = random.choice(No_FLA)
    BGL = 25
elif char_bg == "Outlander":
    Origin = random.choice(Ou_ORI)
    Trait = random.choice(Ou_PTR)
    Ideal = random.choice(Ou_IDE)
    Bond = random.choice(Ou_BND)
    Flaw = random.choice(Ou_FLA)
    BGL = 10
    sheet.append("Your Outlander origin: " + Origin)
elif char_bg == "Sage":
    Specialty = random.choice(Sa_SPE)
    Trait = random.choice(Sa_PTR)
    Ideal = random.choice(Sa_IDE)
    Bond = random.choice(Sa_BND)
    Flaw = random.choice(Sa_FLA)
    BGL = 10
    sheet.append("Your Sage specialty: " + Specialty)
elif char_bg == "Sailor":
    Trait = random.choice(Sai_PTR)
    Ideal = random.choice(Sai_IDE)
    Bond = random.choice(Sai_BND)
    Flaw = random.choice(Sai_FLA)
    BGL = 10
elif char_bg == "Soldier":
    Specialty = random.choice(So_SPE)
    Trait = random.choice(So_PTR)
    Ideal = random.choice(So_IDE)
    Bond = random.choice(So_BND)
    Flaw = random.choice(So_FLA)
    BGL = 10
elif char_bg == "Urchin":
    Trait = random.choice(Ur_PTR)
    Ideal = random.choice(Ur_IDE)
    Flaw = random.choice(Ur_FLA)
    BGL = 10
Gold = str(BGL)
TRI = random.choice(Tri)
TRN = random.choice(Trn)
TRK = random.choice(Trk)
TRT = random.choice(Trt)
Trin = [TRI, TRN, TRK, TRT]
Trinket = random.choice(Trin)

sheet.append("You personality trait: " + Trait)
sheet.append("Your ideal: " + Ideal)
sheet.append("Your bond: " + Bond)
sheet.append("Your flaw: " + Flaw)
sheet.append("You speak Common," + Rlang + Hilang)
sheet.append("Your starting gold: " + Gold)
sheet.append("Your trinket: " + Trinket)

# Imprimir e salvar em .txt a ficha
text_file = open("sheet.txt", "w")
for i in range(0, len(sheet)):
    print(sheet[i])
    n = text_file.write(sheet[i] + '\n')
text_file.close()
input()
webbrowser.open("sheet.txt")