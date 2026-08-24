# carthage

> Suatu alat manajer modul ketergantungan/dependensi untuk pengembangan aplikasi berbasis Cocoa.
> Informasi lebih lanjut: <https://github.com/Carthage/Carthage>.

- Unduh dan bangun seluruh dependensi versi terkini, yang didaftarkan dalam berkas Cartfile:

`carthage update`

- Perbarui daftar dependensi, namun hanya lakukan pembangunan untuk program iOS:

`carthage update --platform ios`

- Perbarui daftar dependensi tanpa melakukan proses pembangunan apapun:

`carthage update --no-build`

- Unduh dan bangun kembali versi dependensi saat ini (tanpa memperbaruinya):

`carthage bootstrap`

- Lakukan proses pembangunan ulang atas suatu dependensi:

`carthage build {{dependensi}}`
