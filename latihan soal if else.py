#1. Soal: Cek Nilai Kelulusan
#Buat program untuk mengecek apakah seorang siswa lulus atau tidak berdasarkan nilai.
#Jika nilai >= 70, tampilkan "Lulus!".
#Jika tidak, tampilkan "Tidak Lulus.".
nilai = 70
if nilai >= 70 :
    print("Lulus!")
else : 
    print("Tidak lulus")

nilai = 65
if nilai >= 70 :
    print("Lulus!")
else : 
    print("Tidak lulus")    


#2. Soal: Cek Bilangan Genap/Ganjil
#Buat program untuk mengecek apakah suatu bilangan genap atau ganjil.
#Jika bilangan habis dibagi 2, tampilkan "Genap".
#Jika tidak, tampilkan "Ganjil"
bilangan = 56
if bilangan % 2 == 0 :
    print("Genap")
else : 
    print("Ganjil")

bilangan = 55
if bilangan % 2 == 0 :
    print("Genap")
else : 
    print("Ganjil")    


#3.Soal: Cek Diskon Belanja
#Buat program untuk mengecek apakah pelanggan dapat diskon berdasarkan total belanja.
#Jika total belanja > 150000, tampilkan "Anda dapat diskon 10%!".
#Jika tidak, tampilkan "Maaf, tidak ada diskon.".
total_belanja = 170000
if total_belanja > 150000 :
    print("Dapat diskon 10%!")
else :
    print("Maaf anda belum mendapat diskon")

total_belanja = 140.000
if total_belanja > 150000 :
    print("Dapat diskon 10%!")
else :
    print("Maaf anda belum mendapat diskon")


#4. Soal: Cek Usia
#Buat program untuk mengecek kategori usia seseorang.
#Jika usia < 17, tampilkan "Anda masih remaja.".
#Jika usia >= 17 dan < 60, tampilkan "Anda dewasa.".
#Jika usia >= 60, tampilkan "Anda lansia.".
usia = 15
if usia < 17 : 
    print("Anda masih remaja")
elif usia < 60 :
    print("Anda Dewasa")
else :
    print("Anda Lansia")

usia = 17
if usia < 17 : 
    print("Anda masih remaja")
elif usia < 60 :
    print("Anda Dewasa")
else :
    print("Anda Lansia")

usia = 70
if usia < 17 : 
    print("Anda masih remaja")
elif usia < 60 :
    print("Anda Dewasa")
else :
    print("Anda Lansia")


#5. Soal: Cek Password
#Buat program untuk mengecek apakah password yang dimasukkan benar.
#Jika password == "python123", tampilkan "Login berhasil!".
#Jika tidak, tampilkan "Password salah!".
password = "python123"
if password == "python123" :
    print("Login Berhasil")
else :
    print("Password salah")

password = "python321"
if password == "python123" :
    print("Login Berhasil")
else :
    print("Password salah")


#6.Soal: Cek Tahun Kabisat
#Buat program untuk mengecek apakah suatu tahun adalah tahun kabisat.
#Tahun kabisat adalah tahun yang habis dibagi 4, kecuali tahun yang habis dibagi 100 tetapi tidak habis dibagi 400.
tahun = 2024
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0) :
    print("kabisat")
else :
    print("tidak kabisat")

tahun = 2025
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0) :
    print("kabisat")
else :
    print("tidak kabisat")


#7. Soal: Cek Hari Kerja
#Buat program untuk mengecek apakah suatu hari adalah hari kerja atau akhir pekan.
#Jika hari == "Senin", "Selasa", "Rabu", "Kamis", atau "Jumat", tampilkan "Hari kerja.".
#Jika hari == "Sabtu" atau "Minggu", tampilkan "Akhir pekan.".
hari = "selasa"
if hari in ["senin", "selasa", "rabu", "kamis", "jumat"] :
    print("hari kerja")
else :
    print("libur")

hari = "sabtu"
if hari in ["senin", "selasa", "rabu", "kamis", "jumat"] :
    print("hari kerja")
else :
    print("libur")


#8. Soal: Cek Bilangan Positif/Negatif
#Buat program untuk mengecek apakah suatu bilangan positif, negatif, atau nol.
#Jika bilangan > 0, tampilkan "Positif".
#Jika bilangan < 0, tampilkan "Negatif".
#Jika bilangan == 0, tampilkan "Nol".
bilangan = 1
if bilangan > 0 :
    print("positif")
elif bilangan < 0 :
    print("negatif")
else :
    print("nol")

bilangan = -1
if bilangan > 0 :
    print("positif")
elif bilangan < 0 :
    print("negatif")
else :
    print("nol")

bilangan = 0
if bilangan > 0 :
    print("positif")
elif bilangan < 0 :
    print("negatif")
else :
    print("nol")


#9. Cek Panjang Password
#Buat program untuk mengecek apakah panjang password memenuhi syarat.
#Jika panjang password >= 8, tampilkan "Password valid!".
#Jika tidak, tampilkan "Password terlalu pendek!".
password = "aselole123"
if len (password) >= 8 :
    print("password valid")
else :
    print("password tidak valid")

password = "aselole"
if len (password) >= 8 :
    print("password valid")
else :
    print("password tidak valid")


#10.  Cek Nilai Huruf
#Buat program untuk mengkonversi nilai angka ke nilai huruf.
#Jika nilai >= 90, tampilkan "A".
#Jika nilai >= 80, tampilkan "B".
#Jika nilai >= 70, tampilkan "C".
#Jika nilai >= 60, tampilkan "D".
#Jika tidak, tampilkan "E".
nilai = 90
if nilai >= 90 :
    print("A")
elif nilai >= 80 :
    print("B")
elif nilai >= 70 :
    print("c")
elif nilai >= 60 :
    print("d")
else :
    print("tidak lulus")

nilai = 80
if nilai >= 90 :
    print("A")
elif nilai >= 80 :
    print("B")
elif nilai >= 70 :
    print("c")
elif nilai >= 60 :
    print("d")
else :
    print("tidak lulus")

nilai = 70
if nilai >= 90 :
    print("A")
elif nilai >= 80 :
    print("B")
elif nilai >= 70 :
    print("c")
elif nilai >= 60 :
    print("d")
else :
    print("tidak lulus")

nilai = 60
if nilai >= 90 :
    print("A")
elif nilai >= 80 :
    print("B")
elif nilai >= 70 :
    print("c")
elif nilai >= 60 :
    print("d")
else :
    print("tidak lulus")

nilai = 50
if nilai >= 90 :
    print("A")
elif nilai >= 80 :
    print("B")
elif nilai >= 70 :
    print("c")
elif nilai >= 60 :
    print("d")
else :
    print("tidak lulus")