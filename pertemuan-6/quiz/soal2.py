stok_gadget = [ 
 {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},  
 {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000}, 
 {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},  
 {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, ] 


def filter_harga(self, data, min_harga, max_harga): 
    min_harga = int(input ('Masukkan batas bawah harga: '))
    max_harga = int(input ('Masukkan batas atas harga:'))

