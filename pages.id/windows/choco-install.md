# choco install

> Pasang suatu atau beberapa paket dengan Chocolatey.
> Informasi lebih lanjut: <https://docs.chocolatey.org/en-us/choco/commands/install/>.

- Pasang suatu atau beberapa paket yang dipisahkan oleh spasi:

`choco install {{nama_paket1 nama_paket2 ...}}`

- Pasang kumpulan paket dari suatu berkas konfigurasi:

`choco install {{jalan\menuju\berkas_daftar_paket.config}}`

- Pasang suatu paket dari berkas `.nuspec` atau `.nupkg` secara spesifik:

`choco install {{jalan\menuju\berkas}}`

- Pasang suatu paket dengan versi spesifik:

`choco install {{nama_paket}} --version {{versi}}`

- Izinkan untuk memasang beberapa versi dari paket yang sama:

`choco install {{nama_paket}} --allow-multiple`

- Lakukan konfirmasi perizinan secara otomatis:

`choco install {{nama_paket}} --yes`

- Tentukan suatu sumber untuk mendapatkan kumpulan paket:

`choco install {{nama_paket}} --source {{url_sumber|alias}}`

- Sediakan nama pengguna (username) dan kata sandi untuk autentikasi:

`choco install {{nama_paket}} --user {{username}} --password {{kata_sandi}}`
