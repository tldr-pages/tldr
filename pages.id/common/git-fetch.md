# git fetch

> Unduh kumpulan objek dan referensi dari suatu repositori jarak jauh.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-fetch>.

- Dapatkan perubahan-perubahan terkini dari repositori bersumber hulu jarak jauh (remote upstream) yang ditentukan sebagai default (bila ditentukan):

`git fetch`

- Dapatkan daftar cabang-cabang baru dari sumber hulu jarak jauh yang ditentukan:

`git fetch {{nama_remote}}`

- Dapatkan daftar perubahan terkini dari seluruh repositori hulu jarak jauh:

`git fetch --all`

- Dapatkan juga daftar tag yang terdaftar dalam repositori hulu jarak jauh:

`git fetch {{[-t|--tags]}}`

- Hapus referensi-referensi lokal menuju cabang-cabang repositori hulu yang telah dihapus secara jarak jauh:

`git fetch {{[-p|--prune]}}`

- Perdalam tingkat kedalaman komit dalam cabang saat ini (jika menggunakan shallow clone) dengan 2 komit:

`git fetch --deepen 2`

- Perbarui cabang `main` tanpa mengalihkan isi direktori kerja repositori lokal menuju versi cabang tersebut (setara dengan `git pull`):

`git fetch {{origin}} main:main`
