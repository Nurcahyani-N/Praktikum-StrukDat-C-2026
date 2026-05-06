class Node:
    def __init__(self, id_buku, judul):
        # Menyimpan id_buku, judul, left (pointer ke anak kiri), dan right (pointer ke anak kanan)
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # BST memiliki satu atribut utama yaitu root
        self.root = None
        self._counter = 1 # Hanya digunakan untuk penomoran saat mencetak hasil In-Order

    def insert(self, id_buku, judul):
        # Menambahkan buku baru ke dalam BST sesuai aturan ID (Kiri < Parent < Kanan)
        if self.root is None:
            self.root = Node(id_buku, judul)
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
        else:
            self._insert_recursive(self.root, id_buku, judul)

    def _insert_recursive(self, current, id_buku, judul):
        if id_buku < current.id_buku:
            if current.left is None:
                current.left = Node(id_buku, judul)
                print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            else:
                self._insert_recursive(current.left, id_buku, judul)
        elif id_buku > current.id_buku:
            if current.right is None:
                current.right = Node(id_buku, judul)
                print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            else:
                self._insert_recursive(current.right, id_buku, judul)

    def traversal_inorder(self):
        # Menampilkan semua koleksi buku secara urut dari ID terkecil ke terbesar
        self._counter = 1
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(f"{self._counter}. {node.id_buku} - {node.judul}")
            self._counter += 1
            self._inorder_recursive(node.right)

    def search(self, id_buku):
        # Mencari apakah suatu buku ada di katalog berdasarkan ID-nya
        print(f"[SEARCH] Mencari ID {id_buku}... ", end="")
        result = self._search_recursive(self.root, id_buku)
        if result:
            print(f"Ditemukan! Judul: {result.judul}")
        else:
            print("Data tidak ditemukan.")

    def _search_recursive(self, current, id_buku):
        if current is None:
            return None
        if current.id_buku == id_buku:
            return current
        elif id_buku < current.id_buku:
            return self._search_recursive(current.left, id_buku)
        else:
            return self._search_recursive(current.right, id_buku)

    def get_min(self):
        # Menemukan buku dengan ID terkecil
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.id_buku

    def get_max(self):
        # Menemukan buku dengan ID terbesar
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.id_buku

    def height(self):
        # Menghitung total ketinggian (height) dari tree yang terbentuk
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        # Basis dari perhitungan height berdasarkan edge, root yang kosong bernilai -1
        if node is None:
            return -1
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))


# --- Skenario Pengujian ---
if __name__ == "__main__":
    print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
    print("=========================================")
    
    katalog = BST()
    
    # 1. Input Data
    katalog.insert(50, "Dasar Pemrograman")
    katalog.insert(30, "Struktur Data")
    katalog.insert(70, "Kecerdasan Buatan")
    katalog.insert(20, "Matematika Diskrit")
    katalog.insert(40, "Basis Data")
    katalog.insert(60, "Jaringan Komputer")
    katalog.insert(80, "Sistem Operasi")
    
    # 2. Cek Koleksi
    print("\n[INFO] Koleksi Buku (In-Order Traversal):")
    katalog.traversal_inorder()
    print("") # Menambah jarak untuk rapi
    
    # 3. Pencarian
    katalog.search(60)
    katalog.search(100)
    print("") # Menambah jarak
    
    # 4. Statistik
    print(f"[STATISTIK] ID Terkecil: {katalog.get_min()}")
    print(f"[STATISTIK] ID Terbesar: {katalog.get_max()}")
    
    # 5. Analisis Struktur
    print(f"[INFO] Tinggi (Height) Tree: {katalog.height()}")
    
    print("=========================================")
    print("Simulasi Selesai!")
    