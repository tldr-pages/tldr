# pacman --sync

> Kegunaan manajer paket Arch Linux.
> Guarda anche: `pacman`.
> Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Instal paket baru:

`sudo pacman --sync {{nama_paket}}`

- Sinkronkan dan perbarui semua paket (tambahkan `--downloadonly` untuk unduh paket dan tidak memperbarui-nya):

`sudo pacman --sync --refresh --sysupgrade`

- Perbarui semua paket dan instal paket baru tanpa konfirmasi:

`sudo pacman --sync --refresh --sysupgrade --noconfirm {{nama_paket}}`

- Cari paket dalam database berdasarkan regular expression atau kata kunci:

`pacman --sync --search "{{pola_pencarian}}"`

- Tampilkan informasi sebuah paket:

`pacman --sync --info {{nama_paket}}`

- Timpa file yang bentrok selama pembaruan paket:

`sudo pacman --sync --refresh --sysupgrade --overwrite {{jalan/menuju/file}}`

- Sinkronkan dan perbarui semua paket, namun abaikan paket tertentu (dapat digunakan lebih dari sekali):

`sudo pacman --sync --refresh --sysupgrade --ignore {{nama_paket}}`

- Hapus paket yang tidak terpasang dan repositori yang tidak digunakan dari cache (gunakan dua tanda `--clean` untuk bersihkan semua paket):

`sudo pacman --sync --clean`
