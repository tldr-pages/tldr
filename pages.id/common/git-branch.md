# git branch

> Perintah Git utama untuk bekerja dengan cabang (*branch*).
> Informasi lebih lanjut: <https://git-scm.com/docs/git-branch>.

- Menampilkan daftar semua cabang (local dan remote; cabang saat ini ditandai oleh `*`) :

`git branch --all`

- Menampilkan daftar semua cabang yang memiliki komit tertentu di dalam riwayat:

`git branch --all --contains {{hash_komit}}`

- Menampilkan nama cabang saat ini:

`git branch --show-current`

- Membuat cabang baru berdasarkan komit saat ini:

`git branch {{nama_cabang}}`

- Membuat cabang baru berdasarkan komit tertentu:

`git branch {{nama_cabang}} {{hash_komit}}`

- Mengganti nama cabang (harus bukan cabang saat ini untuk melakukannya):

`git branch -m {{nama_cabang_lama}} {{nama_cabang_baru}}`

- Menghapus cabang lokal (harus bukan cabang saat ini untuk melakukannya):

`git branch -d {{nama_cabang}}`

- Menghapus cabang remote:

`git push {{nama_remote}} --delete {{nama_cabang_remote}}`
