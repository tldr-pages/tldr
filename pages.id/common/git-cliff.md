# git cliff

> Suatu pembuat teks daftar perubahan (changelog) yang mudah diatur.
> Informasi lebih lanjut: <https://git-cliff.org/docs/usage/args>.

- Buat suatu pesan changelog dari seluruh komit dalam suatu repositori Git, kemudian simpan ke dalam `CHANGELOG.md`:

`git cliff > {{CHANGELOG.md}}`

- Buat suatu pesan changelog atas komit-komit yang dimulai sejak tag terkini dan tampilkan pesan menuju `stdout`:

`git cliff {{[-l|--latest]}}`

- Buat suatu pesan changelog atas komit-komit yang masuk ke dalam tag saat ini (gunakan `git checkout` atas suatu tag sebelum melakukan ini):

`git cliff --current`

- Buat suatu pesan changelog atas komit-komit yang tidak termasuk dalam tag apapun:

`git cliff {{[-u|--unreleased]}}`

- Tulis berkas konfigurasi bawaan menuju `cliff.toml` dalam direktori saat ini:

`git cliff {{[-i|--init]}}`
