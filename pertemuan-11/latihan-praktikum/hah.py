class Node:
    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None  # Pointer ke node selanjutnya

class Queue:
    def __init__(self):
        self.head = None      
        self.tail = None      
        self._size = 0        
        self.total_antrian = 0 

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        self.total_antrian += 1
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
        print(f'[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self.total_antrian}).')

    def dequeue(self):
        if self.is_empty():
            print('[PERINGATAN] Antrian kosong, tidak ada pasien untuk dipanggil.')
            return None
        
        temp = self.head
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
            
        self._size -= 1
        print(f'\n[PANGGIL] Dokter memanggil: {temp.nama} (keluhan: {temp.keluhan}).')
        return temp

    def peek(self):
        if self.is_empty():
            return None
        print(f'[PEEK] Pasien berikutnya: {self.head.nama} — {self.head.keluhan}.')
        return self.head
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print('\n[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.')

    def tampilkan_antrian(self):
        print('\n[ANTRIAN SAAT INI]')
        if self.is_empty():
            print('Antrian kosong.')
            return
        
        current = self.head
        no = 1
        while current:
            print(f'{no}. {current.nama} → {current.keluhan}.')
            current = current.next
            no += 1

print('====================================')
print('SISTEM ANTRIAN POLI UMUM')
print('RS Sehat Bersama')
print('====================================')

poli_umum = Queue()

status = 'YA, antrian masih kosong.' if poli_umum.is_empty() else 'TIDAK, ada pasien.'
print(f'[CEK] Apakah antrian kosong? → {status}\n')

poli_umum.enqueue('Budi', 'demam tinggi')
poli_umum.enqueue('Ani', 'batuk pilek')
poli_umum.enqueue('Citra', 'sakit kepala')

print(f'\n[INFO] Jumlah pasien menunggu: {poli_umum.size()} orang.')
poli_umum.peek()
poli_umum.dequeue()
poli_umum.enqueue('Dodi', 'nyeri perut')
poli_umum.tampilkan_antrian()
poli_umum.dequeue()
print(f'[INFO] Jumlah pasien masih menunggu: {poli_umum.size()} orang.')
poli_umum.clear()

print(f'[CEK] Apakah antrian kosong? → {status}')

print('====================================')
print('Simulasi Selesai!')
print('====================================')