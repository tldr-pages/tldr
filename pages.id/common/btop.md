# btop

> Program pengawasan sumber daya komputer yang dapat menunjukkan informasi pemanfaatan CPU, memori, penyimpanan, jaringan, dan proses sistem operasi.
> Sebuah program `bpytop` versi C++.
> Lihat juga: `btm`, `glances`, `atop`, `htop`, `top`, `sensors`.
> Informasi lebih lanjut: <https://github.com/aristocratos/btop#command-line-options>.

- Jalankan `btop`:

`btop`

- Jalankan `btop` dengan preset pengaturan tertentu:

`btop {{[-p|--preset]}} {{0..9}}`

- Jalankan `btop` dalam mode TTY menggunakan 16 pilihan warna dan simbol grafik ramah TTY:

`btop {{[-t|--tty]}}`

- Jalankan `btop` menggunakan 256 pilihan warna saja daripada mode warna 24-bit:

`btop {{[-l|--low-color]}}`

- Tentukan durasi pembaruan data sebesar 500 milidetik:

`btop {{[-u|--update]}} 500`

- Keluar dari `btop`:

`<q>`

- Tampilkan bantuan:

`btop {{[-h|--help]}}`
