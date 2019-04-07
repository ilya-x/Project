import random
sicret = random.randint(1,99)
guess = 0
tries = 0
while guess != sicret and tries <6:
    guess = int (input ("Твой вариант: "))
    if guess < sicret:
        print ("Это слишком мало")#'a'char "dsfsfsd"
    elif guess == sicret:
        break
    else:
        print ("Это слишком много")
    tries = tries + 1 #t+=1
    print("tries:", tries)
if guess == sicret:
    print (" Ты угадал", sicret)
else:
    print ("Ты проиграл")
    print ("Это число", sicret)
