import random
import math

userSelect , userScore , comScore = 0 , 0 , 0
while(userSelect != 3):
    comSelect = round(random.randint(1 , 2))
    userSelect = int(input("___|1|___ ___|2|___ payane bazy: 3 \n"))
    if userSelect == comSelect :
        userScore += 1
        print(f"Bordy! :)\nyour score : {userScore}, and cpu score : {comScore} \n**********")
    elif comSelect == 1 :
        if userSelect == 2 :
            comScore += 1
            print(f"Bakhty! :( \nyour score : {userScore}, and cpu score : {comScore} \n**********")
    elif comSelect == 2 :
        if userSelect == 1:
            comScore += 1
            print(f"Bakhty! :( \nyour score : {userScore}, and cpu score : {comScore} \n**********")
    elif userSelect == 3 :
        print(f"your score : {userScore}, and cpu score : {comScore}")
        break
    else :
        print("lotfan yek adade sahih vared konid.")
print(f"Bazt tamom shod. \n emtiaze shoma: {userScore}, emtiaze CPU : {comScore}")
if userScore == comScore :
    print("__^MOSAVY^__")
elif userScore < comScore : 
    print("__^SHOMA BAKHTID.^__")
elif userScore > comScore : 
    print("__^SHOMA BORDID.^__")