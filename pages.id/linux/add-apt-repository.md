# add-apt-repository

> Mengelola definisi repositori `apt`.
> Informasi lebih lanjut: <https://manned.org/apt-add-repository>.

- Menambah repositori `apt` baru:

`add-apt-repository {{repository_spec}}`

- Menghilangkan sebuah repositori `apt`:

`add-apt-repository --remove {{repository_spec}}`

- Memperbarui cache paket setelah menambahkan sebuah repositori:

`add-apt-repository --update {{repository_spec}}`

- Mengizinkan sumber paket untuk didownload dari repositori:

`add-apt-repository --enable-source {{repository_spec}}`
