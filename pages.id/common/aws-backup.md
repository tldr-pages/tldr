# aws backup

> Layanan pencadangan untuk melindungi kumpulan layanan dan data terkait dalam Amazon Web Services.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/backup/index.html>.

- Tampilkan rincian BackupPlan (rencana pemulihan layanan yang dicadangkan) berdasarkan nomor induknya:

`aws backup get-backup-plan --backup-plan-id {{nomor_induk}}`

- Buat suatu BackupPlan dengan nama dan aturan tertentu:

`aws backup create-backup-plan --backup-plan {{rencana_pencadangan}}`

- Hapus suatu BackupPlan berdasarkan nomor induknya:

`aws backup delete-backup-plan --backup-plan-id {{nomor_induk}}`

- Tampilkan seluruh BackupPlan yang aktif dalam akun saat ini:

`aws backup list-backup-plans`

- Tampilkan rincian atas laporan pekerjaan pencadangan Anda:

`aws backup list-report-jobs`
