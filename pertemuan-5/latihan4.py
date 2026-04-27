gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]

gudang_pc[1].update ({"kategori": "Aksesoris"})
print(gudang_pc)

gudang_pc.append({"item": "headset", "harga": 350000, "stok": 8})
print(gudang_pc[-1])

for x in gudang_pc:
 total_aset = x["harga"]*x["stok"]
 print (f"{x["item"]} | total aset {total_aset}")