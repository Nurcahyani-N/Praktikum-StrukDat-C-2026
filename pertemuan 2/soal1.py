stock = [15,50,30,25,40]

stock.append(100)
print (stock)

stock.insert(2, 75)
print (stock)

stock.sort()
print (stock)

jumlah = 0
for x in range (len(stock)):
    jumlah += stock [x]
    rata = jumlah / (x+1)
    
    print (rata)

print (stock)