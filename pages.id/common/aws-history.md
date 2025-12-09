# aws history

> Tampilkan riwayat pemanggilan perintah dalam AWS CLI (fitur perekaman riwayat perintah AWS CLI harus diaktifkan terlebih dahulu).
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/history/>.

- Tampilkan daftar riwayat perintah yang dipanggil melalui AWS CLI beserta nomor induknya (command ID):

`aws history list`

- Tampilkan daftar kejadian yang berkaitan dengan suatu perintah berdasarkan nomor induknya (command ID):

`aws history show {{command_id}}`
