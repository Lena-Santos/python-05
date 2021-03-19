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
    print("Du betritts die Schule und hast noch 12 Minuten bis du bei deinem Klassenraum sein musst")
    print("Du siehst einen Schüler (Jg.10).")

    while True:
        befehle = input("(S)prichst du ihn an, versuchst du, ihn zu (i)gnorieren oder siehst du dich (u)m? ")
        if befehle == "s":
            ansprechen()
        elif befehle == "u":
            umsehen()
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

def umsehen():
    print(" Du siehst dich um und siehst:")
    print("Eine Schülerin(Jg.5)")
    print("Einen SChüler (Jg.7)")
    print("Eine Schülerin (Jg.8)")
    print("Eine Schülerin (Jg.10)")
    print("Einen Schüler (Jg.13)")



if __name__ == '__main__':
    main()









