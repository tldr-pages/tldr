# asdf

> Alat baris perintah untuk mengatur versi paket piranti lunak yang berbeda-beda.
> Informasi lebih lanjut: <https://asdf-vm.com/manage/commands.html>.

- Tampilkan seluruh plugin yang tersedia untuk dipasang:

`asdf plugin list all`

- Pasang suatu plugin:

`asdf plugin add {{nama}}`

- Tampilkan seluruh versi yang tersedia terhadap suatu paket:

`asdf list all {{nama}}`

- Pasang suatu paket dengan versi tertentu:

`asdf install {{nama}} {{versi}}`

- Setel versi bawaan/default paket piranti lunak yang akan digunakan secara global (seluruh pengguna):

`asdf set -u {{nama}} {{versi}}`

- Setel versi bawaan/default paket piranti lunak yang akan digunakan secara lokal (pengguna saat ini):

`asdf set {{nama}} {{versi}}`
