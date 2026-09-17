# autoflake

> Hapuskan kumpulan perintah impor dan variable yang tidak dipakai dalam kode program Python.
> Informasi lebih lanjut: <https://github.com/PyCQA/autoflake#advanced-usage>.

- Hapuskan kumpulan variabel yang tidak terpakai dalam suatu berkas kode, dan tampilkan daftar perbedaan isi berkas (diff):

`autoflake --remove-unused-variables {{jalan/menuju/berkas.py}}`

- Hapuskan kumpulan perintah impor yang tidak terpakai dalam beberapa berkas dan tampilkan perbedaannya:

`autoflake --remove-all-unused-imports {{jalan/menuju/berkas1.py jalan/menuju/berkas2.py ...}}`

- Hapuskan kumpulan variabel tidak terpakai dan segera sunting berkas tersebut:

`autoflake --remove-unused-variables --in-place {{jalan/menuju/berkas.py}}`

- Hapus kumpulan variabel tidak terpakai dan segera sunting seluruh berkas dalam suatu direktori secara rekursif:

`autoflake --remove-unused-variables --in-place --recursive {{jalan/menuju/direktori}}`
