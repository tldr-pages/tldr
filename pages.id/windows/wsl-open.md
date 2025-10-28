# wsl-open

> Buka suatu berkas atau URL dari lingkungan dalam Subsistem Windows untuk Linux (WSL) di dalam aplikasi GUI default pengguna di dalam Windows.
> Informasi lebih lanjut: <https://gitlab.com/4U6U57/wsl-open>.

- Buka direktori saat ini di dalam Windows Explorer:

`wsl-open {{.}}`

- Buka suatu URL di dalam aplikasi peramban web (browser) yang diatur sebagai default dalam Windows:

`wsl-open {{https://example.com}}`

- Buka suatu berkas di dalam aplikasi yang diatur sebagai default dalam Windows:

`wsl-open {{jalan\menuju\berkas}}`

- Gunakan `wsl-open` sebagai peramban web default dalam lingkungan syel WSL (sehingga seluruh tautan dalam lingkungan akan dibuka melalui `wsl-open`):

`wsl-open -w`

- Tampilkan informasi bantuan:

`wsl-open -h`
