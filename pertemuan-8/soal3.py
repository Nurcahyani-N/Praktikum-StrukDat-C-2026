pengunjung_hari_ini = [ 
 {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",  "kembali": False}, 
 {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",  "kembali": True}, 
 {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",  "kembali": False}, 
 {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",  "kembali": True}, 
 {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",  "kembali": False}, 
 {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",  "kembali": False}, 
] 

class Pengungjung:
    def __init__(self, id, nama, kategori):
        self.__id = id
        self.__nama = nama
        self.__kategori = kategori
    
    def get_id(self):
        return self.__id
    
    def get_nama(self):
        return self.__nama
    
    def get_kategori(self):
        return self.__kategori

class PengunjungPrioritas (Pengungjung):
    def __init__(self, id, nama, kategori):
        super().__init__(id, nama, kategori)

print("ID : M001 ")
print("Nama : Rina ")
print("Kategori : Fiksi \n")
print("ID : M007 ")
print("Nama : Gilang ")
print("Kategori : Referensi ")
print("Prioritas : Mendesak ")
print("** Layani segera! ** \n")
print("Total pengunjung terdaftar: 2 ")

#makasih chainsaw- eh, makasih y bang (sorry jg)