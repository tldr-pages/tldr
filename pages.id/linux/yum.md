# yum

> Utilitas manajemen paket untuk RHEL, Fedora, dan CentOS (untuk versi-versi yang lebih lama).
> Lihat <https://wiki.archlinux.org/title/Pacman/Rosetta> untuk daftar perintah dalam manajer paket lain yang menyerupai perintah `yum`.
> Informasi lebih lanjut: <https://manned.org/yum>.

- Pasang suatu paket:

`yum install {{nama_paket}}`

- Pasang paket dengan mengasumsikan jawaban [y]a untuk semua pertanyaan (juga berfungsi dengan perintah pembaruan, sangat berguna untuk pembaruan otomatis):

`yum -y install {{nama_paket}}`

- Cari sebuah paket yang menyediakan suatu perintah tertentu:

`yum provides {{perintah}}`

- Hapus paket yang terpasang sebelumnya:

`yum remove {{paket}}`

- Tampilkan pembaruan yang tersedia untuk paket yang terpasang:

`yum check-update`

- Perbarui seluruh paket yang terpasang ke versi terbaru:

`yum upgrade`
