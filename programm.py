import random


def main():
    print_header()
    main_loop()










def print_header():
    print('-------------------------------------')
    print('           EGGE QUEST')
    print('-------------------------------------')
    print()

def main_loop():
    enemies = []

    for x in range(5):
        level = random.randint(5, 13)
        enemies.append(f'Schülerin Jg. {level}')

    print(enemies)


    print("Du betritts die Schule und hast noch 12 Minuten bis du bei deinem Klassenraum sein musst")
    print("Du siehst einen Schüler (Jg.10).")

    while True:
        befehle = input("(S)prichst du ihn an, versuchst du, ihn zu (i)gnorieren oder siehst du dich (u)m? ")
        if befehle == "s":
            ansprechen()
        elif befehle == "u":
            umsehen(enemies)
        elif befehle == "i":
            ignorieren()
        elif befehle == "x":
            break

        else:
            print("FALSCH")




def ansprechen():
    print("Der Schüler ist sehr agressiv und beleidigt dich.")
    print("Du würfelst 22")
    print("Der Schüler (Jg.5) würfelt 7")
    print("Deine Antwort war sehr effektiv! Der Schüler (Jg.5) verschwindet.")

def ignorieren():
    print("Du ziehst deinen Kopf ein und läufst schnell weiter.")
    print("Der Schüler (Jg.10) bemerkt dich nicht einmal.")

def umsehen(enemies):
    print(" Du siehst dich um und siehst:")
    for enemy in enemies:
        print(enemy)




if __name__ == '__main__':
    main()









