# systemctl

> Kelola sistem systemd dan manajer layanan (service manager).
> beberpaa subperintah seperti `disable`, `status`, `reboot`, dll. memiliki dokumentasi penggunaannya sendiri.
> Informasi lebih lanjut: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html>.


- Tampilkan semua layanan (sevice) yang sedang berjalan: 

`systemctl status`

- Tampilkan daftar unit yang gagal dijalankan(failed): 

`systemctl --failed`

- Mulai/Hentikan/Mulai ulang/Muat ulang/Tampilkan status suatu layanan:

`systemctl {{start|stop|restart|reload|status}} {{unit}}`

- Aktifkan/Nonaktifkan unit agar berjalan secara otomatis saat sistem menyala (bootup):

`systemctl {{enable|disable}} {{unit}}`

- Muat ulang konfigurasi systemd untuk memindai unit baru atau yang telah diubah:

`systemctl daemon-reload`

- Periksa apakah suatu unit sedang aktif/diaktifkan saat boot/gagal:

`systemctl {{is-active|is-enabled|is-failed}} {{unit}}`

- Tampilkan semua unit service/socket/automount berdasarkan status berjalan atau gagal:

`systemctl list-units {{[-t|--type]}} {{service|socket|automount|...}} --state {{failed|running}}`

- Tampilkan isi dan jalur absolut dari berkas unit atau lakukan penyuntingan terhadapnya:

`systemctl {{cat|edit}} {{unit}}`
