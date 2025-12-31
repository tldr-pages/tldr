# frps

> Buat suatu peladen pelayan jaringan proksi terbalik (reverse proksi).
> Bagian dari `frp`.
> Informasi lebih lanjut: <https://github.com/fatedier/frp>.

- Jalankan layanan peladen, menggunakan berkas konfigurasi bawaan/default (diasumsikan merupakan berkas `frps.ini` yang terletak pada direktori saat ini):

`frps`

- Jalankan layanan menggunakan berkas konfigurasi dengan format terbaru berbasis TOML (`frps.toml` daripada `frps.ini`) pada direktori saat ini:

`frps {{[-c|--config]}} ./frps.toml`

- Start the service, using a specific configuration file:

`frps {{[-c|--config]}} {{jalan/menuju/berkas}}`

- Periksa apakah isi suatu berkas konfigurasi menggunakan format yang valid:

`frps verify {{[-c|--config]}} {{jalan/menuju/berkas}}`

- Tampilkan isi skrip shell yang perlu dijalankan untuk mengaktifkan fitur penyelesaian perintah otomatis (autocomplete) bagi Bash, fish, PowerShell, maupun Zsh:

`frps completion {{bash|fish|powershell|zsh}}`

- Tampilkan informasi versi:

`frps {{[-v|--version]}}`
