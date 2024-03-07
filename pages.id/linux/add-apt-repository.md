# add-apt-repository

> Kelola definisi repositori `apt`.
> Informasi lebih lanjut: <https://manned.org/apt-add-repository>.

- Tambah repositori `apt` baru:

`add-apt-repository {{repositori}}`

- Hilangkan sebuah repositori `apt`:

`add-apt-repository --remove {{repositori}}`

- Memperbarui cache paket setelah menambahkan sebuah repositori:

`add-apt-repository --update {{repositori}}`

- Mengizinkan sumber paket untuk didownload dari repositori:

`add-apt-repository --enable-source {{repositori}}`
