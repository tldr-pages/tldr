# choco install

> Instal satu paket atau lebih dengan Chocolatey.
> Informasi lebih lanjut: <https://docs.chocolatey.org/en-us/choco/commands/install>.

- Instal satu paket atau lebih paket yang dipisahkan oleh spasi:

`choco install {{paket}}`

- Instal paket dari file konfigurasi khusus:

`choco install {{jalan/menuju/paket.config}}`

- Instal file nuspec atau nupkg tertentu:

`choco install {{jalan/menuju/file}}`

- Instal versi paket tertentu:

`choco install {{paket}} --version {{versi}}`

- Izinkan menginstal beberapa versi paket:

`choco install {{paket}} --allow-multiple`

- Konfirmasikan semua prompt secara otomatis:

`choco install {{paket}} --yes`

- Tentukan sumber khusus untuk menerima paket:

`choco install {{paket}} --source {{url_sumber|alias}}`

- Berikan nama pengguna dan kata sandi untuk otentikasi:

`choco install {{paket}} --user {{nama_pengguna}} --password {{kata_sandi}}`
