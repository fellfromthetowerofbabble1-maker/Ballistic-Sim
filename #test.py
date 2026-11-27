#test
c = 1
w = input("Who are you? ")
while not w and c < 6:
    w = input("Please try again, ")
    if not w:
        c = c +1
if w:
    print(f"Thank you, {w}. Have a wonderful day!")
else:
    print("You have reached the limit. Please try at a later time.")