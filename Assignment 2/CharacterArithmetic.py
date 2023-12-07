a = input("Enter a uppercase letter: ")
al = a.lower()

aord = ord(al)  # unicode value of the letter

aordplus = aord + 10

aordless = aord - 5

achr = chr(aordless)

print("Your final character is ", achr)


