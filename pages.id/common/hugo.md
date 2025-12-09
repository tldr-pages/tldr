# hugo

> Penghasil situs web statis berbasis template. Menggunakan modul, komponen dan tema.
> Informasi lebih lanjut: <https://gohugo.io/commands/>.

- Buat sebuah proyek situs web Hugo baru:

`hugo new site {{jalan/menuju/website}}`

- Buat sebuah proyek tema Hugo baru (tema juga dapat diunduh dari <https://themes.gohugo.io/>):

`hugo new theme {{nama_tema}}`

- Buat sebuah halaman situs web baru:

`hugo new {{nama_bagian}}/{{nama_halaman}}`

- Bangun situs web dari direktori sumber menuju direktori `./public`:

`hugo`

- Bangun situs web termasuk halaman yang ditandai sebagai "draft":

`hugo {{[-D|--buildDrafts]}}`

- Bangun situs web dengan untuk dijalankan pada alamat IP lokal:

`hugo server --bind {{ip_lokal}} {{[-b|--baseURL]}} {{http://ip_lokal}}`

- Bangun situs web menuju direktori yang ditentukan:

`hugo {{[-d|--destination]}} {{alamat/tujuan}}`

- Bangun situs web dan jalankan peladen (server) untuk menyajikannya, dengan memuat ulang saat terdapat halaman yang berubah:

`hugo server`
