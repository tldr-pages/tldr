# alacritty

> Lintas platform, terakselerasi GPU terminal emulator.
> Informasi lebih lanjut: <https://github.com/alacritty/alacritty>.

- Membuka jendela Alacritty baru:

`alacritty`

- Menjalankan Alacritty pada direktori tertentu:

`alacritty --working-directory {{alamat/ke/direktori}}`

- Menjalankan perintah di jendela Alacritty baru:

`alacritty -e {{perintah}}`

- Menentukan berkas konfigurasi alternatif (nilai default `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{alamat/ke/konfigurasi.toml}}`

- Menjalankan dengan mengaktifkan pemuatan ulang konfigurasi secara langsung/otomatis (dapat juga diaktifkan secara default di `alacritty.toml`):

`alacritty --live-config-reload --config-file {{alamat/ke/konfigurasi.toml}}`
