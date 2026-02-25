brg = ("B001", "laptop gaming",15000000)

print ("Harga barang: ", brg[2])

brg[2]= 14000000
print ("Harga barang: ", brg[2])
#terjadi error karena tuple tidak bisa diubah

(kode,nama,harga) = brg
print (kode)
print (nama)
print (harga)