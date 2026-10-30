def rata_penjualan(data):

    if len(data) == 0:
        return 0

    return sum(data) / len(data)


data = [100, 200, 300]

print("Rata-rata =", rata_penjualan(data))