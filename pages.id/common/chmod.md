# chmod

> Mengubah hak akses pengguna suatu file atau direktori.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html>.

- Berikan pengguna pembuat file hak untuk mengeksekusinya (misal: sebagai script):

`chmod u+x {{file}}`

- Berikan hak kepada pengguna untuk membaca ([r]ead) dan menulis ([w]rite) suatu file atau direktori:

`chmod u+rw {{jalan/menuju/berkas_atau_direktori}}`

- Hentikan hak akses terhadap [g]rup untuk mengeksekusi suatu file:

`chmod g-x {{jalan/menuju/berkas}}`

- Berikan semua pengguna hak untuk membaca dan mengeksekusi suatu file:

`chmod a+rx {{jalan/menuju/berkas}}`

- Berikan hak-hak akses suatu file yang sama dari [g]rup kepada pengguna di luar grup ([o]thers):

`chmod o=g {{jalan/menuju/berkas}}`

- Hentikan semua hak akses suatu file:

`chmod o= {{jalan/menuju/berkas}}`

- Berikan hak tulis suatu direktori bagi [g]rup dan lainnya secara [R]ekursif (termasuk seluruh file yang terkandung di dalamnya):

`chmod {{[-R|--recursive]}} g+w,o+w {{jalan/menuju/direktori}}`

- Berikan hak semua pengguna untuk membaca seluruh file dan mengeksekusi para sub-direktori dalam suatu direktori:

`chmod {{[-R|--recursive]}} a+rX {{jalan/menuju/direktori}}`
