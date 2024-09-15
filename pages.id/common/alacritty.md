# alacritty

> Lintas platform, terakselerasi GPU terminal emulator.
> Informasi lebih lanjut: <https://github.com/alacritty/alacritty>.

- Buka jendela Alacritty baru:

`alacritty`

- Jalankan Alacritty pada direktori tertentu:

`alacritty --working-directory {{jalan/menuju/direktori}}`

- Jalankan perintah di jendela Alacritty baru:

`alacritty -e {{perintah}}`

- Gunakan berkas konfigurasi alternatif untuk memuat program (nilai default `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{jalan/menuju/konfigurasi.toml}}`

- Jalankan dan aktifkan fitur muat ulang konfigurasi secara langsung/otomatis (dapat juga diaktifkan secara default di `alacritty.toml`):

`alacritty --live-config-reload --config-file {{jalan/menuju/konfigurasi.toml}}`
