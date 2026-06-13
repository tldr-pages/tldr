# alien

> Konversikan berbagai paket instalasi ke format lain.
> Lihat juga: `debtap`.
> Informasi lebih lanjut: <https://manned.org/alien>.

- Konversikan file instalasi tertentu ke format Debian (ekstensi `.deb`):

`sudo alien {{[-d|--to-deb]}} {{jalan/menuju/berkas}}`

- Konversikan file instalasi tertentu ke format Red Hat (ekstensi `.rpm`):

`sudo alien {{[-r|--to-rpm]}} {{jalan/menuju/berkas}}`

- Konversikan file instalasi tertentu ke file instalasi Slackware (ekstensi `.tgz`):

`sudo alien {{[-t|--to-tgz]}} {{jalan/menuju/berkas}}`

- Konversikan file instalasi tertentu ke format Debian dan install di sistem:

`sudo alien {{[-d|--to-deb]}} {{[-i|--install]}} {{jalan/menuju/berkas}}`
