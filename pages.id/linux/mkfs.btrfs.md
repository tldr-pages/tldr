# mkfs.btrfs

> Membuat sistem file btrfs.
> Default ke `raid1`, yang menyatakan 2 salinan sebuah blok data disebar ke 2 perangkat yang berbeda.
> Informasi lebih lanjut: <https://btrfs.wiki.kernel.org/index.php/Manpage/mkfs.btrfs>.

- Membuat sebuah sistem file btrfs di satu perangkat:

`sudo mkfs.btrfs --metadata single --data single {{/dev/sda}}`

- Membuat sebuah sistem file btrfs di beberapa perangkat dengan raid1:

`sudo mkfs.btrfs --metadata raid1 --data raid1 {{/dev/sda}} {{/dev/sdb}} {{/dev/sdN}}`

- Mengatur sebuah label untuk sistem file:

`sudo mkfs.btrfs --label "{{label}}" {{/dev/sda}} [{{/dev/sdN}}]`
