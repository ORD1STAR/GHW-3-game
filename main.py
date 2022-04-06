import random, os
regen = 1
health = 100
max_health = 100
mana = 100
max_mana = 100
energy = 100
attack = 20
sword_ratio = 1.2
magic_ratio = 0
items = []
floor = 0
playing = True
named = False
randomNames = ["Bolam", "GHW", "Baba", "Terminator", "Lotfi"]

def stats():
    print("--------- Your stats --------")
    print("  * health: " + str(health) + "/" + str(max_health))
    print("  * Energy: " + str(energy) + "/100")
    print("  * Mana  : " + str(mana) + "/" + str(max_mana))
    
def e_stats(health):
    print("--------- Enemy stats --------")
    print("  * Health: " + str(health)) 

while not named:
    input("What's you name: ")
    name = randomNames[random.randint(0, 4)]
    named = (input("is your name: " + name + "? (yes/no) ") == "yes")
print(" ")
print(name, "is a superhero ... he is so strong ... WOW")
print("OH mY goD SoMeoNe juSt kiDnAPpeD his moM !!")
print("He have to save her !")
print("after 37 years of searching he found out that she was at the top of a long tower !!!!")
print("this tower contains 30 floors and every floor contains a certain amount of enemies")
print(" ")
print(" ")
input()

while playing:
    os.system("cls")
    floor += 1
    if floor==2: items.append("Sword");     print("========== You found a sword ==========")
    if floor==5: item.append("Magic Wand"); print("======= You found a Magic Wand =======")
    round = True
    
    e_health = 500 if floor==30 else 50 + 10*floor
    e_attack = 200 if floor==30 else 5 + 5*floor
    
    print(name, "entered the", floor, ("st" if floor ==
          1 else "nd" if floor == 2 else "rd" if floor == 3 else "th"), "floor !")
    print("there is 1 enemie !")
    while round:
        if e_health <= 0 : break
        stats()
        print(" ")
        e_stats(e_health)
            
        print(" ")
        print(" ")
        print("######### YOUR TURN ########")
        choix = []
        print("1- attack with your hands"); choix.append(1)
        if items.__contains__("Sword"):
            print(str(len(choix)+1)+"- attack with your sword")
            choix.append(2)
        if items.__contains__("Magic Wand"):
            print(str(len(choix)+1)+"- attack with your Magic Wand")
            choix.append(3)
        c = int(input("Votre choix: "))
        if c > len(choix): print("ERROR")
        elif c == 1:
            e_health -= attack
            print("You attacked using your hands")
        elif choix[c-1] == 2:
            if energy>=20:
                e_health -= attack*sword_ratio
                energy -= 20
                print("You attacked using your sword")
            else:
                print("OH NO ! you are so tired ! you dealt 0 Damages :((")
        elif choix[c-1] == 3:
            if mana >= 50:
                e_health -= 100 + magic_ratio
                mana -= 50
                print("You attacked using your magic wand !!!!!!!!**!**!*!*!**!*!!")
            else:
                print("OH NOOO ! you stick is not working :( you have no mana")
        choix.clear()
        print(" ")
        print(" ")
        print("######### THE ENEMY TURN ########")
        if e_health>0:
            print("The enemy attacked you")
            health -= e_attack
            if random.randint(0, 100)>=60 :
                health -= int(e_attack/2)
                print("!!!! WOW THAT WAS A STRONGER ONE !!!!!!!!!!!!!! :o")
        else:
            print("The enemy is dead yeyy")
        print(" ")
        print(" ")
        if health > 0:
            if max_health-health >= regen:
                health += regen
            else:
                health = max_health
        if health <=0 : 
            break
        
    if health>0: 
        if floor == 30:
            os.system("cls")
            print("YOU WOOOOONNNNN")
            print("you can take your mom's squeletton back home !!!!!")
            print("after 37 years...")
            break
        print("------ITEM SHOP-------")

        item_list = [
            "Regen Upgrade",
            "Health Upgrade",
            "Attack Upgrade",
            "Mana Upgrade",
            "Sword Upgrade",
            "Magic Wand Upgrade"
        ]
        i1 = item_list[random.randint(0, len(item_list)-1)]
        item_list.remove(i1)
        i2 = item_list[random.randint(0, len(item_list)-1)]

        shop = [i1, i2]
        item_c = []
        print("Choose your item:")
        print("1- Health potion (+100%)")
        item_c.append(0)
        if shop.__contains__("Regen Upgrade"):
            item_c.append(1)
            print(str(len(item_c)) + "- Regeneration Upgrade (+5 hp/round)")
        if shop.__contains__("Health Upgrade"):
            item_c.append(2)
            print(str(len(item_c)) + "- Health Upgrade (+10 hp of max health)")
        if shop.__contains__("Attack Upgrade"):
            item_c.append(3)
            print(str(len(item_c)) + "- Attack Upgrade (+5 attack damage)")
        if shop.__contains__("Mana Upgrade"):
            item_c.append(4)
            print(str(len(item_c)) + "- Mana Upgrade (+50 of max Mana)")
        if shop.__contains__("Sword Upgrade"):
            item_c.append(5)
            print(str(len(item_c)) + "- Sword Upgrade (+0.1%  of sword ratio)")
        if shop.__contains__("Magic Wand Upgrade"):
            item_c.append(6)
            print(str(len(item_c)) + "- Magic Wand Upgrade (+20 of Magic Wand damage)")
        m = int(input())

        if item_c[m-1] == 0:
            health = max_health
        if item_c[m-1] == 1:
            regen += 5
        if item_c[m-1] == 2:
            max_health += 10
        if item_c[m-1] == 3:
            attack += 5
        if item_c[m-1] == 4:
            mana += 50
        if item_c[m-1] == 5:
            sword_ratio += 0.1
        if item_c[m-1] == 6:
            magic_ratio += 20
        item_c.clear()
        mana = max_mana
        energy = 100
    else:
        floor = 0
        health = 100
        max_health = 100
        regen = 1
        mana = 100
        max_mana = 100
        energy = 100
        attack = 20
        sword_ratio = 1.2
        magic_ratio = 0
        items.clear()
        print("YOU DIED :o")
        input()