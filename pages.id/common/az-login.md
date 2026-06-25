# az login

> Masuk ke dalam platform Azure.
> Bagian dari `azure-cli` (juga dikenal sebagai `az`).
> Informasi lebih lanjut: <https://learn.microsoft.com/cli/azure/reference-index#az-login>.

- Lakukan proses masuk/login secara interaktif:

`az login`

- Masuk dengan suatu perwakilan layanan menggunakan suatu token rahasia klien:

`az login --service-principal {{[-u|--username]}} {{http://perwakilan-layanan-azure-cli}} {{[-p|--password]}} {{rahasia}} {{[-t|--tenant]}} {{seseorang.onmicrosoft.com}}`

- Masuk dengan suatu perwakilan layanan menggunakan suatu sertifikat klien:

`az login --service-principal {{[-u|--username]}} {{http://perwakilan-layanan-azure-cli}} {{[-p|--password]}} {{jalan/menuju/sertifikat.pem}} {{[-t|--tenant]}} {{seseorang.onmicrosoft.com}}`

- Masuk menggunakan identitas bawaan suatu sistem VM:

`az login {{[-i|--identity]}}`

- Masuk menggunakan identitas pengguna yang dipadankan ke dalam instansi VM:

`az login {{[-i|--identity]}} {{[-u|--username]}} /subscriptions/{{id_langganan}}/resourcegroups/{{grup_sumber_daya_saya}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{id_saya}}`
