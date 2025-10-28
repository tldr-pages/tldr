# alacritty

> Lintas platform, terakselerasi GPU terminal emulator.
> Informasi lebih lanjut: <https://manned.org/alacritty>.

- Buka jendela Alacritty baru:

`alacritty`

- Jalankan Alacritty sebagai peladen daemon (tanpa membuat jendela baru):

`alacritty --daemon`

- Buat jendela baru pada proses Alacritty yang sedang berjalan:

`alacritty msg create-window`

- Jalankan Alacritty pada direktori tertentu (dapat juga bekerja dalam `alacritty msg create-window`):

`alacritty --working-directory {{jalan/menuju/direktori}}`

- Jalankan perintah di jendela Alacritty baru (dapat juga bekerja dalam `alacritty msg create-window`):

`alacritty -e {{perintah}}`

- Gunakan berkas konfigurasi alternatif untuk memuat program (nilai default `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{jalan/menuju/konfigurasi.toml}}`
