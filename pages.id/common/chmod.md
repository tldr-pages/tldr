# chmod

> Mengubah hak akses pengguna suatu file atau direktori.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/chmod>.

- Berikan pengguna pembuat file hak untuk mengeksekusinya (misal: sebagai script):

`chmod u+x {{file}}`

- Berikan hak kepada pengguna untuk membaca ([r]ead) dan menulis ([w]rite) suatu file atau direktori:

`chmod u+rw {{jalan/menuju/file_atau_direktori}}`

- Hentikan hak akses terhadap [g]rup untuk mengeksekusi suatu file:

`chmod g-x {{jalan/menuju/file}}`

- Berikan semua pengguna hak untuk membaca dan mengeksekusi suatu file:

`chmod a+rx {{jalan/menuju/file}}`

- Berikan hak-hak akses suatu file yang sama dari [g]rup kepada pengguna di luar grup ([o]thers):

`chmod o=g {{jalan/menuju/file}}`

- Hentikan semua hak akses suatu file:

`chmod o= {{jalan/menuju/file}}`

- Berikan hak tulis suatu direktori bagi [g]rup dan lainnya secara [R]ekursif (termasuk seluruh file yang terkandung di dalamnya):

`chmod -R g+w,o+w {{jalan/menuju/direktori}}`

- Berikan hak semua pengguna untuk membaca seluruh file dan mengeksekusi para sub-direktori dalam suatu direktori:

`chmod -R a+rX {{jalan/menuju/direktori}}`
