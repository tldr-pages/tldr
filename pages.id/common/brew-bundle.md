# brew bundle

> Pembungkus untuk Homebrew, Homebrew Cask, dan App Store untuk macOS.
> Informasi lebih lanjut: <https://github.com/Homebrew/homebrew-bundle>.

- Pasang seluruh paket menurut data Brewfile pada direktori saat ini:

`brew bundle`

- Pasang seluruh paket menurut data Brewfile pada lokasi tertentu:

`brew bundle --file {{jalan/menuju/berkas}}`

- Buat suatu berkas Brewfile berisikan daftar seluruh paket yang terpasang saat ini:

`brew bundle dump`

- Hapus seluruh formula yang tidak didefinisikan atau dibutuhkan pada formula dalam berkas Brewfile:

`brew bundle cleanup --force`

- Cari tahu apakah terdapat formula yang perlu dipasang atau dimutakhirkan dalam berkas Brewfile:

`brew bundle check`

- Tampilkan seluruh entri dalam berkas Brewfile:

`brew bundle list --all`
