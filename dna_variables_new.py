#1list comprehensions
squares=[x**2 for x in range(21)]
print(squares)

#2 ########################################
filtered=[i for i in range(50)if i%2==0]
print(filtered)

filtered=[i for i in range(100)if i%7==0]
print(filtered)

filtered=[i for i in range(50)if i%9==5]
print(filtered)

#3check memory usage of your objects
import sys
r=range(0,1000)
print(sys.getsizeof(r))

#4 creat an actual list pf numbers from the same range
import sys
r=[x for x in range(0,1000)]
print(sys.getsizeof(r))

#in place variable swapping
a=34
b=7
c=8

a,b,c=c,a,b
print(a)
print(b)
print(c)

#string to title case

string="human dna is 99.9% similiar to each other"
print(string.title())

#split a string into list
string="A T C G T T C G A T"
print(string.split( ))

#creating a string from a list of string
string=["A","T","G","C","T","A"]
print("".join(string))

#reversing a string and list
string="ATTCGTCCGATGCUACGTACGT"
reversing=string[::-1]
print(reversing)

array=["A","T","G","C"]
reversing=array[::-1]
print(reversing)

#get unique elements from a list of string and variables
dna_string="ATTGCATTTACGTACUCATUCA"
print(set(dna_string))

numbers=[1,1,2,3,5,6,7,3,4,5,2,3,4,5,6,9,8,7,6,2,0,0]
print(set(numbers))

#finding out the most frequently occuring values string and variables
numbers=[1,2,3,5,6,7,1,2,3,4,5,5,7,8,9,0,0]
print(max(set(numbers),key=numbers.count))

dna_string="ATTGCTTACGTGACGTUCCGATACCCAGTCA"
print(max(set(dna_string),key=dna_string.count))

#division_operator
print(5/2)
print(5//2)





