# cp

> Salin berkas dan direktori.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/cp>.

- Salin berkas ke lokasi lain:

`cp {{jalan/menuju/berkas_sumber.ext}} {{jalan/menuju/berkas_tujuan.ext}}`

- Salin berkas ke direktori lain, dengan nama yang sama:

`cp {{jalan/menuju/berkas_sumber.ext}} {{jalan/menuju/direktori_tujuan}}`

- Salin sebuah direktori secara rekursif beserta isinya ke lokasi lain (jika tujuan sudah ada, direktori tersebut disalin ke dalamnya):

`cp -R {{jalan/menuju/direktori_sumber}} {{jalan/menuju/direktori_tujuan}}`

- Salin sebuah direktori secara rekursif beserta isinya, dengan menampilkan berkas-berkas ketika disalin (mode verbose):

`cp -vR {{jalan/menuju/direktori_sumber}} {{jalan/menuju/direktori_tujuan}}`

- Salin lebih dari satu berkas menuju suatu direktori:

`cp -t {{path/to/direktori_tujuan}} {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Salin berkas-berkas teks ke lokasi lain, dalam mode interaktif (menampilkan pertanyaan sebelum menimpa):

`cp -i {{*.txt}} {{jalan/menuju/direktori_tujuan}}`

- Salin tautan simbolis sebelum menyalin:

`cp -L {{tautan}} {{jalan/menuju/direktori_tujuan}}`

- Gunakan argumen pertama sebagai direktori tujuan (berguna untuk perintah seperti `xargs ... | cp -t <DIR_TUJUAN>`):

`cp -t {{path/to/direktori_tujuan}} {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`
