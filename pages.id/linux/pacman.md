# pacman

> Manajer paket untuk Arch Linux.
> Beberapa sub-perintah seperti `pacman sync` memiliki dokumentasi penggunaannya sendiri.
> Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Memperbarui daftar paket yang tersedia dan memperbarui semua paket ke versi yang terbaru:

`sudo pacman -Syu`

- Menginstal paket baru:

`sudo pacman -S {{name_paket}}`

- Menghapus paket dan dependensinya:

`sudo pacman -Rs {{nama_paket}}`

- Mencari paket dalam database menggunakan regular expression atau kata kunci:

`pacman -Ss "{{kata_kunci}}"`

- Memperlihatakan seluruh daftar paket yang terpasang beserta versinya:

`pacman -Q`

- Memperlihatakan daftar paket beserta versinya yang dipasang secara eksplisit:

`pacman -Qe`

- Memperlihatkan daftar paket yang tidak dibutuhkan (dependensi yang terpasang namun tidak dibutuhkan oleh paket lain):

`pacman -Qtdq`

- Mengosongkan seluruh pacman cache:

`sudo pacman -Scc`
