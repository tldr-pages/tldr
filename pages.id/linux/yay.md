# yay

> Yet Another Yogurt: bangun dan pasang paket piranti lunak dari Arch User Repository.
> Lihat juga: `pacman`.
> Informasi lebih lanjut: <https://github.com/Jguer/yay#first-use>.

- Cari dan pasang kumpulan paket dari kumpulan repositori dan AUR secara interaktif:

`yay {{nama_paket|kata_pencarian}}`

- Padankan daftar paket dan perbarui seluruh paket dari kumpulan repositori dan AUR:

`yay`

- Pasang baru suatu paket dari kumpulan repositori dan AUR dan tanpa perlu mengonfirmasi transaksi langkah pemasangan:

`yay -S {{paket}} --noconfirm`

- Hapus suatu paket terpasang beserta seluruh paket ketergantungannya dan berkas konfigurasinya:

`yay -Rns {{paket}}`

- Cari paket berdasarkan kata kunci tertentu dari kumpulan repositori dan AUR:

`yay -Ss {{kata_kunci}}`

- Hapus para paket yatim yang terpasang (yang sebelumnya terpasang sebagai ketergantungan namun kini tak dibutuhkan oleh paket apapun):

`yay -Yc`

- Bersihkan data cache `pacman` dan `yay` (berupa versi-versi paket lawas yang ditahan untuk proses pemulihan dengan rollback dan downgrade):

`yay -Scc`

- Tampilkan statistik pemasangan paket beserta kesehatan sistem operasi:

`yay -Ps`
