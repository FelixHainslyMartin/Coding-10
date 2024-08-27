print ( "<<\t\t LATIHAN \t\t>>" )

# def cek_prima(angka):
#     if angka < 2:
#         return False
#     for i in range(2, int(angka ** 0.5) + 1):
#         if angka % i == 0:
#             return False
#     return True

# angka_minimal = 1
# angka_maksimal = 19

# daftar_bilangan = {}

# for angka in range(angka_minimal, angka_maksimal + 1):
#     if cek_prima(angka):
#         daftar_bilangan[angka] = 'Prima'
#     else:
#         daftar_bilangan[angka] = 'Komposit'

# print("Daftar Bilangan Prima dan Komposit antara", angka_minimal, "dan", angka_maksimal, ":")
# for angka, jenis in daftar_bilangan.items():
#     print(angka, "-", jenis)

def cek_prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

angka_minimal = 1
angka_maksimal = 19

list_prima = []
dict_komposit = {}

for angka in range(angka_minimal, angka_maksimal + 1):
    if cek_prima(angka):
        list_prima.append(angka)
    else:
        dict_komposit[angka] = 'Komposit'

print("List Bilangan Prima antara", angka_minimal, "dan", angka_maksimal, ":", list_prima)
print("Dictionary Bilangan Komposit antara", angka_minimal, "dan", angka_maksimal, ":", dict_komposit)