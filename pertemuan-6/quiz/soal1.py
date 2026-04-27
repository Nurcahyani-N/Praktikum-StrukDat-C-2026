def registrasi_gadget (merk, tipe, harga, sn):
    if harga < 1000000:
        print('Harga harus di atas 1.000.000')
        return None
    if len(sn) < 5:
        print('Serial Number harus berisi minimal 5 karakter')
        return None
    return {
        'merk': merk,
        'tipe' : tipe,
        'harga' : harga,
        'sn' : sn,
        'status' : 'tersedia'
    }
    

inventaris = []
for i in range(3):
    merk= input('Masukkan merk gadget: ')
    tipe= input('Masukkan tipe gadget: ')
    harga= input('Masukkan harga gadget: ')
    sn= input('Masukkan SNsam gadget: ')
    gadget = registrasi_gadget(merk,tipe,harga,sn)
    if gadget:
        inventaris.apped(gadget)
    else:
        print('Registrasi gagal')

for item in inventaris:
    print(item)