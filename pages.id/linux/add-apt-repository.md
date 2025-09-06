# add-apt-repository

> Kelola definisi repositori `apt`.
> Informasi lebih lanjut: <https://manned.org/add-apt-repository>.

- Tambah repositori `apt` baru:

`add-apt-repository {{repositori}}`

- Hilangkan sebuah repositori `apt`:

`add-apt-repository {{[-r|--remove]}} {{repositori}}`

- Perbarui cache paket setelah menambahkan sebuah repositori:

`add-apt-repository --update {{repositori}}`

- Izinkan sumber paket untuk diunduh dari repositori:

`add-apt-repository {{[-s|--enable-source]}} {{repositori}}`
