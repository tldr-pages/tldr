# apptainer cache

> Kelola cache Apptainer lokal.
> Informasi lebih lanjut: <https://apptainer.org/docs/user/main/cli/apptainer_cache.html>.

- Tampilkan semua image kontainer dalam cache:

`apptainer cache list`

- Tampilkan image kontainer dalam cache dengan informasi detail:

`apptainer cache list {{[-v|--verbose]}}`

- Tampilkan hanya jenis cache tertentu:

`apptainer cache list {{[-T|--type]}} {{library|oci|shub|blob|...}}`

- Bersihkan seluruh cache:

`apptainer cache clean`

- Bersihkan hanya jenis cache tertentu:

`apptainer cache clean {{[-T|--type]}} {{library|oci|shub|blob|...}}`

- Bersihkan entri cache yang usianya lebih lama dari jumlah hari tertentu:

`apptainer cache clean {{[-D|--days]}} {{days}}`

- Tampilkan pratinjau tentang apa yang akan dibersihkan tanpa menghapus apa pun:

`apptainer cache clean {{[-n|--dry-run]}}`

- Bersihkan secara paksa tanpa konfirmasi:

`apptainer cache clean {{[-f|--force]}}`
