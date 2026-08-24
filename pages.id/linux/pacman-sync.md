# pacman --sync

> Kegunaan manajer paket Arch Linux.
> Lihat juga: `pacman`.
> Informasi lebih lanjut: <https://manned.org/pacman.8>.

- Pasang suatu paket:

`sudo pacman -S {{nama_paket}}`

- Sinkronkan dan perbarui semua paket (tambahkan `--downloadonly` untuk unduh paket dan tidak memperbarui-nya):

`sudo pacman -Syu`

- Perbarui semua paket dan instal paket baru tanpa konfirmasi:

`sudo pacman -Syu --noconfirm {{nama_paket}}`

- Cari paket dalam database berdasarkan `regex` atau kata kunci:

`pacman -Ss "{{pola_pencarian}}"`

- Tampilkan [i]nformasi suatu paket:

`pacman -Si {{nama_paket}}`

- Timpa file yang bentrok selama pembaruan paket:

`sudo pacman -Syu --overwrite {{jalan/menuju/berkas}}`

- Hapus kumpulan paket dan repositori yang tidak terpakai dari cache (gunakan opsi flag `Scc` untuk hapus seluruh paket):

`sudo pacman -Sc`

- Tentukan versi paket yang hendak dipasang:

`sudo pacman -S {{nama_paket}}={{versi}}`
