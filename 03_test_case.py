def cek_bonus(total_belanja):

    if total_belanja >= 100000:
        return "Bonus"

    return "Tidak Bonus"


print(cek_bonus(150000))
print(cek_bonus(100000))
print(cek_bonus(50000))