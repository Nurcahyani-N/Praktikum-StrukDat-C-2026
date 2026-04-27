stok_barang = [15, 40, 30, 10, 25]
#temukan indeks
print(stok_barang[3])
stok_barang[3]=50

#tambahkan nilai
stok_barang.append (5)
stok_barang.sort (reverse=True)
print(stok_barang)
#total seluruh
print(sum(stok_barang))

#if
rata= sum(stok_barang)// len(stok_barang)
nilai= "stok aman" if rata >20 else "waspada"
print (nilai)