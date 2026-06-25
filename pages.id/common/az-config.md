# az config

> Atur konfigurasi program Azure CLI.
> Bagian dari `azure-cli` (juga dikenal sebagai `az`).
> Informasi lebih lanjut: <https://learn.microsoft.com/cli/azure/config>.

- Tampilkan seluruh konfigurasi:

`az config get`

- Tampilkan seluruh konfigurasi dalam suatu bagian (section):

`az config get {{nama_bagian}}`

- Setel suatu konfigurasi:

`az config set {{nama_konfigurasi}}={{nilai}}`

- Hapus setelan suatu konfigurasi:

`az config unset {{nama_konfigurasi}}`
