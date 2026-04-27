# Data awal
data = [
    "Hani",
    "Halim",
    "Indra dan Ressy",
    "Icha",
    "Rama",
    "Ayah Sadiid",
    "Mak lung ",
    "Ibu Radit",
    "Pak lung",
    "Memel dan Jefri",
    "Teguh",
    "Tika",
    "Angah",
    "Pak lung",
    "Ika dan Rido",
    "Nisa",
    "Habib",
    "Ibu Nonon",
    "Dani",
    "Mia",
    "Faris",
    "Mama Elly",
    "Sadiid dan kia",
    "Rifa",
    "Rafi dan Wulan",
    "Tafrisyam",
    "Ibu Sadiid",
    "Mama Wiwik",
    "Haris",
    "Hafiz"
]

# Fungsi untuk menyesuaikan berdasarkan Juz 1
def set_juz1(nama, data):
    if nama not in data:
        print("Nama tidak ditemukan!")
        return data
    
    idx = data.index(nama)
    data_baru = data[idx:] + data[:idx]
    return data_baru

# Fungsi tampilkan
def tampilkan(data):
    for i, nama in enumerate(data, start=1):
        print(f"Juz {i}. {nama}")

# Input user
nama_juz1 = input("Siapa yang dapat Juz 1 hari ini? ")

# Proses
data = set_juz1(nama_juz1, data)

# Output
print("\nPembagian Khatam Alquran minggu ini:")
tampilkan(data)