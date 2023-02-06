import hashlib
m = hashlib.sha256()

def tryPass(word):
    newHash = hashlib.sha256(word.encode('utf-8')).hexdigest()
    for h in hashes:
        if newHash == h:
            for i in range(len(passwords)):
                if newHash == passwords[i][1]:
                    passwords[i][2] = word
                    hashes.remove(h)
                    print("Password found for", passwords[i][0], ": ", word, ". There are ", len(hashes), "passwords left to crack")
                    if len(hashes) == 0:
                        raise SystemExit()

# get hashes to crack
passwords = []
hashes = []
with open('passwords.txt') as file:
    for line in file:
        # if not '/' in line:
        parts = line.split(":")
        passwords.append([parts[0], parts[1], ""])
        hashes.append(parts[1])
        # print(passwords[len(passwords)-1])

print("There are", len(hashes), "passwords to crack")          

# seven-character password with capitalization and 1-digit appended
print("Rule 1: 7-character passwords that are capitalized with 1-digit appended")
with open('rockyou.txt', errors="ignore") as file:  # this feels like bad practice, but I don't know the encoding...
    for line in file:
        if len(line) == 7:  # this is 7 including the \n, so really 6
            attemptBase = line.capitalize().strip()
            for i in range(10):
                attemptNum = attemptBase + str(i)
                tryPass(attemptNum)

# eight-character password with one of *, ~, !, or # leading
print("Rule 2: 8-character password with at least one of *, ~, !, or # leading")
symbols = ["*", "~", "!", "#"]
with open('rockyou.txt', errors="ignore") as file:  # this feels like bad practice, but I don't know the encoding...
    for line in file:
        if len(line) == 2:  # I start here because this is one character
            attemptBase = line.strip()
            for sym1 in symbols:
                for sym2 in symbols:
                    for sym3 in symbols:
                        for sym4 in symbols:
                            for sym5 in symbols:
                                for sym6 in symbols:
                                    for sym7 in symbols:
                                        attemptNum = sym1 + sym2 + sym3 + sym4 + sym5 + sym6 + sym7 + attemptBase
                                        # print(attemptNum)
                                        tryPass(attemptNum)
            # input()
        if len(line) == 3:
            attemptBase = line.strip()
            for sym1 in symbols:
                for sym2 in symbols:
                    for sym3 in symbols:
                        for sym4 in symbols:
                            for sym5 in symbols:
                                for sym6 in symbols:
                                    attemptNum = sym1 + sym2 + sym3 + sym4 + sym5 + sym6 + attemptBase
                                    # print(attemptNum)
                                    tryPass(attemptNum)
            # input()
        if len(line) == 4:
            attemptBase = line.strip()
            for sym1 in symbols:
                for sym2 in symbols:
                    for sym3 in symbols:
                        for sym4 in symbols:
                            for sym5 in symbols:
                                attemptNum = sym1 + sym2 + sym3 + sym4 + sym5 + attemptBase
                                # print(attemptNum)
                                tryPass(attemptNum)
            # input()
        if len(line) == 5:
            attemptBase = line.strip()
            for sym1 in symbols:
                for sym2 in symbols:
                    for sym3 in symbols:
                        for sym4 in symbols:
                            attemptNum = sym1 + sym2 + sym3 + sym4 + attemptBase
                            # print(attemptNum)
                            tryPass(attemptNum)
            # input()
        if len(line) == 6:
            attemptBase = line.strip()
            for sym1 in symbols:
                for sym2 in symbols:
                    for sym3 in symbols:
                        attemptNum = sym1 + sym2 + sym3 + attemptBase
                        # print(attemptNum)
                        tryPass(attemptNum)
            # input()
        if len(line) == 7:
            attemptBase = line.strip()
            for sym1 in symbols:
                for sym2 in symbols:
                    attemptNum = sym1 + sym2 + attemptBase
                    # print(attemptNum)
                    tryPass(attemptNum)
            # input()
        if len(line) == 8:
            attemptBase = line.strip()
            for sym1 in symbols:
                attemptNum = sym1 + attemptBase
                # print(attemptNum)
                tryPass(attemptNum)
            # input()

print("Rule 3: 5-character password with the letter 'a' replace with '@' and 'l' replaced with '1'")
with open('rockyou.txt', errors="ignore") as file:  # this feels like bad practice, but I don't know the encoding...
    for line in file:
        if len(line) == 6:
            attemptBase = line.strip()
            attemptNum = attemptBase.replace("a", "@").replace("l", "1")
            # print(attemptNum)
            tryPass(attemptNum)
            # input()

print("Rule 4: Any password that is made with only digits and up to 6 digits in length")
with open('rockyou.txt', errors="ignore") as file:  # this feels like bad practice, but I don't know the encoding...
    #Tries 1 digit numbers
    for i1 in range(10):
        attemptNum = str(i1)
        # print(attemptNum)
        tryPass(attemptNum)
    # input()
    #Tries 2 digit numbers
    for i1 in range(10):
        for i2 in range(10):
            attemptNum = str(i1) + str(i2) 
            # print(attemptNum)
            tryPass(attemptNum)
    # input()
    # Tries 3 digit numbers
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                attemptNum = str(i1) + str(i2) + str(i3)
                # print(attemptNum)
                tryPass(attemptNum)
    # input()
    # Tries 4 digit numbers
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                for i4 in range (10):
                    attemptNum = str(i1) + str(i2) + str(i3) + str(i4) 
                    # print(attemptNum)
                    tryPass(attemptNum)
    # input()
    # Tries 5 digit numbers
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                for i4 in range (10):
                    for i5 in range(10):
                        attemptNum = str(i1) + str(i2) + str(i3) + str(i4) + str(i5)
                        # print(attemptNum)
                        tryPass(attemptNum)
    # input()
    # Tries 6 digit numbers
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                for i4 in range (10):
                    for i5 in range(10):
                        for i6 in range(10):
                            attemptNum = str(i1) + str(i2) + str(i3) + str(i4) + str(i5) + str(i6)
                            # print(attemptNum)
                            tryPass(attemptNum)
            # input()
                                    
print("Rule 5: Any unmodified word from the rockyou word list")
with open('rockyou.txt', errors="ignore") as file:  # this feels like bad practice, but I don't know the encoding...
    for line in file:
        if len(line) == 8:
            attemptBase = line.strip()
            # print(attemptBase)
            tryPass(attemptBase)
            # input()

print("Ending Attempts with", len(hashes), "left to crack")
for p in passwords:
    print(p[0], ":", p[2])

