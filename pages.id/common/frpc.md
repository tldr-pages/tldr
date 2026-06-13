# frpc

> Hubungkan perangkat menuju jaringan proksi yang diatur oleh suatu peladen/server `frps`.
> Bagian dari `frp`.
> Informasi lebih lanjut: <https://github.com/fatedier/frp>.

- Jalankan layanan klien, menggunakan berkas konfigurasi bawaan/default (diasumsikan merupakan berkas `frps.ini` yang terletak pada direktori saat ini):

`frpc`

- Jalankan layanan menggunakan berkas konfigurasi dengan format terbaru berbasis TOML (`frps.toml` daripada `frps.ini`) pada direktori saat ini:

`frpc {{[-c|--config]}} ./frps.toml`

- Start the service, using a specific configuration file:

`frpc {{[-c|--config]}} {{jalan/menuju/berkas}}`

- Periksa apakah isi suatu berkas konfigurasi menggunakan format yang valid:

`frpc verify {{[-c|--config]}} {{jalan/menuju/berkas}}`

- Tampilkan isi skrip shell yang perlu dijalankan untuk mengaktifkan fitur penyelesaian perintah otomatis (autocomplete) bagi Bash, fish, PowerShell, maupun Zsh:

`frpc completion {{bash|fish|powershell|zsh}}`

- Tampilkan informasi versi:

`frpc {{[-v|--version]}}`
