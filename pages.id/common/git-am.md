# git am

> Gunakan perubahan dari file deskripsi perubahan (patch) untuk melakukan sebuah komit. Dapat digunakan untuk menerima komit melalui surel/email.
> Lihat juga `git format-patch` untuk membuat file deskripsi perubahan/patch.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-am>.

- Gunakan dan komit perubahan dari file patch dalam direktori lokal:

`git am {{jalan/menuju/file.patch}}`

- Gunakan dan komit perubahan dari file patch dari sumber dalam jaringan (online):

`curl -L {{https://example.com/file.patch}} | git apply`

- Batalkan proses perubahan yang dilakukan:

`git am --abort`

- Lakukan perubahan-perubahan dari file patch sebisa mungkin, dan tolak file patch jika proses tersebut gagal:

`git am --reject {{jalan/menuju/file.patch}}`
