def stok_terbanyak(stok):

    if len(stok) == 0:
        return None

    terbesar = stok[0]

    for item in stok[1:]:

        if item > terbesar:
            terbesar = item

    return terbesar


print(stok_terbanyak([30, 20, 50, 10]))