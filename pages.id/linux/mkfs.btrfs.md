# mkfs.btrfs

> Pasang strategi manajemen berkas terhadap perangkat penyimpanan menggunakan sistem BTRFS.
> Default ke `raid1`, yang menyatakan 2 salinan sebuah blok data disebar ke 2 perangkat yang berbeda.
> Informasi lebih lanjut: <https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html>.

- Buat instalasi BTRFS baru terhadap suatu partisi kosong:

`sudo mkfs.btrfs {{/dev/sdXY}}`

- Buat instalasi BTRFS di suatu perangkat penyimpanan:

`sudo mkfs.btrfs {{[-m|--metadata]}} single {{[-d|--data]}} single {{/dev/sdX}}`

- Buat instalasi BTRFS yang mencakup beberapa perangkat penyimpanan dengan raid1:

`sudo mkfs.btrfs {{[-m|--metadata]}} raid1 {{[-d|--data]}} raid1 {{/dev/sdX /dev/sdY /dev/sdZ ...}}`

- Tentukan label nama untuk pemasangan instalasi manajemen berkas:

`sudo mkfs.btrfs --label "{{label}}" {{/dev/sda}} [{{/dev/sdN}}]`

- Tangguhkan instalasi sistem manajemen berkas saat ini jika ditemukan dalam perangkat tersebut:

`sudo mkfs.btrfs {{[-f|--force]}} {{/dev/sdX}}`
