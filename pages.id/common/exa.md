# exa

> Pengganti `ls` (Tampilkan isi direktori) yang modern.
> Informasi lebih lanjut: <https://github.com/ogham/exa#command-line-options>.

- Tampilkan daftar berkas, satu berkas per baris:

`exa {{[-1|--oneline]}}`

- Tampilkan daftar seluruh berkas, termasuk berkas-berkas tersembunyi:

`exa {{[-a|--all]}}`

- Tampilkan daftar seluruh berkas dengan format informasi panjang (perizinan, pemilik, ukuran, dan tanggal modifikasi):

`exa {{[-l|--long]}} {{[-a|--all]}}`

- Tampilkan daftar seluruh berkas dengan berkas terbesar terlebih dahulu:

`exa {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Tampilkan daftar berkas dalam format pohon (tree) hingga tingkat kedalaman ketiga:

`exa {{[-l|--long]}} {{[-T|--tree]}} {{[-L|--level]}} {{3}}`

- Tampilkan daftar berkas yang diurutkan menurut tanggal modifikasi (terlawas terlebih dahulu):

`exa {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- Tampilkan daftar berkas dengan informasi header, ikon, dan status berkas dalam Git:

`exa {{[-l|--long]}} {{[-h|--header]}} --icons --git`

- Jangan tampilkan daftar berkas yang terdaftar dalam `.gitignore`:

`exa --git-ignore`
