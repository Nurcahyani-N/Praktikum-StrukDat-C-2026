pengunjung_hari_ini = [ 
 {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",  "kembali": False}, 
 {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",  "kembali": True}, 
 {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",  "kembali": False}, 
 {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",  "kembali": True}, 
 {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",  "kembali": False}, 
 {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",  "kembali": False}, 
] 

def tampilkan_pengunjung(pengunjung_hari_ini):
    print ('===== DATA PENGUNJUNG PERPUSTAKAAN =====')
    print("No | ID | Nama | Usia | Kategori | Status Kembali")
    print("---+------+--------+------+----------+---------------")
    for i in range(len(pengunjung_hari_ini)):
        id = pengunjung_hari_ini[i]['id']
        Nama = pengunjung_hari_ini[i]['nama']
        Usia = pengunjung_hari_ini[i]['usia']
        Kategori = pengunjung_hari_ini[i]['kategori']
        Status = pengunjung_hari_ini[i]['kembali']
        if "kembali" in pengunjung_hari_ini == True:
            Status = 'Sudah Kembali'
        else:
            Status = 'Belum Kembali'
        print(f"{i+1}. |{id}| {Nama}| {Usia} |{Kategori} |{Status}")

def filter_belum_kembali(pengunjung_hari_ini):
    print("\n===== PENGUNJUNG BELUM KEMBALI ===== ")
    for i in range(len(pengunjung_hari_ini)):
        Nama = pengunjung_hari_ini[i]['nama']
        print(f"{i+1}. {Nama}")
         
lama = [l for l in pengunjung_hari_ini if l['kembali'] == False]

def ambil_nama(item):
    return item['nama']
lama.sort(key=ambil_nama)

tampilkan_pengunjung(pengunjung_hari_ini)
filter_belum_kembali(lama)
print ('Total belum kembali:', len(lama), 'pengunjung')

#alhamdulillah 