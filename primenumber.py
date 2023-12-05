def prime(rang_e):
   primenumbers =[]

for i in range(2,10001):

  isPrime = True
  for j in range(2,((rang_e+1)/2)+1):
    if (i%j ==0):
      isPrime = False
      break

  if(isPrime ==True):
      primenumbers.append(i)

print(primenumbers)