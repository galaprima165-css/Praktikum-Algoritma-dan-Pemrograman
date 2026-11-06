# 1. Konversi dari String ke Integer
str_angka = "70"
int_angka = int(str_angka)
print("Hasil Penjumlahan (70 + 50):", int_angka + 50)

# 2. Konversi dari Float ke Integer (Angka dibelakang koma dihilangkan)
ipk_float = 3.49
ipk_int = int(ipk_float)
print("Float ke Int:", ipk_int) # Output: 3

# 3. Konversi dari Integer ke String
tahun = 2027
pesan = "Tahun saat ini: " + str(tahun)
print(pesan)

# 4. Konversi dari List ke Set (Menghapus elemen duplikat)
daftar_buah = ["Apel", "semangka", "Pisang", "Pisang", "semangka"]
buah_unik = set(daftar_buah)
print("Buah Unik:", buah_unik)
