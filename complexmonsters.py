complexmonsters = {}

def CreateDict():
    file = open("complexmonsters.txt", "r")
    lines = file.readlines()
    for x in lines:
        info = x.split(',')
        key = int(info[0])
        info.pop(0)
        values = info
        complexmonsters[key] = values

def SearchByID():
    ID = int(input("Input monster ID"))
    info = complexmonsters[ID]
    print("Name:", info[0])
    print("Origin:", info[1])
    print("Description:", info[2])
    print("Attack:", info[3])
    print("Magical Force:", info[4])
    print("Magical Defence:", info[5])
    print("Defence:", info[6])
    print("Intelligence:", info[7])
    print("Health:", info[8])
    print("Experience:", info[9])
    return(info)

def SearchByName():
    name = input("Input monster name (capitalised)")
    x = 1
    while True:
        if (complexmonsters[x])[0] == name:
            break
        else:
            x = x + 1
    info = complexmonsters[x]
    print("Name:", info[0])
    print("Origin:", info[1])
    print("Description:", info[2])
    print("Attack:", info[3])
    print("Magical Force:", info[4])
    print("Magical Defence:", info[5])
    print("Defence:", info[6])
    print("Intelligence:", info[7])
    print("Health:", info[8])
    print("Experience:", info[9])
    return(info)

def LoadMonster():
    selected = 'F'
    while selected == 'F':
        userinput = int(input("Would you like to search by ID [0] or Name [1]?"))
        if userinput == 0:
            info = SearchByID()
        elif userinput == 1:
            info = SearchByName()
        selected = input("Confirm Selection? T/F")
    print("Selection Confirmed for Player 1")
    print("")
    return(info)

def PlayerSelection():
    CreateDict()
    selection = LoadMonster()
    return(selection)

def RestoreHealth(P):
    if P[1] > 5:
        P[1] = P[1] - 5
        P[5] = P[5] + 5
    else:
        P[5] = P[5] + P[1]
        P[1] = 0
        print("Magical Force Depleted!!!")
    print("Health:", P[5])


def BoostDefense(P):
    if P[6] > 3:
        P[6] = P[6] - 3
        P[3] = P[3] + 3
    else:
        P[3] = P[3] + P[6]
        P[6] = 0
        print("Experience Depleted!!!")
    print("Defense:", P[3])

def BoostAttack(P):
    if P[6] > 3:
        P[6] = P[6] - 3
        P[0] = P[0] + 3
    else:
        P[0] = P[0] + P[6]
        P[6] = 0
        print("Experience Depleted!!!")
    print("Attack:", P[3])

def Attack(P, Q, QMD):
    AttackPower = int((P[0]/6)*(P[4]/10 + 1)) - int((QMD/5)*(Q[3]/10 + 1))
    Q[5] = Q[5] - AttackPower
    print("Player 1 attacks Player 2!! Player 2 Health:", Q[5])
    QMD = 0

def SetupDefense(P):
    print("You have", P[2], "magical defense remaining")
    amount = 999
    while amount > P[2] and amount > 0:
        amount = int(input("How much defense would you like to spend?"))
        if amount > P[2]:
            print("invalid: must be a positive number equal/smaller to", P[5])
    P[2] = P[2] - amount
    print("You have", P[2], "magical defense remaining. Current defense:", amount)
    return amount

def Turn(P, Q, PMD, QMD):
    seestats = input("Would you like to see your stats? T/F")
    if seestats == "T":
        print("Attack:", P[0])
        print("Magical Force:", P[1])
        print("Magical Defense:", P[2])
        print("Defense:", P[3])
        print("Intelligence:", P[4])
        print("Health:", P[5])
        print("Experience:", P[6])
    selection = int(input("Select: Attack [0], Restore Health [1], Boost Defense [2], Boost Attack [3], Setup Defense [4]"))
    if selection == 0:
        print("You have decided to attack!")
        Attack(P, Q, QMD)
    elif selection == 1:
        print("You have decided to restore health!")
        RestoreHealth(P)
    elif selection == 2:
        print("You have decided to boost defense!")
        BoostDefense(P)
    elif selection == 3:
        print("You have decided to boost attack power!")
        BoostAttack(P)
    elif selection == 4:
        print("You have decided to set up your defense!")
        PMD = SetupDefense(P)

def Play():
    Player1, Player2 = [], []
    Player1MD, Player2MD = 0,0
    print("Player 1 Selection:")
    Player1 = list(map(int,PlayerSelection()[3:]))
    print("Player 2 Selection:")
    Player2 = list(map(int, PlayerSelection()[3:]))
    while (Player1[5] > 0) and (Player2[5] > 0):
        print("Player 1 Turn:")
        Turn(Player1, Player2, Player1MD, Player2MD)
        print("")
        print("Player 2 Turn:")
        Turn(Player2, Player1, Player2MD, Player1MD)
        print("")
    if Player1[5] <= 0:
        print("Player 2 Wins!")
    else:
        print("Player 1 Wins!")

Play()
