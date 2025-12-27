# choco info

> Tampilkan informasi suatu paket piranti lunak secara terperinci dengan Chocolatey.
> Informasi lebih lanjut: <https://docs.chocolatey.org/en-us/choco/commands/info/>.

- Tampilkan informasi mengenai suatu paket:

`choco info {{paket}}`

- Tampilkan informasi mengenai suatu paket dengan versi yang terpasang secara lokal saja:

`choco info {{paket}} {{[-l|--local-only]}}`

- Tentukan suatu repositori paket secara kustom sebagai sumber informasi kumpulan paket:

`choco info {{paket}} {{[-s|--source]}} {{url_sumber|alias}}`

- Gunakan suatu username dan kata sandi untuk mendukung proses autentikasi pengguna:

`choco info {{paket}} {{[-u|--user]}} {{username}} {{[-p|--password]}} {{kata_sandi}}`
