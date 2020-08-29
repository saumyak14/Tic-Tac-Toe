import sys
b={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}

print("1|2|3")
print("-+-+-")
print("4|5|6")
print("-+-+-")
print("7|8|9")
print("-----------------")
player=1
moves=0
def count(a):
    if b[1]==b[2]==b[3]==a or b[4]==b[5]==b[6]==a or b[7]==b[8]==b[9]==a:
        return 1
    elif b[1]==b[4]==b[7]==a or b[2]==b[5]==b[8]==a or b[3]==b[6]==b[9]==a:
        return 1
    elif b[1]==b[5]==b[9]==a or b[3]==b[5]==b[7]==a:
        return 1
    else:
        return 0
n=0
while n<9:
    print(b[1]+"|"+b[2]+"|"+b[3])
    print("-+-+-")
    print(b[4]+"|"+b[5]+"|"+b[6])
    print("-+-+-")
    print(b[7]+"|"+b[8]+"|"+b[9])
    print("------------")
    while True:
        if player==1:
            p1=input("player 1:")
            if int(p1) in b and b[int(p1)]==" ":
                b[int(p1)]="X"
                c=count("X")
                if c==1:
                    print("player 1 win")
                    print("press 5 to exit and 6 to play again")
                    q = input()
                    if(q=="5"):
                       sys.exit()
                player=2
                break
            else:
                print("wrong choice,try again.")
                continue
        if player==2:
            p2=input("player 2:")
            if int(p2) in b and b[int(p2)]==" ":
                b[int(p2)]="O"
                c=count("O")
                if c==1:
                    print("player 2 wins")
                    print("press 5 to exit")
                    q = input()
                    if(q=="5"):
                       sys.exit()
                player=1
                break
            else:
                print("wrong choice,try again.")
                continue

    n+=1
else:
    print("Draw")
