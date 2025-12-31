# git changelog

> Buat laporan riwayat perubahan (changelog) dari daftar komit dan tag yang terkandung dalam repositori Git.
> Bagian dari `git-extras`.
> Informasi lebih lanjut: <https://manned.org/git-changelog>.

- Buat atau mutakhirkan file `History.md` berisikan riwayat komit sejak tag komit Git terkini:

`git changelog`

- Tampilkan daftar komit pada versi saat ini:

`git changelog {{[-l|--list]}}`

- Tampilkan daftar rentang komit yang dilakukan sejak tag komit `2.1.0` hingga komit terkini:

`git changelog {{[-l|--list]}} {{[-s|--start-tag]}} {{2.1.0}}`

- Tampilkan, dengan format yang mudah dibaca manusia, daftar rentang komit antara tag `0.5.0` dan `1.0.0`:

`git changelog {{[-s|--start-tag]}} {{0.5.0}} {{[-f|--final-tag]}} {{1.0.0}}`

- Tampilkan, dengan format yang mudah dibaca manusia, daftar rentang komit antara komit `0b97430` dan komit yang ditandai sebagai tag `1.0.0`:

`git changelog --start-commit {{0b97430}} {{[-f|--final-tag]}} {{1.0.0}}`

- Gunakan `CHANGELOG.md` untuk menyimpan informasi daftar perubahan tersebut:

`git changelog {{CHANGELOG.md}}`

- Hapus dan gantikan keseluruhan isi file perubahan dengan yang baru:

`git changelog {{[-p|--prune-old]}}`
