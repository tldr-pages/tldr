# ar

> Buat, olah, dan ekstrak berkas dalam format arsip Unix. Biasanya dimanfaatkan untuk pustaka statis (`.a`) dan paket piranti lunak Debian (`.deb`).
> Lihat juga: `tar`.
> Informasi lebih lanjut: <https://manned.org/ar>.

- E[x]trak seluruh berkas dalam suatu arsip:

`ar x {{jalan/menuju/berkas.a}}`

- Lihat daf[t]ar isi dari suatu arsip:

`ar t {{jalan/menuju/berkas.ar}}`

- Gantikan ([r]eplace) atau tambahkan suatu berkas ke dalam arsip:

`ar r {{jalan/menuju/berkas.deb}} {{jalan/menuju/debian-binary jalan/menuju/control.tar.gz jalan/menuju/data.tar.xz ...}}`

- Ma[s]ukkan suatu berkas objek (setara dengan penggunaan `ranlib`):

`ar s {{jalan/menuju/berkas.a}}`

- Buat suatu arsip berisikan kumpulan berkas tertentu, dan suatu berkas daftar indeks para objek:

`ar rs {{jalan/menuju/berkas.a}} {{jalan/menuju/berkas1.o jalan/menuju/berkas2.o ...}}`
