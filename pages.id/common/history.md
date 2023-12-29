# history

> Sejarah command-line.
> Informasi lebih lanjut: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Tampilkan sejarah perintah-perintah dengan angka baris:

`history`

- Tampilkan 20 perintah-perintah terakhir (di `zsh` perintah ini menampilkan semua perintah-perintah sejak dari baris ke-20):

`history {{20}}`

- Hapus sejarah perintah-perintah (hanya untuk sesi shell `bash` saat ini):

`history -c`

- Tulis ulang file sejarah dengan sejarah sesi shell `bash` saat ini (seringkali dikombinasikan dengan `history -c` untuk menghapus sejarah):

`history -w`

- Hapus entri sejarah pada offset tertentu:

`history -d {{offset}}`
