# rspec

> Kerangka pengujian dalam Behavior-driven development yang ditulis dalam bahasa Ruby untuk menguji kode Ruby.
> Informasi lebih lanjut: <https://rspec.info>.

- Menginisiasi file konfigurasi .rspec dan spec helper:

`rspec --init`

- Menjalankan semua file tes:

`rspec`

- Menjalankan file tes dalam direktori khusus:

`rspec {{jalan/ke/directory}}`

- Menjalankan file tes khusus:

`rspec {{jalan/ke/file}}`

- Menjalankan beberapa file tes:

`rspec {{jalan/ke/file1}} {{jalan/ke/file2}}`

- Menjalankan kasus khusus dalam file tes (misalnya tes yang ada di baris 83):

`rspec {{jalan/ke/file}}:{{83}}`

- Menjalankan tes dengan seed khusus:

`rspec --seed {{angka_seed}}`
