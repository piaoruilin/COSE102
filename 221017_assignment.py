#1번
count=0
a=int(input())
b=int(input())
while a<=b:
    a+=10000 #adding 10000 for every (2n+1)th day
    b*=1.02 #interest of 2% on b
    count+=1 #the next day
    if a>b:
        break
    a*=1.07 #interest of 7% on a for every (2n)th day
    b*=1.02 #continue with compound interest of 2%
    count+=1
print(count)

#2번
a=int(input())
count=0
for i in range(1,a): #to find factors of a
    if a%i==0: 
        count+=i #i acts as a counter for every increments of integer from 1.
if count==a: 
  print('YES') #once count reaches the initial value, there are conditional statements to determine YES and NO.
else:
  print('NO')

#3번
a=[]
k=0
a=input().split() #split input values
b=input()
c=input() 
n=int(input())
for i in range(len(a)):
    if a[i]==c: #go through the cycle of list a until the length of array a is reached.
        k=i 
print(a[(n%len(a)+k)%len(a)]) #print the name related to the length and k.

#4번 
a=list(input().split())
count=0
for i in range(len(a)):
    if a[i][-1]=='고' or a[i][-1]=='려' or a[i][-1]=='대': #-1 is used to obtain the last element of the array
        count+=1
print(count) #count determines the number of times the loop went through, aka the number of true statements in the split array.

#5번
a=input()
n=0
for i in range(len(a)):
    for j in range(len(a)): #double loop is used to determine the position of the letters in array a.
        if i!=j: #go through condition if the letters aren't equal.
            if a[i]==a[j]:
                n+=1 #add an increment to counter (n) once the same letter is obtained.
if n==0:
  print('YES')
else:
  print('NO') #print YES or NO accordingly.
