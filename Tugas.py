import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Fungsi lambda untuk menghitung gaji setelah peningkatan 5%
hitung_gaji_setelah_peningkatan = lambda gaji: gaji * 1.05

# Gunakan loop for untuk menerapkan fungsi lambda ke setiap baris dalam kolom 'Gaji'
for i in range(len(df)):
    df.at[i, 'Gaji'] = hitung_gaji_setelah_peningkatan(df.at[i, 'Gaji'])

# Tampilkan DataFrame setelah perubahan
print(df)

# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

# Pertanyaan 2:
import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Fungsi lambda untuk menghitung gaji setelah peningkatan 5%
hitung_gaji_setelah_peningkatan = lambda gaji: gaji * 1.05

# Gunakan loop for untuk menerapkan fungsi lambda ke setiap baris dalam kolom 'Gaji'
for i in range(len(df)):
    df.at[i, 'Gaji'] = hitung_gaji_setelah_peningkatan(df.at[i, 'Gaji'])

# Tampilkan DataFrame setelah perubahan
print("DataFrame Setelah Perubahan:")
print(df)

# Ringkasan perubahan
print("\nRingkasan Perubahan:")
for i in range(len(df)):
    print(f"{df.at[i, 'Nama']}: Gaji awal {data['Gaji'][i]}, Gaji setelah perubahan {df.at[i, 'Gaji']}")


# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.

# Pertanyaan 3:
import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Fungsi lambda untuk menghitung gaji setelah peningkatan 5% dan tambahan 2% jika usia di atas 30 tahun
hitung_gaji_setelah_peningkatan = lambda usia, gaji: gaji * 1.05 if usia <= 30 else gaji * 1.05 * 1.02

# Gunakan loop for untuk menerapkan fungsi lambda ke setiap baris dalam kolom 'Gaji'
for i in range(len(df)):
    df.at[i, 'Gaji'] = hitung_gaji_setelah_peningkatan(df.at[i, 'Usia'], df.at[i, 'Gaji'])

# Tampilkan DataFrame setelah perubahan
print("DataFrame Setelah Perubahan:")
print(df)


# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

# Pertanyaan 4:
import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Fungsi lambda untuk menghitung gaji setelah peningkatan 5% dan tambahan 2% jika usia di atas 30 tahun
hitung_gaji_setelah_peningkatan = lambda usia, gaji: gaji * 1.05 if usia <= 30 else gaji * 1.05 * 1.02

# Gunakan loop for untuk menerapkan fungsi lambda ke setiap baris dalam kolom 'Gaji'
for i in range(len(df)):
    df.at[i, 'Gaji'] = hitung_gaji_setelah_peningkatan(df.at[i, 'Usia'], df.at[i, 'Gaji'])

# Tampilkan DataFrame setelah perubahan
print("DataFrame Setelah Perubahan:")
print(df)

# Ringkasan hasil
print("\nRingkasan Hasil:")
for i in range(len(df)):
    print(f"{df.at[i, 'Nama']}: Gaji awal {data['Gaji'][i]}, Gaji setelah perubahan {df.at[i, 'Gaji']}")


# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.