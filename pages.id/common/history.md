# history

> Sejarah command-line.
> Informasi lebih lanjut: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Menampilkan sejarah perintah-perintah dengan angka baris:

`history`

- Menampilkan 20 perintah-perintah terakhir (di `zsh` perintah ini menampilkan semua perintah-perintah sejak dari baris ke-20):

`history {{20}}`

- Menghapus sejarah perintah-perintah (hanya untuk sesi shell `bash` saat ini):

`history -c`

- Menulis ulang file sejarah dengan sejarah sesi shell `bash` saat ini (seringkali dikombinasikan dengan `history -c` untuk menghapus sejarah):

`history -w`

- Menghapus entri sejarah pada offset tertentu:

`history -d {{offset}}`
