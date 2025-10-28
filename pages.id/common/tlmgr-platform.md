# tlmgr platform

> Atur konfigurasi platform (arsitektur bahasa prosesor) yang digunakan pada TeX Live.
> Informasi lebih lanjut: <https://www.tug.org/texlive/doc/tlmgr.html#platform>.

- Tampilkan daftar seluruh platform yang tersedia untuk diunduh dari repositori paket:

`tlmgr platform list`

- Tambahkan berkas-berkas executable yang tersedia untuk suatu platform:

`sudo tlmgr platform add {{platform}}`

- Hapus berkas-berkas executable yang tersedia untuk suatu platform:

`sudo tlmgr platform remove {{platform}}`

- Lakukan pengecekan otomatis dan alih konfigurasi pemasangan paket menuju platform saat ini:

`sudo tlmgr platform set auto`

- Alih konfigurasi pemasangan paket menuju suatu platform:

`sudo tlmgr platform set {{platform}}`
