# choco install

> Instal satu paket atau lebih dengan Chocolatey.
> Informasi lebih lanjut: <https://docs.chocolatey.org/en-us/choco/commands/install>.

- Instal satu paket atau lebih paket yang dipisahkan oleh spasi:

`choco install {{nama_paket}}`

- Instal paket dari file konfigurasi khusus:

`choco install {{lokasi/ke/nama_paket.config}}`

- Instal file nuspec atau nupkg tertentu:

`choco install {{lokasi/ke/file}}`

- Instal versi paket tertentu:

`choco install {{nama_paket}} --version {{versi}}`

- Izinkan menginstal beberapa versi paket:

`choco install {{nama_paket}} --allow-multiple`

- Konfirmasikan semua prompt secara otomatis:

`choco install {{nama_paket}} --yes`

- Tentukan sumber khusus untuk menerima paket:

`choco install {{nama_paket}} --source {{url_sumber|alias}}`

- Berikan nama pengguna dan kata sandi untuk otentikasi:

`choco install {{nama_paket}} --user {{nama_user}} --password {{kata_sandi}}`
