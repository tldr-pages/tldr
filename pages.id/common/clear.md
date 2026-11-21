# clear

> Bersihkan layar terminal.
> Informasi lebih lanjut: <https://manned.org/clear>.

- Bersihkan layar:

`clear`

- Bersihkan layar namun jangan mengatur ulang penyangga guliran barisan teks (setara dengan menekan `<Ctrl l>` dalam Bash):

`clear -x`

- Berikan informasi jenis program terminal yang dipakai untuk membersihkan layar (secara bawaan bernilai nilai variabel lingkungan `$TERM`):

`clear -T {{jenis_terminal}}`

- Tampilkan versi program `ncurses` yang digunakan oleh `clear`:

`clear -V`
