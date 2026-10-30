Pertemuan 13 - Debugging dan Testing
Nama : Josua Evanno M A Sihotang 
NIM :2225250210 
Kelas : 3B

Kasus
Program digunakan untuk menghitung rata-rata penjualan, menentukan status diskon, dan mencari penjualan tertinggi.

Test Case
ID	Input	Expected	Actual Awal	Status
T1	[100,200,150,250]	175	175	PASS
T2	[]	0	0	PASS
T3	100000	Dapat Diskon	Dapat Diskon	PASS
T4	99999	Tidak Dapat Diskon	Tidak Dapat Diskon	PASS
T5	[100,200,150,250]	250	250	PASS
Bug Report
B01
Perhitungan rata-rata menggunakan pembagi tetap.

Perbaikan: Menggunakan len(data).

B02
Batas diskon menggunakan operator >.

Perbaikan: Menggunakan >=.

B03
Pencarian nilai maksimum menggunakan operator salah.

Perbaikan: Menggunakan >.

Retest
Seluruh test PASS.

Cara Menjalankan
python praktik/praktik_4_debugging.py

Refleksi
Tracing variabel dan test case batas sangat membantu menemukan bug.