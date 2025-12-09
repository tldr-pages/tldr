# aws configure

> Atur konfigurasi penggunaan AWS CLI.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Atur konfigurasi AWS CLI secara interaktif (akan membuat konfigurasi baru atau memutakhirkan konfigurasi bawaan):

`aws configure`

- Atur konfigurasi bagi suatu profil pengguna AWS CLI (akan membuat profil pengguna baru atau memutakhirkannya):

`aws configure --profile {{nama_profil}}`

- Tampilkan nilai terhadap suatu variabel konfigurasi:

`aws configure get {{nama_variabel}}`

- Tampilkan nilai terhadap suatu variabel konfigurasi pada suatu profil pengguna:

`aws configure get {{nama_variabel}} --profile {{nama_profil}}`

- Atur nilai suatu variabel konfigurasi:

`aws configure set {{nama_variabel}} {{nilai}}`

- Atur nilai suatu variabel konfigurasi bagi suatu profil pengguna:

`aws configure set {{nama_variabel}} {{nilai}} --profile {{nama_profil}}`

- Tampilkan seluruh konfigurasi yang disimpan:

`aws configure list`

- Tampilkan seluruh konfigurasi yang disimpan bagi suatu profil pengguna:

`aws configure list --profile {{nama_profil}}`
