# rspec

> Kerangka pengujian dalam Behavior-driven development yang ditulis dalam bahasa Ruby untuk menguji kode Ruby.
> Informasi lebih lanjut: <https://rspec.info>.

- Menginisiasi file konfigurasi .rspec dan spec helper:

`rspec --init`

- Menjalankan semua file tes:

`rspec`

- Menjalankan file tes dalam direktori khusus:

`rspec {{lokasi/ke/directory}}`

- Menjalankan file tes khusus:

`rspec {{lokasi/ke/file}}`

- Menjalankan beberapa file tes:

`rspec {{lokasi/ke/file1}} {{lokasi/ke/file2}}`

- Menjalankan kasus khusus dalam file tes (misalnya tes yang ada di baris 83):

`rspec {{lokasi/ke/file}}:{{83}}`

- Menjalankan tes dengan _seed_ khusus:

`rspec --seed {{seed_number}}`
