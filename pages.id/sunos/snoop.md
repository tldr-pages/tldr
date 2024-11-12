# snoop

> Pengendus paket jaringan.
> Perintah setara tcpdump untuk SunOS.
> Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Tangkap paket pada antarmuka jaringan tertentu:

`snoop -d {{e1000g0}}`

- Simpan paket yang tertangkap pada sebuah berkas dari pada menampilkannya:

`snoop -o {{jalan/menuju/berkas}}`

- Tampilkan rangkuman lapisan protokol paket-paket dari sebuah berkas dengan rinci:

`snoop -V -i {{jalur/ke/berkas}}`

- Tangkap paket jaringan yang datang dari sebuah nama host dan pergi ke port yang ditentukan:

`snoop to port {{port}} from host {{nama_host}}`

- Tangkap dan tampilkan sebuah hex-dump dari pertukaran paket jaringan di antara 2 alamat IP:

`snoop -x0 -p4 {{ip1}} {{ip2}}`
