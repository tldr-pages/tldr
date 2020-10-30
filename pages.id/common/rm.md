# rm

> Menghapus berkas atau direktori.

- Menghapus berkas dari lokasi manapun:

`rm {{alamat/ke/berkas}} {{alamat/ke/berkas/lainnya}}`

- Menghapus direktori dan semua subdirektorinya secara rekursif:

`rm -r {{alamat/ke/direktori}}`

- Menghapus direktori secara paksa, tanpa meminta konfirmasi atau menampilkan pesan kesalahan:

`rm -rf {{alamat/ke/direktori}}`

- Menghapus banyak file secara interaktif, dengan meminta konfirmasi sebelum setiap penghapusan:

`rm -i {{(beberapa)_berkas}}`

- Menghapus berkas dengan mode verbose, mencetak pesan untuk setiap file yang terhapus:

`rm -v {{alamat/ke/directori/*}}`
