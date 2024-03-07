# add-apt-repository

> Kelola definisi repositori `apt`.
> Informasi lebih lanjut: <https://manned.org/apt-add-repository>.

- Tambah repositori `apt` baru:

`add-apt-repository {{repositori}}`

- Hilangkan sebuah repositori `apt`:

`add-apt-repository --remove {{repositori}}`

- Perbarui cache paket setelah menambahkan sebuah repositori:

`add-apt-repository --update {{repositori}}`

- Izinkan sumber paket untuk diunduh dari repositori:

`add-apt-repository --enable-source {{repositori}}`
