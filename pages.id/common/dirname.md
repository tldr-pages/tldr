# dirname

> Hapus bagian nama berkas dari sebuah alamat berkas, untuk menentukan alamat direktori asal berkas.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>.

- Tentukan alamat direktori dari suatu alamat:

`dirname {{jalan/menuju/berkas_atau_direktori}}`

- Tentukan alamat direktori dari berbagai alamat:

`dirname {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`

- Gunakan karakter NUL daripada baris baru untuk memisah luaran antar alamat (berguna jika digunakan bersamaan dengan `xargs`):

`dirname {{[-z|--zero]}} {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`
