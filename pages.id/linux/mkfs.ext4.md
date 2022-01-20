# mkfs.ext4

> Membuat sistem file ext4 didalam sebuah partisi.
> Informasi lebih lanjut: <https://manned.org/mkfs.ext4>.

- Membuat sistem file ext4 di dalam partisi 1 di perangkat B (`sdb1`):

`sudo mkfs.ext4 {{/dev/sdb1}}`

- Membuat sistem file ext4 dengan label volume:

`sudo mkfs.ext4 -L {{label_volume}} {{/dev/sdb1}}`
