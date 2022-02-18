import random
a=1
while a < 2:
    print("Come one come all to the epic casino")
    print("777 is $1000")
    print("cherry cherry cherry is $800")
    print("Bar Bar Bar is $500")
    print("Space Space Space is $250")
# 7 has 5% chance
# cherry has 20% chance
# bar has 30% chance
# Space has 45% chance
    mylist=["7","cherry","cherry","cherry","cherry","bar","bar","bar","bar","bar","bar","space","space","space","space","space","space","space","space","space"]
    x=random.randrange(0,19)
    y=random.randrange(0,19)
    z=random.randrange(0,19)
    val1=mylist[x]
    val2=mylist[y]
    val3=mylist[z]
    if input("say /pull to pull the lever ")=="/pull":
        print(val1, val2, val3)
        if val1==val2==val3=="7":
            print("you made $1000")
        elif val1==val2==val3=="cherry":
            print("you made $800")
        elif val1==val2==val3=="bar":
            print("you made $800")
        elif val1==val2==val3=="space":
            print("you made $250")
        else:
            print("Scram you made no money!")
    else:
        print("Thats not a command")
        break
