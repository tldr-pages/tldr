# aws cognito-idp

> Atur suatu kumpulan pengguna (user pool) Amazon Cognito beserta pengguna dan grup di dalamnya, dan lakukan autentikasi.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/>.

- Buat suatu kumpulan pengguna (pool) Cognito baru:

`aws cognito-idp create-user-pool --pool-name {{nama}}`

- Tampilkan seluruh kumpulan pengguna:

`aws cognito-idp list-user-pools --max-results {{10}}`

- Hapus suatu kumpulan pengguna:

`aws cognito-idp delete-user-pool --user-pool-id {{id_kumpulan_pengguna}}`

- Buat suatu pengguna baru dalam suatu kumpulan:

`aws cognito-idp admin-create-user --username {{username}} --user-pool-id {{id_kumpulan_pengguna}}`

- Tampilkan daftar pengguna dalam suatu kumpulan:

`aws cognito-idp list-users --user-pool-id {{id_kumpulan_pengguna}}`

- Hapus suatu pengguna dari suatu kumpulan:

`aws cognito-idp admin-delete-user --username {{username}} --user-pool-id {{id_kumpulan_pengguna}}`
