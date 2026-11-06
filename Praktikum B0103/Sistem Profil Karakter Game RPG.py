# ============================================
# Profil Karakter Game
# ============================================

# 1. Membuat variabel profil karakter
nama_hero = "Arthena"                                   # String
level = 10                                              # Integer
hp = 850.5                                              # Float (Health Point)
is_alive = True                                         # Boolean
inventory = ["Pedang Baja", "Busur Elf", "Tombak Naga"] # List (minimal 3 senjata)
atribut = {"kekuatan": 80, "kelincahan": 65}            # Dictionary


def tampilkan_info():
    """Menampilkan seluruh informasi karakter."""
    print("Nama Hero :", nama_hero)
    print("Level     :", level)
    print("HP        :", hp)
    print("Hidup?    :", is_alive)
    print("Inventory :", inventory)
    print("Atribut   :", atribut)


# 2. Menampilkan seluruh informasi karakter
print("=== INFORMASI KARAKTER AWAL ===")
tampilkan_info()

# 3. Menampilkan tipe data masing-masing variabel
print("\n=== TIPE DATA VARIABEL ===")
print("nama_hero :", type(nama_hero))
print("level     :", type(level))
print("hp        :", type(hp))
print("is_alive  :", type(is_alive))
print("inventory :", type(inventory))
print("atribut   :", type(atribut))

# 4. Aksi karakter
# a. Karakter mendapatkan item baru
inventory.append("Ramuan HP")

# b. Karakter naik level: konversi ke float lalu tambah 0.5
level = float(level)
level = level + 0.5

# 5. Mencetak informasi terbaru
print("\n=== INFORMASI KARAKTER TERBARU ===")
tampilkan_info()

print("\nTipe data level sekarang :", type(level))