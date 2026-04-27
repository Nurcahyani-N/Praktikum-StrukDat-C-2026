from kurs import KURS

def idr_ke_luar(jumlah_idr, mata_uang):
    if mata_uang not in KURS:
        raise ValueError("Mata uang tidak tersedia.")
    return jumlah_idr / KURS[mata_uang]

def luar_ke_idr(jumlah_luar, mata_uang):
    if mata_uang not in KURS:
        raise ValueError("Mata uang tidak tersedia.")
    return jumlah_luar * KURS[mata_uang]

def konversi(jumlah, dari, ke):
    dari = dari.upper()
    ke = ke.upper()
    if dari == "IDR":
        return idr_ke_luar(jumlah, ke)
    elif ke == "IDR":
        return luar_ke_idr(jumlah, dari)
    else:
        # konversi via IDR
        idr = luar_ke_idr(jumlah, dari)
        return idr_ke_luar(idr, ke)