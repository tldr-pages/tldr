# rm

> Hapus berkas atau direktori.
> Lihat juga: `rmdir`.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/rm>.

- Hapus berkas dari lokasi manapun:

`rm {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Hapus berkas dari lokasi manapun dengan mengabaikan nama-nama file yang tidak ditemukan:

`rm -f {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Hapus banyak berkas secara [i]nteraktif, dengan meminta konfirmasi sebelum setiap penghapusan:

`rm -i {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Hapus berkas dengan mode [v]erbose, mencetak pesan untuk setiap file yang terhapus:

`rm -v {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Hapus direktori dan semua subdirektorinya secara [r]ekursif:

`rm -r {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`
