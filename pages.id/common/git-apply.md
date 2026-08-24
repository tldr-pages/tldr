# git apply

> Gunakan perubahan dari file deskripsi perubahan (patch) kepada indeks perubahan tanpa mencatat sebuah komit.
> Lihat juga: `git am`.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-apply>.

- Tampilkan informasi lengkap (mode verbose) atas proses perubahan yang sedang dilakukan:

`git apply {{[-v|--verbose]}} {{jalan/menuju/berkas}}`

- Gunakan patch dan tambahkan file yang diubah ke dalam indeks perubahan:

`git apply --index {{jalan/menuju/berkas}}`

- Gunakan perubahan dari file patch dari sumber dalam jaringan (online):

`curl {{[-L|--location]}} {{https://example.com/file.patch}} | git apply`

- Tampilkan informasi statistik perbedaan (diffstat) setelah melakukan perubahan menurut file patch:

`git apply --stat --apply {{jalan/menuju/berkas}}`

- Batalkan perubahan yang dilakukan melalui file patch:

`git apply {{[-R|--reverse]}} {{jalan/menuju/berkas}}`

- Simpan hasil perubahan ke dalam indeks perubahan tanpa merubah susunan file/direktori dalam direktori kerja saat ini:

`git apply --cache {{jalan/menuju/berkas}}`
