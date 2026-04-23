navigasi = []

# Push
navigasi.append('Google')
navigasi.append('Youtube')
navigasi.append('Instagram')
navigasi.append('Google Classroom')
navigasi.append('Soliter')
print("Riwayat Navigasi: ", navigasi)

# Peek
topElement = navigasi[-1]
print("Peek: ", topElement)

# Pop
poppedElement = navigasi.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", navigasi)

# isEmpty
isEmpty = not bool(navigasi)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(navigasi))