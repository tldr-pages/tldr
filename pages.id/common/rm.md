# rm

> Hapus file atau direktori.
> Lihat juga: `rmdir`.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/rm>.

- Hapus file dari lokasi manapun:

`rm {{alamat/ke/file1 alamat/ke/file2 ...}}`

- Hapus file dari lokasi manapun dengan mengabaikan nama-nama file yang tidak ditemukan:

`rm -f {{alamat/ke/file1 alamat/ke/file2 ...}}`

- Hapus banyak file secara [i]nteraktif, dengan meminta konfirmasi sebelum setiap penghapusan:

`rm -i {{alamat/ke/file1 alamat/ke/file2 ...}}`

- Hapus file dengan mode [v]erbose, mencetak pesan untuk setiap file yang terhapus:

`rm -v {{alamat/ke/file1 alamat/ke/file2 ...}}`

- Hapus direktori dan semua subdirektorinya secara [r]ekursif:

`rm -{{alamat/ke/file1 alamat/ke/file2 ...}}`
