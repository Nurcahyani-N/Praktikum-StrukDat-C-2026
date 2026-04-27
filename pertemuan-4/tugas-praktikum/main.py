from kurs import KURS
from konverter import konversi
from tabulate import tabulate

def tampilan_kurs():
    data = []
    for kode in ["USD", "EUR", "SGD", "JPY"]:
        nilai = KURS[kode]
        # format angka dengan pemisah ribuan titik
        nilai_format = f"{nilai:,.0f}".replace(",", ".")
        data.append([kode, nilai_format])

    print("=== KONVERTER MATA UANG ===")
    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid", stralign="center"))

def format_rp(angka):
    # Format Rp dengan titik ribuan, tanpa desimal
    return "Rp " + f"{angka:,.0f}".replace(",", ".")

def main():
    tampilan_kurs()

    mata_uang_tersedia = ["IDR", "USD", "EUR", "SGD", "JPY"]

    dari = input(f"\nDari ({'/'.join(mata_uang_tersedia)}): ").upper()
    while dari not in mata_uang_tersedia:
        print("Mata uang tidak tersedia. Coba lagi.")
        dari = input(f"Dari ({'/'.join(mata_uang_tersedia)}): ").upper()

    ke = input(f"Ke ({'/'.join(mata_uang_tersedia)}): ").upper()
    while ke not in mata_uang_tersedia:
        print("Mata uang tidak tersedia. Coba lagi.")
        ke = input(f"Ke ({'/'.join(mata_uang_tersedia)}): ").upper()

    while True:
        try:
            jumlah = int(input("Jumlah: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid.")

    hasil = konversi(jumlah, dari, ke)

    # Menampilkan hasil 
    if dari == "IDR":
        print(f"\n{format_rp(jumlah)} = {hasil:.2f} {ke}")
    elif ke == "IDR":
        print(f"\n{jumlah} {dari} = {format_rp(hasil)}")
    else:
        # Jika konversi antar valas, tampilkan 2 langkah
        dari_ke_idr = konversi(jumlah, dari, "IDR")
        hasil_final = konversi(dari_ke_idr, "IDR", ke)
        print(f"\n{jumlah} {dari} = {format_rp(dari_ke_idr)}")
        print(f"{format_rp(dari_ke_idr)} = {hasil_final:.2f} {ke}")

if __name__ == "__main__":
    main()