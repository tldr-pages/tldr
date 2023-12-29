# git bugreport

> Tangkap dan simpan informasi sistem dan pengguna Git dalam file teks untuk kepentingan melaporkan dan menyelesaikan masalah/bug internal dalam Git.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-bugreport>.

- Buat file laporan masalah/bug baru pada direktori saat ini:

`git bugreport`

- Buat file laporan pada direktori tertentu, dan buat direktori tersebut jika belum:

`git bugreport --output-directory {{jalan/menuju/direktori}}`

- Buat file laporan baru, dengan nama file diakhiri dengan tanggal pelaporan menurut format `strftime`:

`git bugreport --suffix {{%m%d%y}}`
