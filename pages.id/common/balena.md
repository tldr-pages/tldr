# balena

> Lakukan interaksi dengan layanan balenaCloud, openBalena, dan balena API.
> Informasi lebih lanjut: <https://www.balena.io/docs/reference/cli/>.

- Masuk dengan akun balenaCloud:

`balena login`

- Buat suatu aplikasi balenaCloud atau openBalena baru:

`balena app create {{nama_aplikasi}}`

- Tampilkan daftar seluruh aplikasi yang diatur dalam akun balenaCloud atau openBalena:

`balena apps`

- Tampilkan daftar seluruh perangkat yang terhubung dengan akun balenaCloud atau openBalena:

`balena devices`

- Pasang citra balenaOS ke dalam suatu perangkat penyimpanan lokal:

`balena local flash {{jalan/menuju/balenaos.img}} --drive {{lokasi_penyimpanan}}`
