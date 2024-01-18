# rm

> Hapus file atau direktori.
> Lihat juga: `rmdir`.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/rm>.

- Hapus file dari lokasi manapun:

`rm {{jalan/menuju/file1 jalan/menuju/file2 ...}}`

- Hapus file dari lokasi manapun dengan mengabaikan nama-nama file yang tidak ditemukan:

`rm -f {{jalan/menuju/file1 jalan/menuju/file2 ...}}`

- Hapus banyak file secara [i]nteraktif, dengan meminta konfirmasi sebelum setiap penghapusan:

`rm -i {{jalan/menuju/file1 jalan/menuju/file2 ...}}`

- Hapus file dengan mode [v]erbose, mencetak pesan untuk setiap file yang terhapus:

`rm -v {{jalan/menuju/file1 jalan/menuju/file2 ...}}`

- Hapus direktori dan semua subdirektorinya secara [r]ekursif:

`rm -r {{jalan/menuju/file_atau_direktori1 jalan/menuju/file_atau_direktori2 ...}}`
