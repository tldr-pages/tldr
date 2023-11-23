# yum

> Utilitas manajemen paket untuk RHEL, Fedora, dan CentOS (untuk versi-versi yang lebih lama).
> Untuk perintah-perintah setara dalam pengelola paket lainnya, lihat <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Informasi lebih lanjut: <https://manned.org/yum>.

- Instal sebuah paket baru:

`yum install {{nama_paket}}`

- Instal sebuah paket baru dan mengasumsikan jawaban [y]a untuk semua pertanyaan (juga berfungsi dengan perintah pembaruan, sangat berguna untuk pembaruan otomatis):

`yum -y install {{nama_paket}}`

- Cari sebuah paket yang menyediakan suatu perintah tertentu:

`yum provides {{perintah}}`

- Hapus paket yang terpasang sebelumnya:

`yum remove {{paket}}`

- Tampilkan pembaruan yang tersedia untuk paket yang terpasang:

`yum check-update`

- Perbarui seluruh paket yang terpasang ke versi terbaru:

`yum upgrade`
