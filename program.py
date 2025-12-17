
import random
randomnumber = random.randint(1,10000)
attempt_count = 0
print("Note!: Please Make the Number Under 100000 or else it will take toooo long!")
inp = int(input("Please input a number to see how long will it take to find it by just randomizing!:"))
while randomnumber != inp:
    print(f"#{attempt_count} Randomized Number is not {inp} it is {randomnumber}")
    attempt_count += 1
    randomnumber = random.randint(1,10000)
    if randomnumber == inp:
        print(f"#{attempt_count} Randomized Number is {inp}")
