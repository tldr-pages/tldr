# a2ping

> Ubah file gambar menjadi EPS atau PDF.
> Informasi lebih lanjut: <https://manned.org/a2ping>.

- Ubah sebuah gambar menjadi PDF (Catatan: Nama file output bersifat opsional):

`a2ping {{jalan/menuju/gambar.ext}} {{jalan/menuju/output.pdf}}`

- Kompres dokumen EPS atau PDF menggunakan metode tertentu:

`a2ping --nocompress {{none|zip|best|flate}} {{jalan/menuju/file}}`

- Pindai HiResBoundingBox jika ditemukan (akan dipindai secara default):

`a2ping --nohires {{jalan/menuju/file}}`

- Izinkan konten halaman berada melewati batas bawah dan kiri (tidak diizinkan secara default):

`a2ping --below {{jalan/menuju/file}}`

- Berikan opsi/argumen tambahan untuk `gs`:

`a2ping --gsextra {{argumen_tambahan_gs}} {{jalan/menuju/file}}`

- Berikan opsi/argumen tambahan untuk program lainnya (seperti `pdftops`):

`a2ping --extra {{arguments}} {{jalan/menuju/file}}`

- Tampilkan informasi bantuan:

`a2ping -h`
