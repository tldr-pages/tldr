# history

> Tampilkan riwayat penugasan baris perintah (command-line).
> Informasi lebih lanjut: <https://www.gnu.org/software/bash/manual/bash.html#index-history>.

- Tampilkan riwayat penugasan baris perintah beserta angka baris:

`history`

- Tampilkan 20 perintah tugas terakhir (di Zsh perintah ini menampilkan semua perintah-perintah sejak dari baris ke-20):

`history {{20}}`

- Tampilkan riwayat dengan format tanggal dan waktu tertentu (hanya tersedia dalam Zsh):

`history -{{d|f|i|E}}`

- Hapus seluruh riwayat perintah penugasan (hanya untuk sesi shell Bash saat ini):

`history -c`

- Tulis ulang berkas dengan riwayat sesi shell Bash saat ini (seringkali dikombinasikan dengan `history -c` untuk menghapus riwayat):

`history -w`

- Hapus entri riwayat pada offset tertentu:

`history -d {{offset}}`
