print("------------Tic Tac Toe-------------")
Row_1=[]
for index in range(3):
    element=(input("Enter the X or O:")).upper()
    if element not in {"X","O"}:
        break
    else:
        Row_1.append(element)
if len(Row_1)!=3:
    print("Game has ended. Please try again.")
else:
    print(Row_1)
    if Row_1==["X","X","X"]:
        print("X wins.")
    elif Row_1==["O","O","O"]:
        print("O wins.")
    else:
        Row_2=[]
        for index in range(3):
            element=(input("Enter the X or O:")).upper()
            if element not in {"X","O"}:
                break
            else:
                Row_2.append(element)
        if len(Row_2)!=3:
            print("Game has ended. Try again.")
        else:
            print(Row_1)
            print(Row_2)   
            if Row_2==["X","X","X"]:
                print("X wins.")
            elif Row_2==["O","O","O"]:
                print("O wins.")
            else:
                Row_3=[]
                element_1=(input("Enter the X or O:")).upper()
                if element_1 not in {"X","O"}:
                    print("Invalid entry.Game has ended. Try again.")
                else:
                    Row_3.append(element_1)
                    if element_1=="X" and Row_1[0]=="X" and Row_2[0]=="X":
                        print("X wins.")
                    elif element_1=="O" and Row_1[0]=="O" and Row_2[0]=="O":
                        print("O wins.")
                    else:
                        element_2=(input("Enter the X or O:")).upper()
                        if element_2 not in {"X","O"}:
                            print("Invalid entry. Game has ended. Try again.")
                        else:
                            Row_3.append(element_2)
                            if element_2=="X" and Row_1[1]=="X" and Row_2[1]=="X":
                                print("X wins.")
                            elif element_2=="O" and Row_1[1]=="O" and Row_2[1]=="O":
                                print("O wins.")
                            else:
                                element_3=(input("Enter the X or O:")).upper()
                                if element_3 not in {"X","O"}:
                                    print("Invalid entry. Game has ended. Try again.")
                                else:
                                    Row_3.append(element_3)
                                    print(Row_1)
                                    print(Row_2)
                                    print(Row_3)
                                    if Row_3==["X","X","X"]:
                                        print("X wins.")
                                    elif Row_3==["O","O","O"]:
                                        print("O wins.")    
                                    elif element_3=="X" and Row_1[2]=="X" and Row_2[2]=="X":
                                        print("X wins.")
                                    elif element_3=="O" and Row_1[2]=="O" and Row_2[2]=="O":
                                        print("O wins.")
                                    elif Row_1[0]=="X" and Row_2[1]=="X" and Row_3[2]=="X":
                                        print("X wins.")
                                    elif Row_1[0]=="O" and Row_2[1]=="O" and Row_3[2]=="O":
                                        print("O wins.")
                                    elif Row_1[2]=="X" and Row_2[1]=="X" and Row_3[0]=="X":
                                        print("X wins.")
                                    elif Row_1[2]=="O" and Row_2[1]=="O" and Row_3[0]=="O":
                                        print("O wins.")
                                    elif Row_1==["","",""] and Row_2==["","",""] and Row_3==["","",""]:
                                        print("It's an empty board. Try again.")
                                    else:
                                        print("It's a draw.")
