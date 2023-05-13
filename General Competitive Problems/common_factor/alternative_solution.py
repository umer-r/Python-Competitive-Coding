data  = input()
li = data.split()
   
a = int(li[0])
b = int(li[1])
   
def gcd(a, b):
    if (a == 0): 
        return b; 
    return gcd(b%a, a); 
   
if (a>0 and a<(10**12+1) and b>=1 and b<(10**12+1)):
    count = 1
    for i in range(2, gcd(a, b)+1):
        if a%i==0 and b%i==0:
            print(i)
            count = count+1
    print(count)