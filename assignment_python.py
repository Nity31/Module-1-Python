#1.sum of first n positive number
n=int(input("Enter a number n: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum,"is sum of n number")


#2.program to count occurrences of a substring in a string
n=input("Enter a String :")
print(n.count("n"))


#3.to count the occurrences of each word in a given sentence
s=input("Enter a string :")
words=s.split()
for i in words:
    count=0
    for j in words:
        if i == j:
            count=count+1
    print(i," : ",count)
        

'''4. program to get a single string from two given strings, separated by a space and swap the first
two characters of each string'''
s1="Python"
s2="Programminng"
print(s1+" "+s2)
list1=list(s1)
list2=list(s2)
list1[0],list1[1]=list1[1],list1[0]
list2[0],list2[1]=list2[1],list2[0]
new_list="".join(list1)
new_list2="".join(list2)
print(new_list)
print(new_list2)



'''5. program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead If the string length of the given
string is less than 3, leave it unchanged '''
s=input("Enter a string :")
if len(s)<3:
    print(s)
elif s.endswith("ing"):
    print(s+"ly")
else:
    print(s+"ing")


'''6.program to find the first appearance of the substring 'not' and 'poor' from a given string, if
'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string'''
s=input("Enter a string :")
not_pos=s.find("not")
poor_pos=s.find("poor")

if not_pos!= -1 and poor_pos!= -1 and not_pos<poor_pos:
    print(s[:not_pos]+"good"+s[poor_pos+4:])
else:
    print(s)

'''7.Program to find Greatest Common Divisor of two numbers.
For example, the GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14.'''
a=int(input("Enter a number"))
b=int(input("Enter b number"))
small= min(a,b)
for i in range(1,small+1):
    if a%i==0 and b%i==0:
        gcd=i
print("GCD of a and b is :",gcd)


'''8. program to check whether a list contains a sublist.'''
l=[1,2,3,4,[2,3,4],8,9]
for i in l:
    if type(i)==list:
        print("sublist is present")
else:
    print("sublist is not present")


'''9.program to find the second smallest number in a list'''
l=[233,344,212,422,323,333,221]
l.sort()
print(l)
print("Second smallest number is :",l[1])


'''10.Write a Python program to get unique values from a list'''
import random
l=[1,2,1.1,2.2,3,4,"python",True,9,4]
print(random.choice(l))



'''11.program to unzip a list of tuples into individual lists'''
t=[("a",3),("b",43),("c",333)]
d,e=zip(*t)
print(list(d))
print(list(e))


#12.program to convert a list of tuples into a dictionary
t=[("a",3),("b",2),("c",4)]
result=dict(t)
print(result)


#13.program to sort a dictionary (ascending /descending) by value
d={"Name":"Nity","RollNo":1,"Sub1":43,"Name2":"Vishwa","Rollno":2,"Sub1":54}
asc=dict(sorted(d.items()))
dec=dict(sorted(d.items(),reverse=True))
print("ascending:",asc)
print("descending:",dec)



'''14.program to find the highest 3 values in a dictionary'''
d={"orange":34,"apple":44,"Mango":45,"Litchi":46,"kiwi":99,"banana":86}
result=sorted(d.values(),reverse=True)
print(result)
print("Highest 3 values are :",result[:3])



'''15.Given a number n, write a python program to make and print the list of Fibonacci series up to n.
Input : n=7
Hint : first 7 numbers in the series
Expected output :
First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13'''
n=int(input("Enter a number :"))
a,b=0,1
print(a,end=" ")
for i in range(1,n+1):
    print(b,end=" ")
    a,b=b,a+b


'''16.Counting the frequencies in a list using a dictionary in Python.
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2'''
l=[1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]
dic={}
for i in l:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
for key , value in sorted (dic.items()):
    print(key," : ",value)


'''17.Write a python program using function to find the sum of odd series and even series
Odd series: 12/ 1! + 32/ 3! + 52/ 5!+……n
Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n'''
def factorial(num):
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    return fac
    
def even(n):
    total=0
    for i in range(2,n+1,2):
        total=total+(i**2)/factorial(i)
    print("Sum of even number:",total)

def odd(n):
    total=0
    for i in range(1,n+1,2):
        total=total+(i**2)/factorial(i)
    print("Sum of odd number :",total)
    

n=int(input("Enter a number :"))

even(n)
odd(n)


#19.Python function that takes a list and returns a new list with unique elements of the first list.
def l(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    else:
        return list2
list1=[1,2,3,4,5,1,3,4,5,7,6,9]
print("original List",list1)
print("Unique List",l(list1))
        
    
