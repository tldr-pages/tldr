# btop

> CPU, bellek, diskler, ağ ve süreçler hakkında bilgi gösteren bir kaynak izleyici.
> `bpytop` aracının C++ sürümüdür.
> Ayrıca bakınız: `btm`, `glances`, `atop`, `htop`, `top`, `sensors`.
> Daha fazla bilgi: <https://github.com/aristocratos/btop#command-line-options>.

- Programı başlat:

`btop`

- Programı belirtilen ayar önayarıyla başlat:

`btop {{[-p|--preset]}} {{0..9}}`

- Programı 16 renk ve TTY dostu grafik simgeleri kullanan TTY modunda başlat:

`btop {{[-t|--tty]}}`

- Programı 24-bit renk modu yerine 256-renk modunda başlat:

`btop {{[-l|--low-color]}}`

- Güncelleme sıklığını 500 milisaniye olarak ayarla:

`btop {{[-u|--update]}} 500`

- Programdan çık:

`<q>`

- Yardımı görüntüle:

`btop {{[-h|--help]}}`
