# libreoffice

> Antarmuka baris perintah untuk LibreOffice, aplikasi perkantoran mahir dan gratis.
> Informasi lebih lanjut: <https://www.libreoffice.org/>.

- Buka suatu atau beberapa berkas dalam mode baca-saja (read-only):

`libreoffice --view {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Tampilkan isi suatu atau beberapa berkas:

`libreoffice --cat {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Cetak berkas menggunakan mesin pencetak (printer) tertentu:

`libreoffice --pt {{printer_name}} {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Konversi semua berkas `.doc` dalam direktori saat ini menuju PDF:

`libreoffice --convert-to pdf *.doc`
