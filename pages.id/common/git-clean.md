# git clean

> Hapus berkas-berkas yang tak dilacak oleh Git pada pohon direktori kerja saat ini.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-clean>.

- Hapus menggunakan mode interaktif:

`git clean {{[-i|--interactive]}}`

- Tampilkan kumpulan berkas yang akan dihapus tanpa menghapusnya:

`git clean {{[-n|--dry-run]}}`

- Hapus berkas-berkas secara paksa:

`git clean {{[-f|--force]}}`

- Hapus kumpulan [d]irektori secara paksa:

`git clean {{[-f|--force]}} -d`

- Hanya hapus berkas-berkas tak dilacak dengan alamat berkas spesifik atau pola (glob) nama yang sesuai dengan yang ditentukan:

`git clean {{[-f|--force]}} -- {{jalan/menuju/direktori}} '{{*.ext}}'`

- Hapus berkas-berkas tak dilacak kecuali dalam alamat atau pola nama yang ditentukan:

`git clean {{[-f|--force]}} {{[-e|--exclude]}} '{{*.ext}}' {{[-e|--exclude]}} {{jalan/menuju/direktori}}/`

- Hapus berkas-berkas yang tak dilacak, termasuk berkas yang dikecualikan (menurut daftar `.gitignore` dan `.git/info/exclude`):

`git clean {{[-f|--force]}} -x`
