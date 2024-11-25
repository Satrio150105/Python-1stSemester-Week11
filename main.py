import matematika

radius = int(input("Masukkan Bilangan: "))
luas_lingkaran = matematika.luas_lingkaran(radius)
print(f"Luas Lingkaran dengan radius {radius} adalah: {luas_lingkaran}")

sisi = int(input("Masukkan Bilangan: "))
luas_persegi = matematika.luas_persegi(sisi)
print(f"Luas Persegi dengan sisi {sisi} adalah: {luas_persegi}")