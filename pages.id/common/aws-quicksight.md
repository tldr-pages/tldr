# aws quicksight

> Buat, hapus, tampilkan daftar, cari, dan perbarui entitas-entitas AWS QuickSight.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- Tampilkan kumpulan dataset:

`aws quicksight list-data-sets --aws-account-id {{id_akun_aws}}`

- Tampilkan daftar pengguna:

`aws quicksight list-users --aws-account-id {{id_akun_aws}} --namespace default`

- Tampilkan daftar kelompok:

`aws quicksight list-groups --aws-account-id {{id_akun_aws}} --namespace default`

- Tampilkan daftar dasbor:

`aws quicksight list-dashboards --aws-account-id {{id_akun_aws}}`

- Tampilkan informasi terperinci mengenai suatu dataset:

`aws quicksight describe-data-set --aws-account-id {{id_akun_aws}} --data-set-id {{id_data_set}}`

- Tampilkan siapa yang mendapat hak akses dan hak kegiatan terhadap suatu dataset:

`aws quicksight describe-data-set-permissions --aws-account-id {{id_akun_aws}} --data-set-id {{id_data_set}}`
