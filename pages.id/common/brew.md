# brew

> Homebrew - suatu manajer paket bagi macOS dan Linux.
> Beberapa subperintah seperti `install` mempunyai dokumentasi terpisah.
> Informasi lebih lanjut: <https://docs.brew.sh/Manpage>.

- Pasang versi terkini oleh suatu formula atau cask:

`brew install {{formula|cask}}`

- Tampilkan daftar formula dan cask yang terpasang:

`brew list`

- Mutakhirkan suatu formula atau cask (jika nama tidak disediakan, semua formula dan cask terpasang akan dimutakhirkan):

`brew upgrade {{formula|cask}}`

- Dapatkan program Homebrew versi terkini dan semua formula dan cask yang tersedia dari repositori paket Homebrew:

`brew update`

- Tampilkan daftar formula dan cask yang memiliki versi lebih baru dari yang terpasang:

`brew outdated`

- Cari formula (paket biasa) serta cask (berkas aplikasi `.app` bagi macOS):

`brew search {{teks}}`

- Tampilkan informasi mengenai suatu formula atau cask (versi, lokasi pemasangan, formula/cask tambahan yang dibutuhkan, dll.):

`brew info {{formula|cask}}`

- Cek kondisi pemasangan Homebrew saat ini untuk mendeteksi kemungkinan galat atau masalah:

`brew doctor`
