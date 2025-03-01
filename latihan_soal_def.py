#1. Buat fungsi sapa() yang menampilkan pesan "Halo, selamat datang!".
def sapa() :
    print("Halo, Selamat datang!")

sapa()

#2. Buat fungsi tambah(a, b) yang mengembalikan hasil penjumlahan a + b.
def tambah (a, b):
    return a + b

hasil = tambah(3, 5)
print(hasil)

#3. Buat fungsi kali(a, b) yang mengembalikan hasil perkalian a * b.
def kali (a, b):
    return a * b

hasil = kali (5, 3)
print(hasil)

#4. Buat fungsi cek_genap(angka) yang mengembalikan True jika angka genap, dan False jika ganjil.
def cek_genap(angka):
    return angka % 2==0

print(cek_genap(5))
print(cek_genap(4))

#5. Buat fungsi hitung_diskon(harga, diskon) yang mengembalikan harga setelah diskon.
def hitung_diskon(harga,diskon):
    harga_setelah_diskon = harga - (harga * diskon / 100)
    return harga_setelah_diskon

print(hitung_diskon(10000, 20))
print(hitung_diskon(180000, 15))

#6. Buat fungsi sapa_nama(nama) yang menampilkan pesan "Halo, [nama]!".
def sapa_nama(nama):
    print(f"Halo, {nama}")

sapa_nama("ihir")

#7. Buat fungsi luas_persegi_panjang(panjang, lebar) yang mengembalikan luas persegi panjang.
def luas_persegi_panjang (panjang, lebar):
    return panjang * lebar

hasil = luas_persegi_panjang (3, 5)
print(hasil)    

#8. Buat fungsi volume_kubus(sisi) yang mengembalikan volume kubus.
def volume_kubus(sisi):
    return sisi ** 3

hasil = volume_kubus(5)
print(hasil)

#9. Buat fungsi rata_rata(a, b, c) yang mengembalikan rata-rata dari tiga angka.
def rata_rata (a, b, c) :
    return (a + b + c) / 3

hasil = rata_rata(3, 5, 7)
print(hasil)

#10. Buat fungsi konversi_celcius_ke_fahrenheit(celcius) yang mengembalikan suhu dalam Fahrenheit.
def konversi_celcius_ke_fahrenheit (celcius):
    return str ((celcius * 9 / 5) + 32) + " Fahrenheit" 

hasil = konversi_celcius_ke_fahrenheit (50)
print(hasil)

#str untuk menggabungkan huruf dan angka