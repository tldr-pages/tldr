# aws rds

> Gunakan AWS Relational Database Service, suatu layanan untuk membuat, menjalankan, dan membesarkan operasional sistem pangkalan data relasional.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/rds/>.

- Tampilkan bantuan untuk suatu subperintah RDS:

`aws rds {{subperintah}} help`

- Hentikan suatu instansi RDS:

`aws rds stop-db-instance --db-instance-identifier {{nomor_induk_instansi}}`

- Jalankan suatu instansi RDS:

`aws rds start-db-instance --db-instance-identifier {{nomor_induk_instansi}}`

- Ubah suatu instansi RDS:

`aws rds modify-db-instance --db-instance-identifier {{nomor_induk_instansi}} {{kumpulan_parameter}} --apply-immediately`

- Terapkan pembaruan untuk suatu instansi RDS:

`aws rds apply-pending-maintenance-action --resource-identifier {{arn_pangkalan_data}} --apply-action {{system-update}} --opt-in-type {{immediate}}`

- Ubah nomor induk suatu instansi:

`aws rds modify-db-instance --db-instance-identifier {{nomor_induk_lama_instansi}} --new-db-instance-identifier {{nomor_induk_baru_instansi}}`

- Nyalakan ulang suatu instansi:

`aws rds reboot-db-instance --db-instance-identifier {{nomor_induk_instansi}}`

- Hapus suatu instansi:

`aws rds delete-db-instance --db-instance-identifier {{nomor_induk_instansi}} --final-db-snapshot-identifier {{nomor_induk_snapshot}} --delete-automated-backups`
