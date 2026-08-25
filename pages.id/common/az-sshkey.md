# az sshkey

> Kelola kumpulan kunci publik SSH dengan instansi mesin virtual (VM).
> Bagian dari `azure-cli` (juga dikenal sebagai `az`).
> Informasi lebih lanjut: <https://learn.microsoft.com/cli/azure/sshkey>.

- Buat suatu kunci SSH baru:

`az sshkey create --name {{nama}} {{[-g|--resource-group]}} {{grup_sumber_daya}}`

- Unggah suatu kunci publik SSH:

`az sshkey create --name {{nama}} {{[-g|--resource-group]}} {{grup_sumber_daya}} --public-key "{{@jalan/menuju/kunci.pub}}"`

- Tampilkan daftar kunci publik SSH yang terdaftar:

`az sshkey list`

- Tampilkan informasi mengenai suatu kunci publik SSH terdaftar:

`az sshkey show --name {{nama}} {{[-g|--resource-group]}} {{grup_sumber_daya}}`
