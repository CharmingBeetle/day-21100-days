print('Math Game')
print()
score = 0
mult = int(input('What are your multiples: '))
while True: 
  for i in range(1, 11):
    print(i, "X", mult, "= ")
    ans = int(input(' '))
    if ans == i*mult:
      print('Well done')
      score +=1
      continue
    else:
      print('Sorry thats incorrect.')
      continue
  if score ==10:
    print("Congrats! A perfect score! You scored 10 out of 10! 🎉")
    break
  else:
    print('You scored', score, 'out of 10.')
    exit()