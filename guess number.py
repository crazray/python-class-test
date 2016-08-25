from random import randint
num = randint (1,100)
print  ('welcome to guess number game!')
bingo = False
while bingo ==False:
  answer = int(input ('enter your number: '))
  if answer > num:
    print ('too big')
  elif answer < num:
    print ('too small')
  else:
    print ('bingo')
    break
print ('Congratulation!')
