def rata_penjualan(data):

    if len(data) == 0:
        return 0

    return sum(data) / len(data)


penjualan = [100, 150, 200]

print(rata_penjualan(penjualan))