import sys
import math
import time

analysisIsOn = False
constantP = 3
constantQ = 5

#Checks if the number is prime or not
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    else:
        return True

#Calculates the GCD of a number 
def gcd(e,r):
    if r == 0:
        return e
    return gcd(r, e % r)

#Implements the euclidean algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a=r//e
            b = r%e
            r=e
            e=b
            print("%d = %d*(%d) + %d"%(r,a,e,b))
 
#Implements the extended euclidean algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
#Implements the multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. , where s = s(modr) beacuse s<0"%(s))
        elif(s>0):
            print("s=%d."%(s))
        return s%r

#Implements encryption procedure
def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    result = ""
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    for num in x:
        if(num == 400):
            result = result + " "
        else:
            result = result + chr(num+65)
    return result
     
 
#Implements decryption procedure
def decrypt(priv_key,c_text):
    txt =[]
    x=''
    m=0
    d,n=priv_key
    for c in c_text:
        if(c.isupper()):
            txt.append(ord(c)-65)
        elif(c.islower()):              
            txt.append(ord(c)-97)
        elif(c.isspace()):
            txt.append(400)
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x

# outputs data size to a file  
file1 = open("data.txt","a")#append mode 

for i in range(1,101):
    constantMessage = "abCem4771eabCem4771eabCem4771eabCem4771eabCem4771e"*i
    print("the message memory size is",str(sys.getsizeof(constantMessage))+ " bytes")
    file1.write(str(sys.getsizeof(constantMessage))+",") 
    #Implements the main procedure
    while True:
        if analysisIsOn:
            p=constantP
            q=constantQ
            start_time = time.time()
        else:
            print("")
            print("IMPLEMENTATION OF RSA ALGORITHM")
            print("-----------------------------------------------------")
             
            #Inputs prime numbers
            p = int(input("Enter a prime number for P: "))
            q = int(input("Enter a prime number for Q: "))
            print("-----------------------------------------------------")

            while(((is_prime(p)==False)or(is_prime(q)==False))):
                print("'p' and 'q' should be prime!")
                p = int(input("Enter a prime number for P: "))
                q = int(input("Enter a prime number for Q: "))
                print("-----------------------------------------------------")
             
        #Calculates RSA modulus
        n = q * p
         
        #Calculates eulers toitent
        r = (q-1)*(p-1)

        print("RSA Modulus(n) is:",n)
        print("Eulers Toitent(r) is:",r)
        print("-----------------------------------------------------")
         
        #Calculates the maximum coprime value of 'e' between (1-1000)
        for i in range(1,1000):
            if(gcd(i,r)==1):
                e=i
        print("e is: ",e)
        print("-----------------------------------------------------")
         
        #Calculates the private and public Keys
        print("EUCLID'S ALGORITHM:")
        eugcd(e,r)
        print("-----------------------------------------------------")

        print("EUCLID'S EXTENDED ALGORITHM:")
        d = mult_inv(e,r)
        print("The value of d is:",d)
        print("-----------------------------------------------------")
        public = (e,n)
        private = (d,n)
        print("Private Key is:",private)
        print("Public Key is:",public)
        print("-----------------------------------------------------")

#outputs response time to file
        if analysisIsOn:
            decrypt(public,constantMessage)
            file1.write(str(time.time() - start_time)+"\n") 
            print("--- %s seconds ---" % (time.time() - start_time))
            break;
        
        if not analysisIsOn:
            #Inputs the message
            message = input("Enter your (cipher/plain)text:")

            #Choosing between encryption or decryption
            mode = input("Enter 'e' for encryption or 'd' for decryption: ")

            #Prints output
            if(mode.lower()=='e'):
                print("Your encrypted message is:",encrypt(public,message))
            elif(mode.lower()=='d'):
                print("Your decrypted message is:",decrypt(private,message))
            else:
                print("Plase enter 'e' or 'd' only!")
            

