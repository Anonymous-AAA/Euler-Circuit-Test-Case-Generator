#! python3
# Euler circuit testcase generator
import random,sys,math
n=int(input("Enter number of vertices:"))
m=int(input("Enter number of edges:"))

# Uncomment the two lines below and comment the above two lines for direct terminal input.First argument is number of vertices , second number of edges

# n=int(sys.argv[1])
# m=int(sys.argv[2])


ch=0
k=[]
j=[]
Close={}
u=True

if n<3 or m<n or m>math.comb(n,2):
    print(f"Impossible to have an euler circuit with no repeating edges and self loops having {n} vertices and {m} edges.")
    sys.exit()

def euler():
    
    global k,Close,u
    euler_part()
    i=2
    while i<m-2:
        
        if len(Close[k[i-1]])<n:
            while u:
                ch=random.randrange(0,n)
                u=ch in Close[k[i-1]]
        else:
            euler_part()
            i=2
            continue
            
            
        # print(k)  
        # print(Close)
        u=True    
        Close[k[i-1]].append(ch)
        Close.setdefault(ch,[ch])
        Close[ch].append(k[i-1])
        k.append(ch)
        i+=1

   

def after_euler():
    global k,Close,u
    while u:
            if len(set().union(Close[k[m-3]],[k[0]]))<n:
                ch=random.randrange(0,n)
                u=ch in Close[k[m-3]] or ch==k[0]
            else:
                euler()


    Close[k[m-3]].append(ch)
    Close.setdefault(ch,[ch])
    Close[ch].append(k[m-3])
    k.append(ch)


    u=True

    # print(k)  
    # print(Close)


def euler_part():
    global k,Close,u
    ch=random.randrange(0,n)
    
    k=[ch]
    Close={}
    while(ch==k[0]):
        ch=random.randrange(0,n)
    k.append(ch)
    
    
    Close[k[0]]=[k[1],k[0]]
    Close[k[1]]=[k[0],k[1]]
    u=True




euler()
after_euler()


while u:
        if len(set().union(Close[k[m-2]],Close[k[0]]))<n:
            ch=random.randrange(0,n)
            u=ch in Close[k[m-2]] or ch in Close[k[0]]
        else:
            euler()
            after_euler()

        

# print(k)  
# print(Close)
k.append(ch)
k.append(k[0])
# print(k)  
# print(Close)

for i in range(m):
    j.append([k[i],k[i+1]])
    random.shuffle(j[i])


random.shuffle(j)

print(n)
print(m)

for i in j:
    print(f"{i[0]} {i[1]}")



print("\n\n\nOne of the possible outputs:")

for i in range(m):
    print(f"{k[i]} {k[i+1]}")






