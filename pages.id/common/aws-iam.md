# aws iam

> Berinteraksi dengan Identity and Access Management (IAM), manajer untuk mengelola identitas dan akses layanan AWS secara aman.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/iam/>.

- Tampilkan daftar pengguna:

`aws iam list-users`

- Tampilkan daftar kebijakan:

`aws iam list-policies`

- Tampilkan daftar grup:

`aws iam list-groups`

- Dapatkan daftar pengguna dalam suatu grup:

`aws iam get-group --group-name {{nama_grup}}`

- Tampilkan deskripsi suatu kebijakan IAM:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{nama_kebijakan}}`

- Tampilkan daftar kunci akses:

`aws iam list-access-keys`

- Tampilkan daftar kunci akses untuk suatu pengguna:

`aws iam list-access-keys --user-name {{nama_pengguna}}`

- Tampilkan bantuan:

`aws iam help`
