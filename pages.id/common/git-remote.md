# git remote

> Kelola kumpulan repositori yang dilacak/diikuti dari sumber jarak jauh ("remotes").
> Informasi lebih lanjut: <https://git-scm.com/docs/git-remote>.

- Tampilkan daftar remote, namanya dan URL:

`git remote {{[-v|--verbose]}}`

- Tampilkan informasi tentang suatu remote:

`git remote show {{nama_remote}}`

- Tambahkan suatu remote untuk diikuti pada repositori saat ini:

`git remote add {{nama_remote}} {{url_remote}}`

- Ubah alamat URL dari remote (gunakan `--add` untuk tetap menyimpan URL lama):

`git remote set-url {{nama_remote}} {{url_baru}}`

- Tampilkan alamat URL dari suatu remote:

`git remote get-url {{nama_remote}}`

- Hapus remote dari daftar remote yang dilacak pada repositori saat ini:

`git remote remove {{nama_remote}}`

- Ubah nama remote untuk dikelola dalam repositori saat ini:

`git remote rename {{nama_lama}} {{nama_baru}}`
