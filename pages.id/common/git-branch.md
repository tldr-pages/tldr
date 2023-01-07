# git branch

> Perintah Git utama untuk bekerja dengan cabang (_branch_).
> Informasi lebih lanjut: <https://git-scm.com/docs/git-branch>.

- Tampilkan daftar semua cabang (lokal dan remote; cabang saat ini ditandai oleh `*`) :

`git branch --all`

- Tampilkan daftar semua cabang yang memiliki komit Git tertentu di dalam riwayat:

`git branch --all --contains {{hash_komit}}`

- Tampilkan nama cabang saat ini:

`git branch --show-current`

- Buat cabang baru berdasarkan komit saat ini:

`git branch {{nama_cabang}}`

- Buat cabang baru berdasarkan komit tertentu:

`git branch {{nama_cabang}} {{hash_komit}}`

- Ubah nama cabang (harus bukan cabang saat ini untuk melakukannya):

`git branch -m {{nama_cabang_lama}} {{nama_cabang_baru}}`

- Hapus cabang lokal (harus bukan cabang saat ini untuk melakukannya):

`git branch -d {{nama_cabang}}`

- Hapus cabang remote:

`git push {{nama_remote}} --delete {{nama_cabang_remote}}`
