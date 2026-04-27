platNomor = []
platTanpaNomor = []
ganjil = []
genap = []

def pisah_plat ():
   for x in range (4):
      plat = input('Masukkan plat: ')
      platNomor.append(plat)

      platNoNomor = plat.split()
      platTanpaNomor.append(platNoNomor)
      baru = int(platTanpaNomor[x][1])
      platTanpaNomor[x][1] = baru
   print(platTanpaNomor)

   # Pisah
   for x in range (4):
      if (platTanpaNomor[x][1] % 2) == 0:
         genap.append(platTanpaNomor[x])
      else:
         ganjil.append(platTanpaNomor[x])

   print('Ganjil: ', ganjil)
   print('Genap: ', genap)

pisah_plat()