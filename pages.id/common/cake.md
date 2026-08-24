# cake

> Alat baris perintah untuk memproses proyek aplikasi web berbasis framework CakePHP.
> Informasi lebih lanjut: <https://book.cakephp.org/5/en/console-commands.html#cakephp-provided-commands>.

- Tampilkan informasi dasar mengenai proyek aplikasi saat ini beserta daftar perintah:

`cake`

- Tampilkan daftar rute aplikasi web yang tersedia:

`cake routes`

- Hapus berkas-berkas cache konfigurasi proyek:

`cake cache clear_all`

- Bangun berkas cache metadata bagi proyek saat ini:

`cake schema_cache build --connection {{koneksi}}`

- Hapus berkas cache metadata:

`cake schema_cache clear`

- Hapus suatu tabel cache:

`cake schema_cache clear {{nama_tabel}}`

- Jalankan sebuah peladen web untuk kepentingan pengembangan (secara bawaan mengarah menuju port 8765):

`cake server`

- Jalankan sebuah proses REPL (syel interaktif):

`cake console`
