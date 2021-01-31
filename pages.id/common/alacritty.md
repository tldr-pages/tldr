# alacritty

> Lintas platform, terakselerasi GPU terminal emulator.
> Informasi lebih lanjut: <https://github.com/jwilm/alacritty>.

- Membuka jendela alacritty baru:

`alacritty`

- Menjalankan alacritty pada direktori tertentu:

`alacritty --working-directory {{alamat/ke/direktori}}`

- Menjalankan perintah di jendela alacritty baru:

`alacritty -e {{perintah}}`

- Menentukan berkas konfigurasi alternatif (nilai default `$XDG_CONFIG_HOME/alacritty/alacritty.yml`):

`alacritty --config-file {{alamat/ke/konfigurasi.yml}}`

- Menjalankan dengan mengaktifkan pemuatan ulang konfigurasi secara langsung/otomatis(dapat juga diaktifkan secara default di `alacritty.yml`):

`alacritty --live-config-reload --config-file {{alamat/ke/konfigurasi.yml}}`
