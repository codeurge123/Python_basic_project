import random
n = random.randint(1,100)
a = -1
print("Welcome to Guess the Number Game")

guesses = 0

while(a != n):
    a = int(input("Guess the number : "))

    if(a < 0 or a > 100):
        print("Enter the number in range of 1 to 100")
        guesses -= 1 # Not count as number of guesses if number enter in out of range
    elif(a > n):
        print("Lower Number Please")
    else:
        print("Higher Number Please")
    
    guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempts ")

