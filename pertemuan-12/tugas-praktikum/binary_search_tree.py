class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.kiri = None
        self.kanan = None

class BST:
    def __init__(self):
        self.root = None
        self._jumlah = 1
    
    def insert (self, id_buku, judul):
        if self.root is None:
            self.root = Node(id_buku, judul)
            print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}')
        else:
            self._insert_rekursif(self.root, id_buku, judul)

    def _insert_rekursif(self, current, id_buku, judul):
        if id_buku < current.id_buku:
            if current.kiri is None:
                current.kiri = Node (id_buku, judul)
                print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}')
            else:
                self._insert_rekursif(current.kiri, id_buku, judul)
        elif id_buku > current.id_buku:
            if current.kanan is None:
                current.kanan = Node (id_buku, judul)
                print(f'[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}')
            else:
                self._insert_rekursif(current.kanan, id_buku, judul)
    
    def traversal_inorder(self):
        print("\n[INFO] Koleksi Buku (In-Order Traversal):")
        self._tampil = 1
        self._inorder_rekursif(self.root)

    def _inorder_rekursif(self, current):
        if current:
            self._inorder_rekursif(current.kiri)
            print(f"{self._tampil}. {current.id_buku} - {current.judul}")
            self._tampil += 1
            self._inorder_rekursif(current.kanan)

    def search(self, id_buku):
        print(f"[SEARCH] Mencari ID {id_buku}...", end="")
        result = self._search_rekursif(self.root, id_buku)
        if result:
            print(f"Ditemukan! Judul: {result.judul}")
        else:
            print("Data tidak ditemukan.")

    def _search_rekursif(self, current, id_buku):
        if current is None:
            return None
        if current.id_buku == id_buku:
            return current
        elif id_buku < current.id_buku:
            return self._search_rekursif(current.kiri, id_buku)
        else:
            return self._search_rekursif(current.kanan, id_buku)
        
    def get_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.kiri is not None:
            current = current.kiri
        return current.id_buku
    
    def get_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.kanan is not None:
            current = current.kanan
        return current.id_buku
    
    def height(self):
        return self._height_rekursif(self.root)
    
    def _height_rekursif(self, node):
        if node is None:
            return -1
        return 1 + max(self._height_rekursif(node.kiri), self._height_rekursif(node.kanan))
    
katalog = BST()
print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print('=========================================')

katalog.insert(50, 'Dasar Pemograman')
katalog.insert(30, 'Struktur Data')
katalog.insert(70, 'Kecerdasan Buatan')
katalog.insert(20, 'Matematika Diskrit')
katalog.insert(40, 'Basis Data')
katalog.insert(60, 'Jaringan Komputer')
katalog.insert(80, 'Sistem Operasi')

katalog.traversal_inorder()


print(f'\n[STATISTIK] ID Terkecil: {katalog.get_min()}')
print(f'[STATISTIK] ID Terbesar: {katalog.get_max()}')
print(f'[INFO] Tinggi (Height) Tree: {katalog.height()}')

print('=========================================')
print('Simulasi Selesai!')