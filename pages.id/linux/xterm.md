# xterm

> Emulator terminal untuk sistem window X.
> Informasi lebih lanjut: <https://manned.org/xterm>.

- Membuka terminal dengan judul `Example`:

`xterm -T {{Example}}`

- Membuka terminal dalam mode fullscreen:

`xterm -fullscreen`

- Membuka terminal dengan warna background biru tua dan warna foreground (warna font) kuning:

`xterm -bg {{darkblue}} -fg {{yellow}}`

- Membuka terminal dengan 100 karakter per baris dan 35 baris, di posisi layar x=200px, y=20px:

`xterm -geometry {{100}}x{{35}}+{{200}}+{{20}}`

- Membuka terminal dengan font Serif dengan ukuran font sebesar 20:

`xterm -fa {{'Serif'}} -fs {{20}}`
