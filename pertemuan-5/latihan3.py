ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

mahasiswa = ukm_coding - ukm_robotik
print(mahasiswa)

mahasiswa = ukm_coding | ukm_robotik
print(mahasiswa)

if "Andi" in ukm_robotik:
    print (True)
else:
    print (False)