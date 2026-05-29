'''#1.sum of first n positive number
n=int(input("Enter a number n: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum,"is sum of n number")


#2.program to count occurrences of a substring in a string
n=input("Enter a String :")
print(n.count("n"))'''


'''#3.to count the occurrences of each word in a given sentence
s=input("Enter a string :")
words=s.split()
for i in words:
    count=0
    for j in words:
        if i == j:
            count=count+1
    print(i," : ",count)'''
        

'''4. program to get a single string from two given strings, separated by a space and swap the first
two characters of each string'''
'''s1="Python"
s2="Programminng"
print(s1+" "+s2)
list1=list(s1)
list2=list(s2)
list1[0],list1[1]=list1[1],list1[0]
list2[0],list2[1]=list2[1],list2[0]
new_list="".join(list1)
new_list2="".join(list2)
print(new_list)
print(new_list2)'''



'''5. program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead If the string length of the given
string is less than 3, leave it unchanged '''
'''s=input("Enter a string :")
if len(s)<3:
    print(s)
elif s.endswith("ing"):
    print(s+"ly")
else:
    print(s+"ing")'''


'''6.program to find the first appearance of the substring 'not' and 'poor' from a given string, if
'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
Return the resulting string'''
'''s=input("Enter a string :")
not_pos=s.find("not")
poor_pos=s.find("poor")

if not_pos!= -1 and poor_pos!= -1 and not_pos<poor_pos:
    print(s[:not_pos]+"good"+s[poor_pos+4:])
else:
    print(s)'''


'''8. program to check whether a list contains a sublist.'''
#l=[1,2,3,4,[5,6,7],8,9]
#print(l)

'''10.Write a Python program to get unique values from a list'''
'''import random
l=[1,2,1.1,2.2,3,4,"python",True,9,4]
print(random.choice(l))'''

'''#12.program to convert a list of tuples into a dictionary
t=[("a",3),("b",2),("c",4)]
result=dict(t)
print(result)'''


'''#13.program to sort a dictionary (ascending /descending) by value
d={"Name":"Nity","RollNo":1,"Sub1":43,"Name2":"Vishwa","Rollno":2,"Sub1":54}
asc=dict(sorted(d.items()))
dec=dict(sorted(d.items(),reverse=True))
print("ascending:",asc)
print("descending:",dec)'''




'''15.Given a number n, write a python program to make and print the list of Fibonacci series up to n.
Input : n=7
Hint : first 7 numbers in the series
Expected output :
First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13'''
'''n=int(input("Enter a number :"))
a,b=0,1
print(a,end=" ")
for i in range(1,n+1):
    print(b,end=" ")
    a,b=b,a+b'''


'''Counting the frequencies in a list using a dictionary in Python.
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2'''

l=[]
n=int(input("Enter a number :"))
l=n
print(l)
