# git apply

> Gunakan perubahan dari file deskripsi perubahan (patch) kepada indeks perubahan tanpa mencatat sebuah komit.
> Lihat juga `git am`, yang sama-sama menggunakan perubahan dari file patch namun juga mencatatnya ke dalam sebuah komit baru.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-apply>.

- Tampilkan informasi lengkap (mode verbose) atas proses perubahan yang sedang dilakukan:

`git apply --verbose {{jalan/menuju/file}}`

- Gunakan patch dan tambahkan file yang diubah ke dalam indeks perubahan:

`git apply --index {{jalan/menuju/file}}`

- Gunakan perubahan dari file patch dari sumber dalam jaringan (online):

`curl -L {{https://example.com/file.patch}} | git apply`

- Tampilkan informasi statistik perbedaan (diffstat) setelah melakukan perubahan menurut file patch:

`git apply --stat --apply {{jalan/menuju/file}}`

- Batalkan perubahan yang dilakukan melalui file patch:

`git apply --reverse {{jalan/menuju/file}}`

- Simpan hasil perubahan ke dalam indeks perubahan tanpa merubah susunan file/direktori dalam direktori kerja saat ini:

`git apply --cache {{jalan/menuju/file}}`
