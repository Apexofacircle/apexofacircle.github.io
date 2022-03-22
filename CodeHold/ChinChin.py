import random
              
_stillplaying = True

print("You go first")

while _stillplaying:

    _input = input("Pick a intiger between 0 and 4:")
    _inputthumbs = input("Pick 0,1 or 2 thumbs:")

    _rand = random.randrange(0,2)

    if int(_inputthumbs) + int(_rand)  == int(_input):
        print("YOU WIN")
        print("You picked " + str(_inputthumbs) +" thumbs")
        print("You guesed the number of thumbs to be " + str(_input))
        _stillplaying = False
        
    else:
        print()
        print("oponent picked: "  + str(_rand))
        print("Next round")
        print()
#enim turn
        _inputthumbs = input("Pick 0,1 or 2 thumbs:")
        _enimthumbs = random.randrange(0,2)
        _enimnum = random.randrange(0,4)

        if _enimthumbs + int(_inputthumbs) == _enimnum:
            print("You loose")
            print("enim picked " + str(_enimthumbs) + "thumbs")
            _stillplaying = False
        else:
            print("Next round")
            print()