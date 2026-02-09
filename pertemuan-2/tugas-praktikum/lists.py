#PYTHONLIST
#untuk menyimpan beberapa item di satu variable dgn berbagai jenis tipe data 
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #len digunakan untuk melihat ada berapa item

mylist = ["apple", "banana", "cherry"]
print(type(mylist)) #melihat tipe data dari item

thislist = list(("apple", "banana", "cherry")) 
print(thislist) #bisa menggunakan list yang sudah tersedia

#ACCESS ITEMS
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #akan menampilan item index 1

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #akan menampilkan dari item terakhir

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #menampilkan dari indeks 2-4

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #menampilkan dari indeks 0-3

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #menampilkan dari indeks 2-habis

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #menampilkan dari indeks -4 sd -2

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") #memastikan apakah keyword ada pada list

#CHANGE ITEMS
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" #hanya mengganti item di indeks 1
print(thislist) 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] #mengganti pada indeks 1 dan 2 saja 
print(thislist)                                #lalu membiarkan yg lainnya

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] #hanya mengganti indeks 1 tapi dengan 2 item
print(thislist)                                #lalu indeks 2 akan dibiarkan begitu saja

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] #mengganti dua indeks dengan 1 item
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #memasukkan item baru pada posisi indeks kedua
print(thislist)

#ADD ITEMS
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") #ditambahkan pada posisi terakhir
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") #memasukkan item baru pada posisi spesifik
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #menambahkan isi list2 ke dalam isi list1
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) #menambakah tuple ka dalam list
print(thislist)

#REMOVE ITEMS
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #menghapus item dengan nama spesifik
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #menghapus berdasarkan index item
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop() #otomatis hapus last item
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0] #berdasarkan index. kalau ga ada [] ntar 
print(thislist) #listnya kehapus semua

thislist = ["apple", "banana", "cherry"]
thislist.clear() #clear it completely
print(thislist) 

#LOOP
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#SORT
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort() #disusun dari alphabet dan kapital dulu
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) #biar disusun dari huruf kecil
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort() #kecil besar
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True) #besar kecil
print(thislist)

def myfunc(n):
  return abs(n - 50) #customize mendekati 50 
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) 

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() #posisinya terbalik dari list awal
print(thislist)

#COPY
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#JOIN
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

"""
Method	    Description
append()   	Adds an element at the end of the list
clear()   	Removes all the elements from the list
copy()    	Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()  	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	  Adds an element at the specified position
pop()	      Removes the element at the specified position
remove()  	Removes the item with the specified value
reverse() 	Reverses the order of the list
sort()    	Sorts the list
"""