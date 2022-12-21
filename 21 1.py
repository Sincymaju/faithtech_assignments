
assigment 1
given a list L and an integer n,rotate L to the
right by n places
if n is negative rotate L to the left by n places
L=[1,2,3,4,5,6,7,8,9,10]
if n=3 then L=[8,9,10,1,2,3,4,5,6,7]
if n=-3 then L=[4,5,6,7,8,9,10,1,2,3]

def rotate (l,n):
    if n==0:
        return
    if n>0:
      for i in range(n):#n is 3
          x=L.pop()
          L.insert(0,x)#L=[8,9,10,1,2,3,4,5,6,7]
    else:
        for i in range(-n):
            x=L.pop(0)
            x=L.append(x)#L=[4,5,6,7,8,9,10,1,2,3]
        return
L=[1,2,3,4,5,6,7,8,9,10]
n=int(input('enter integer'))
rotate(L,n)
print(L)



#palidrome ,assignment 2
def is_palidrome(str):
    if str==str[::-1]:
        return True
    else:
        return False
n =input('enter string')
print(is_palidrome(n))

#assignment 3
def fibonacci(n):
    if n<=0:
        print('incorrect input')
        #first fibonacci number is zero
    elif n==1:
        return 0
#second fibonacci number is zero
    elif n==2:
       return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=int(input('enter an integer'))
for i in range(n+1):
    print(fibonacci(i))


# assignment 4
# number guessing game
import random
number = random.randint(1, 10)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))


# assignment 5
# calculate the number of digits and letters in an string
str = input("enter a string")
digit=letter=0
for ch in str:
   if ch.isdigit():
      digit=digit+1
   elif ch.isalpha():
      letter=letter+1
   else:
      pass
print("Letters:", letter)
print("Digits:", digit)