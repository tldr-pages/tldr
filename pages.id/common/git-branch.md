# git branch

> Perintah Git utama untuk bekerja dengan cabang (*branch*).
> Informasi lebih lanjut: <https://git-scm.com/docs/git-branch>.

- Menampilkan daftar cabang lokal. Cabang saat ini ditandai oleh `*`:

`git branch`

- Menampilkan daftar semua cabang (lokal dan remote):

`git branch -a`

- Tunjukkan nama cabang saat ini:

`git branch --show-current`

- Buat cabang baru berdasarkan komit saat ini:

`git branch {{nama_cabang}}`

- Buat cabang baru berdasarkan komit tertentu:

`git branch {{nama_cabang}} {{hash_komit}}`

- Ganti nama cabang (harus bukan cabang saat ini untuk melakukannya):

`git branch -m {{nama_cabang_lama}} {{nama_cabang_baru}}`

- Hapus cabang lokal (harus bukan cabang saat ini untuk melakukannya):

`git branch -d {{nama_cabang}}`

- Hapus cabang remote:

`git push {{nama_remote}} --delete {{nama_cabang_remote}}`
