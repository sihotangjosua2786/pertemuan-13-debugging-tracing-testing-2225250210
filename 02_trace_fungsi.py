def hitung_diskon(harga, persen):
    diskon = harga * persen / 100
    return harga - diskon


print(hitung_diskon(50000, 20))