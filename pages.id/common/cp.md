# cp

> Membuat salinan file dan direktori.

- Membuat salinan file ke lokasi lain:

`cp {{jalan/menuju/file_sumber.ext}} {{jalan/menuju/file_tujuan.ext}}`

- Menyalin file ke direktori lain, dengan nama yang sama:

`cp {{jalan/menuju/file_sumber.ext}} {{jalan/menuju/direktori_tujuan}}`

- Menyalin sebuah direktori secara beserta isinya ke lokasi lain (jika tujuan sudah ada, direktori tersebut disalin ke dalamnya):

`cp -R {{jalan/menuju/direktori_sumber}} {{jalan/menuju/direktori_tujuan}}`

- Menyalin sebuah direktori secara beserta isinya, dalam mode `verbose` (menampilkan file-file ketika disalin):

`cp -vR {{jalan/menuju/direktori_sumber}} {{jalan/menuju/direktori_tujuan}}`

- Menyalin file-file teks ke lokasi lain, dalam mode interaktif (menampilkan pertanyaan sebelum menimpa):

`cp -i {{*.txt}} {{jalan/menuju/direktori_tujuan}}`

- Melepaskan tautan simbolis sebelum menyalin:

`cp -L {{tautan}} {{jalan/menuju/direktori_tujuan}}`
