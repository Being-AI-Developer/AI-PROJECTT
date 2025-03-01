def hitung_diskon (harga, diskon) :
    return harga - (harga * diskon)
harga_asli = 100000
diskon = 0.2
harga_akhir = hitung_diskon (harga_asli, diskon)
print (f"Harga setelah diskon : {harga_akhir}")