# git bugreport

> Tangkap dan simpan informasi sistem dan pengguna Git dalam berkas teks untuk kepentingan melaporkan dan menyelesaikan masalah/bug internal dalam Git.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-bugreport>.

- Buat berkas laporan masalah/bug baru pada direktori saat ini:

`git bugreport`

- Buat berkas laporan pada direktori tertentu, dan buat direktori tersebut jika belum:

`git bugreport --output-directory {{jalan/menuju/direktori}}`

- Buat berkas laporan baru, dengan nama berkas diakhiri dengan tanggal pelaporan menurut format `strftime`:

`git bugreport --suffix {{%m%d%y}}`
