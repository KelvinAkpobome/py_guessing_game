import random
def level(numb, guess, random_num):
    count = 0
    while count < guess:
        y = True


        while y == True:
            try:
                guessed_number = int(input('MAKE A GUESS: '))
                y = False
            except ValueError:
                print('Enter an integer or a number')
        count = count + 1
        if guessed_number in range(numb + 1):

            if guessed_number == guessed_number:
                if guessed_number == random_num:
                    print('You are correct')
                    break
                elif guessed_number != random_num:
                    print('You are wrong')
                    print(f'you may just have {guess-(count)} guess remaining now')
        else:


            count = count - 1
            print(f'Please can you Enter a number between 1 and {numb}')
            print(f'you have {guess-(count)} guess remaning now')
    else:
        print(f'THE NUMBER IS {random_num}')
        print('Sorry, you have to try again')



x=True
while x==True:
    difficulty=input("Enter a STAGE YOU WISH: ").lower()
    if difficulty=="easy":
        max_num=10
        rand_num=random.randint(1,max_num)
        guess=6
        level(max_num,guess,rand_num)
        x=False
    elif difficulty=="medium":
        max_num=20
        rand_num=random.randint(1,max_num)
        guess=4
        level(max_num,guess,rand_num)
        x=False
    elif difficulty=="hard":
        max_num=50
        rand_num=random.randint(1,max_num)
        guess=3
        level(max_num,guess,rand_num)
        x=False
    else:
        print("You are wrong, PLEASE TRY AGAIN")