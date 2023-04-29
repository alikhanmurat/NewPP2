import random

print ("Hello! What is your name?")
name = str(input())
txt1 = "Well, {}, I am thinking of a number between 1 and 20."
print (txt1.format(name))
x = random.randrange(1, 20)
y = int(input())
z = 0

while x != y:
    if y < x:
        print ("Your guess is too low.")
        print ("Take a guess.")
        z += 1
        y = int(input())
    elif y > x:
        print ("Your guess is too high.")
        print ("Take a guess.")
        z += 1
        y = int(input())
    else:
      break
txt2 = "Good job, {}! You guessed my number in {} guesses!"
print(txt2.format(name, z))
