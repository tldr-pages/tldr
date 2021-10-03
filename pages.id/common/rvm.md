# rvm

> Alat untuk menginstal, mengatur dan bekerja dengan berbagai lingkungan Ruby.
> Informasi lebih lanjut: <https://rvm.io>.

- Instal satu atau lebih versi Ruby (dipisah dengan spasi):

`rvm install {{version(s)}}`

- Menampilkan daftar versi-versi yang terinstal:

`rvm list`

- Menggunakan spesifik versi Ruby:

`rvm use {{version}}`

- Menyetel versi Ruby bawaan:

`rvm --default use {{version}}`

- Memperbarui versi Ruby:

`rvm upgrade {{current_version}} {{new_version}}`

- Menghapus versi Ruby dan menyimpan kode sumbernya:

`rvm uninstall {{version}}`

- Menghapus versi Ruby sekaligus kode sumbernya:

`rvm remove {{version}}`

- Menampilkan spesifik _dependencies_ untuk sistem operasi anda:

`rvm requirements`
