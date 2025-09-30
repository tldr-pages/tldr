# git init

> Inisialisasikan sebuah repositori Git lokal.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-init>.

- Inisialisasikan suatu direktori menjadi repositori lokal baru:

`git init`

- Inisialisasikan sebuah repositori dengan nama cabang (branch) awal yang ditentukan:

`git init {{[-b|--initial-branch]}} {{nama_cabang}}`

- Inisialisasikan sebuah repositori menggunakan format hash objek berbasis SHA256 (membutuhkan Git versi 2.29+):

`git init --object-format sha256`

- Inisialisasikan sebuah repositori kosong (barebones) yang dapat digunakan sebagai remote melalui koneksi SSH:

`git init --bare`
