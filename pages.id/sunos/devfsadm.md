# devfsadm

> Perintah administrasi untuk `/dev`. Kelola namespace `/dev`.
> Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Pindai piringan baru:

`devfsadm -c disk`

- Bersihkan semua tautan /dev yang beruntai dan memindai perangkat baru:

`devfsadm -C -v`

- Dry-run - luaran yang akan dirubah tapi tanpa membuat modifikasi:

`devfsadm -C -v -n`
