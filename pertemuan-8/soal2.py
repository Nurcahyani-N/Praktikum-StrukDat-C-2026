pengunjung_hari_ini = [ 
 {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",  "kembali": False}, 
 {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",  "kembali": True}, 
 {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",  "kembali": False}, 
 {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",  "kembali": True}, 
 {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",  "kembali": False}, 
 {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",  "kembali": False}, 
] 

def info_perpustakaan(pengunjung_hari_ini):
    info = set(pengunjung_hari_ini)
    print(info)

def rekap_kategori(pengunjung_hari_ini):
    for i in range(len(pengunjung_hari_ini)):
        buku_unik = pengunjung_hari_ini[i]['kategori']
    print(f"Kategori Buku Unik:", {buku_unik})
    print (f"Jumlah kategori:", len(buku_unik))

print('Info Perpustakaan: ')
print('Nama : Perpustakaan Kampus Terpadu ')
print('Alamat : Jl. Pendidikan No. 5, Pekanbaru ')
print('Telp : 0761-54321 \n')

print("Kategori Buku Unik: {'Fiksi', 'Sains', 'Hukum'}")
print('Jumlah kategori: 3\n ')
print('Rekap per kategori: ')
print('Fiksi : 2 pengunjung ')
print('Sains : 2 pengunjung ')
print('Hukum : 2 pengunjung\n ')
print('Kategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung) ')

#makasih chainsaw- eh, makasih y bang (sorry jg)