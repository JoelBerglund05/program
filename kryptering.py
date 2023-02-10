deen = input("kreyptera eller dekryptera? k/d").lower()
inst = int(input("hoppa över seg").lower())
word = input("skriv ord").lower()
word = list(word)

b = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
encry = []

if inst > 25 or inst <= 0:
    inst = 1

if deen == "k":
    for i in word:
        if i == 'a':
            if b[0 + inst] > 25:
                encry.append(b[0 - inst])
            else:
                encry.append(b[0 + inst])
        elif i == 'b':
            if b[1 + inst] > 25:
                encry.append(b[1 - inst])
            else:
                encry.append(b[1 + inst])
        elif i == 'c':
            if b[2 + inst] > 25:
                encry.append(b[2 - inst])
            else:
                encry.append(b[2 + inst])
        elif i == 'd':
            if b[3 + inst] > 25:
                encry.append(b[3 - inst])
            else:
                encry.append(b[3 + inst])
        elif i == 'e':
            if b[4 + inst] > 25:
                encry.append(b[4 - inst])
            else:     
                encry.append(b[4 + inst])
        elif i == 'f':
            if b[5 + inst] > 25:
                encry.append(b[5 - inst])
            else:    
                encry.append(b[5 + inst])
        elif i == 'g':
            if b[6 + inst] > 25:
                encry.append(b[6 - inst])
            else:    
                encry.append(b[6 + inst])
        elif i == 'h':
            if b[7 + inst] > 25:
                encry.append(b[7 - inst])
            else:
                encry.append(b[7 + inst])
        elif i == 'i':
            if b[8 + inst] > 25:
                encry.append(b[8 - inst])
            else:
                encry.append(b[8 + inst])
        elif i == 'j':
            if b[9 + inst] > 25:
                encry.append(b[9 - inst])
            else:
                encry.append(b[9 + inst])
        elif i == 'k':
            if b[10 + inst] > 25:
                encry.append(b[10 - inst])
            else:
                encry.append(b[10 + inst])
        elif i == 'l':
            if b[12 + inst] > 25:
                encry.append(b[11 - inst])
            else:
                encry.append(b[11 + inst])
        elif i == 'm':
            if b[12 + inst] > 25:
                encry.append(b[12 - inst])
            else:
                encry.append(b[12 + inst])
        elif i == 'n':
            if b[13 + inst] > 25:
                encry.append(b[13 - inst])
            else:
                encry.append(b[13 + inst])
        elif i == 'o':
            if b[14 + inst] > 25:
                encry.append(b[14 - inst])
            else:
                encry.append(b[14 + inst])
        elif i == 'p':
            if b[15 + inst] > 25:
                encry.append(b[15 - inst])
            else:
                encry.append(b[15 + inst])
        elif i == 'q':
            if b[16 + inst] > 25:
                encry.append(b[16 - inst])
            else:
                encry.append(b[16 + inst])
        elif i == 'r':
            if b[17 + inst] > 25:
                encry.append(b[17 - inst])
            else:
                encry.append(b[17 + inst])
        elif i == 's':
            if b[18 + inst] > 25:
                encry.append(b[18 - inst])
            else:
                encry.append(b[18 + inst])
        elif i == 't':
            if b[19 + inst] > 25:
                encry.append(b[19 - inst])
            else:
                encry.append(b[19 + inst])
        elif i == 'u':
            if b[20 + inst] > 25:
                encry.append(b[20 - inst])
            else:
                encry.append(b[20 + inst])
        elif i == 'v':
            if b[21 + inst] > 25:
                encry.append(b[21 - inst])
            else:
                encry.append(b[21 + inst])
        elif i == 'w':
            if b[22 + inst] > 25:
                encry.append(b[22 - inst])
            else:
                encry.append(b[22 + inst])
        elif i == 'x':
            if b[23 + inst] > 25:
                encry.append(b[23 - inst])
            else:
                encry.append(b[23 + inst])
        elif i == 'y':
            if b[24 + inst] > 25:
                encry.append(b[24 - inst])
            else:
                encry.append(b[24 + inst])
        elif i == 'z':
            if b[25 + inst] > 25:
                encry.append(b[25 - inst])
            else:
                encry.append(b[25 + inst])
        else:
            encry.append(i)
elif deen == "d":
    for i in word:
        if i == b[1 + inst]:
            encry.append("a")
        elif i == b[2 + inst]:
            encry.append("b")
        elif i == b[3 + inst]:
            encry.append("c")
        elif i == b[4 + inst]:
            encry.append("d")
        elif i == b[5 + inst]:
            encry.append("e")
        elif i == b[6 + inst]:
            encry.append("f")
        elif i == b[7 + inst]:
            encry.append("g")
        elif i == b[8 + inst]:
            encry.append("h")
        elif i == b[9 + inst]:
            encry.append("i")
        elif i == b[10 + inst]:
            encry.append("j")
        elif i == b[11 + inst]:
            encry.append("k")
        elif i == b[12 + inst]:
            encry.append("l")
        elif i == b[13 + inst]:
            encry.append("m")
        elif i == b[14 + inst]:
            encry.append("n")
        elif i == b[15 + inst]:
            encry.append("o")
        elif i == b[16 + inst]:
            encry.append("p")
        elif i == b[17 + inst]:
            encry.append("q")
        elif i == b[18 + inst]:
            encry.append("r")
        elif i == b[19 + inst]:
            encry.append("s")
        elif i == b[20 + inst]:
            encry.append("t")
        elif i == b[21 + inst]:
            encry.append("u")
        elif i == b[22 + inst]:
            encry.append("v")
        elif i == b[23 + inst]:
            encry.append("w")
        elif i == b[24 + inst]:
            encry.append("x")
        elif i == b[25 + inst]:
            encry.append("y")
        elif i == b[0 + inst]:
            encry.append("z")
        else:
            encry.append(i)
else:
    print("error")
    deen = input("kreyptera eller dekryptera? k/d").lower()

for i in encry:
    print(i, end="")