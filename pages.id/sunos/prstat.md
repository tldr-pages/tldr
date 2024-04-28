# prstat

> Laporkan statistik proses aktif.
> Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1m/prstat>.

- Periksa semua proses dan laporan statistik yang diurutkan berdasarkan tingkat penggunaan CPU:

`prstat`

- Periksa semua proses dan laporan statistik yang disortir berdasarkan penggunaan memori:

`prstat -s rss`

- Laporkan ringkasan total penggunaan untuk tiap user:

`prstat -t`

- Laporkan informasi pengukuran proses microstate:

`prstat -m`

- Cetak daftar penggunaan CPU 5 proses teratas tiap 1 detik:

`prstat -c -n {{5}} -s cpu {{1}}`
