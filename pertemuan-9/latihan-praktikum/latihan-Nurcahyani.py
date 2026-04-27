#SOAL NOMOR 1
class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self, plat):
        baru = Node(plat)
        if not self.head:
            self.head = baru
            self.tail = baru
        else:
            baru.prev = self.tail
            self.tail.next = baru
            self.tail = baru

    def tampilkan_maju(self):
        curr = self.head
        while curr:
            print(curr.plat)
            curr = curr.next

    def tampilkan_mundur(self):
        curr = self.tail
        while curr:
            print(curr.plat)
            curr = curr.prev

    #SOAL NOMOR 2
    def hapus_kendaraan(self, plat):
        curr = self.head
        while curr:
            if curr.plat == plat:
                if curr == self.head:
                    self.head = curr.next
                    if self.head: self.head.prev = None
                elif curr == self.tail:
                    self.tail = curr.prev
                    if self.tail: self.tail.next = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                return
            curr = curr.next

#SOAL NOMOR 3
class NodeValet:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_giliran = None

    def tambah_petugas(self, nama):
        baru = NodeValet(nama)
        if not self.head:
            self.head = baru
            self.tail = baru
            baru.next = self.head 
            self.current_giliran = self.head 
        else:
            self.tail.next = baru
            self.tail = baru
            self.tail.next = self.head 

    def giliran_berikutnya(self, n):
        if not self.head:
            print("Petugas selanjutnya belum ditetapkan.")
            return
        for i in range(1, n + 1):
            print(f"Giliran {i}: {self.current_giliran.nama}")
            self.current_giliran = self.current_giliran.next

# --- UJI COBA SOAL 1 ---
nomor1 = DoubleLinkedList()
nomor1.tambah_kendaraan("B 1234 ABC")
nomor1.tambah_kendaraan("D 5678 XYZ")
nomor1.tambah_kendaraan("A 9999 TUV")

print("===NO.1===")
print("[Maju]")
nomor1.tampilkan_maju()
print("\n[Mundur]")
nomor1.tampilkan_mundur()

# --- UJI COBA SOAL 2 ---
nomor2 = DoubleLinkedList()
nomor2.tambah_kendaraan("B 1111 AA")
nomor2.tambah_kendaraan("D 2222 BB")
nomor2.tambah_kendaraan("A 3333 CC")
nomor2.tambah_kendaraan("B 4444 DD")

print("\n===NO.2===")
print("Sebelum:")
nomor2.tampilkan_maju()
nomor2.hapus_kendaraan("A 3333 CC")
print("\nSesudah:")
nomor2.tampilkan_maju()

# --- UJI COBA SOAL 3 ---
nomor3 = CircularLinkedList()
print("\n===SOAL 3===")
nomor3.tambah_petugas("Andi")
nomor3.tambah_petugas("Budi")
nomor3.tambah_petugas("Citra")
nomor3.tambah_petugas("Dewi")
nomor3.giliran_berikutnya(6)