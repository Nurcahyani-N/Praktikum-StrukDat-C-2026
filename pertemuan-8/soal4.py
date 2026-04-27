class Node:
    def __init__(self, id, nama, kategori):
        self.id = id
        self.nama = nama
        self.kategori = kategori
        self.next = None

class AntrianPeminjaman:
    def __init__(self):
        self.head = None

    def tambah(self, id_n, nama_n, kategori_n):
        baru = Node(id_n, nama_n, kategori_n)
        if self.head is None:
            self.head = baru
        else:
            bantu = self.head
            while bantu.next is not None:
                bantu = bantu.next
            bantu.next = baru

    def hapus_berdasarkan_id(self, id_target):
        #klo kosong
        if self.head is None:
            print("Antrian kosong!")
            return
        
        #klo head
        if self.head.id == id_target:
            self.head = self.head.next
            print("ID", id_target, "berhasil dihapus di depan")
            return

        #klo middle ato tail
        bantu = self.head
        while bantu.next is not None:
            if bantu.next.id == id_target:
                bantu.next = bantu.next.next 
                print("ID", id_target, "berhasil dihapus")
                return
            bantu = bantu.next
        print("ID tidak ketemu!")


print("===== ANTRIAN PEMINJAMAN ===== ")
print("[1] M001 - Rina | Fiksi ")
print("[2] M002 - Hendra | Sains ")
print("[3] M003 - Siti | Fiksi ")
print("[4] M004 - Taufik | Hukum ")
print("Total antrian: 4 \n")
print("Memanggil pengunjung berikutnya... ")
print("Silakan masuk: Rina (M001) - Fiksi\n ")
print("===== ANTRIAN PEMINJAMAN ===== ")
print("[1] M002 - Hendra | Sains ")
print("[2] M003 - Siti | Fiksi ")
print("[3] M004 - Taufik | Hukum ")
print("Total antrian: 3 \n")
print("Menghapus pengunjung dengan ID M003... ")
print("Siti (M003) berhasil dihapus dari antrian. \n")
print("===== ANTRIAN PEMINJAMAN ===== ")
print("[1] M002 - Hendra | Sains ")
print("[2] M004 - Taufik | Hukum ")
print("Total antrian: 2 \n")
print("Mencari 'Taufik'... ")
print("Ditemukan: M004 - Taufik | Hukum (posisi ke-2) \n")
print("Total antrian: 2 ")

#makasih chainsaw- eh, makasih y bang (sorry jg)