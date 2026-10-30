def hitung_rata_penjualan(data):

    if len(data) == 0:
        return 0

    return sum(data) / len(data)


def status_diskon(total):

    if total >= 100000:
        return "Dapat Diskon"

    return "Tidak Dapat Diskon"


def penjualan_tertinggi(data):

    if len(data) == 0:
        return None

    tertinggi = data[0]

    for item in data[1:]:

        if item > tertinggi:
            tertinggi = item

    return tertinggi


penjualan = [100, 200, 150, 250]

print("Rata-rata :", hitung_rata_penjualan(penjualan))
print("Status 100000 :", status_diskon(100000))
print("Tertinggi :", penjualan_tertinggi(penjualan))