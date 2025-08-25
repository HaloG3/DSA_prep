# lamda function : means function on the go [lamda variable: expression]

# filter : it takes a iterable and a function ; then gives us a sequence and can filter something form that iterable
# here we convert that sequence to list and print
nums =[3,4,5,5,6,7,2,3,]
evens = list (filter(lambda n : n%2 == 0, nums ))
print(evens)

doubles = list(map(lambda n: n*2, nums))
print (doubles)


 # map function: when changing any value we use it
 # IT TAKES THE value ; apply some operation and it takes a functions as input with a iterabl
 
