# hugo

> Penghasil website statis berbasis template. Menggunakan modul, komponen dan tema.
> Informasi lebih lanjut: <https://gohugo.io>.

- Membuat website Hugo baru:

`hugo new site {{alamat/ke/website}}`

- Membuat tema Hugo baru (tema juga dapat diunduh dari <https://themes.gohugo.io/>):

`hugo new theme {{nama_tema}}`

- Membuat halaman baru:

`hugo new {{nama_bagian}}/{{nama_berkas}}`

- Menbuild website ke direktori `./public`:

`hugo`

- Menbuild website termasuk halaman yang ditandai sebagai "draft":

`hugo --buildDrafts`

- Menbuild website ke direktori yang ditentukan:

`hugo --destination {{alamat/tujuan}}`

- Menbuild website, memulai webserver untuk menyajikannya, dan secara otomatis memuat ulang jika ada halaman yang berubah:

`hugo server`
