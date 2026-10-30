def status_diskon(total):

    if total >= 100000:
        return "Dapat Diskon"

    return "Tidak Dapat Diskon"


print(status_diskon(90000))
print(status_diskon(100000))
print(status_diskon(120000))