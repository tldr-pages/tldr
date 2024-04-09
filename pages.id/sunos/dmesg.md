# dmesg

> Tulis pesan kernel ke `stdout`.
> Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1m/dmesg>.

- Tampilkan pesan kernel:

`dmesg`

- Tampilkan berapa memori fisik yang tersedia di sistem ini:

`dmesg | grep -i memory`

- Tampilkan pesan kernel 1 halaman dalam 1 waktu:

`dmesg | less`
