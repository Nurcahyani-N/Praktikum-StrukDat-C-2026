data_aktivitas = {
  "p1": {"nama": "Diki", "poin":88},
  "p2": {"nama": "Aqul", "poin": 45},
  "p3": {"nama":"Abid", "poin": 92},
  "p4": {"nama":"Rehan", "poin": 70}
  }

for x in data_aktivitas.values():
  if x["poin"]>80:
    print(f"{x["nama"]} mendapatkan predikat gold")
  elif x["poin"]>=50 and x["poin"]<=80:
    print(f"{x["nama"]} mendapatkan predikat silver")
  elif x["poin"]<50:
    print(f"{x["nama"]} mendapatkan predikat bronze")
     
