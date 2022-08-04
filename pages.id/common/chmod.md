# chmod

> Mengubah hak akses pengguna ([u]ser) suatu file atau direktori.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/chmod>.

- Memberikan pengguna pembuat file hak untuk mengeksekusinya (misal: sebagai script):

`chmod u+x {{file}}`

- Memberikan hak kepada pengguna untuk membaca ([r]ead) dan menulis ([w]rite) suatu file atau direktori:

`chmod u+rw {{file_atau_direktori}}`

- Memberhentikan hak akses terhadap [g]rup untuk mengeksekusi suatu file:

`chmod g-x {{file}}`

- Memberikan semua pengguna hak untuk membaca dan mengeksekusi suatu file:

`chmod a+rx {{file}}`

- Memberikan hak-hak akses suatu file yang sama dari [g]rup kepada pengguna di luar grup ([o]thers):

`chmod o=g {{file}}`

- Menghentikan semua hak akses suatu file:

`chmod o= {{file}}`

- Memberikan hak tulis suatu direktori bagi [g]rup dan lainnya secara [R]ekursif (termasuk seluruh file yang terkandung di dalamnya):

`chmod -R g+w,o+w {{direktori}}`

- Memberikan hak semua pengguna untuk membaca seluruh file dan mengeksekusi para sub-direktori dalam suatu direktori:

`chmod -R a+rX {{direktori}}`
