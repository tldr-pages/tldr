# touch

> Mengubah waktu akses (atime) dan waktu modifikasi (mtime) dari sebuah file.
> Informasi lebih lanjut: <https://manned.org/man/freebsd-13.1/touch>.

- Membuat file baru yang kosong atau mengubah waktu file yang telahj ada ke waktu sekarang:

`touch {{nama_file}}`

- Mengatur waktu sebuah file ke tanggal dan jam tertentu:

`touch -t {{YYYYMMDDHHMM.SS}} {{nama_file}}`

- Menggunakan waktu dari satu file untuk mengatur waktu file yang lain:

`touch -r {{nama_file}} {{nama_file2}}`
