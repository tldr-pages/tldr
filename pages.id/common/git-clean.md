# git clean

> Hapus berkas-berkas yang tak dilacak oleh Git pada pohon direktori kerja saat ini.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-clean>.

- Hapus seluruh berkas yang tak dilacak:

`git clean`

- Hapus menggunakan mode [i]nteraktif:

`git clean {{-i|--interactive}}`

- Tampilkan kumpulan berkas yang akan dihapus tanpa menghapusnya:

`git clean --dry-run`

- Hapus berkas-berkas secara paksa:

`git clean {{-f|--force}}`

- Hapus kumpulan [d]irektori secara paksa:

`git clean {{-f|--force}} -d`

- Hapus berkas-berkas yang tak dilacak, termasuk berkas yang dikecualikan (menurut daftar `.gitignore` dan `.git/info/exclude`):

`git clean -x`
