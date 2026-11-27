# asr

> Pulihkan (salin) isi suatu citra penyimpanan menuju volume penyimpanan yang lain.
> Makna nama perintah ini adalah perangkat Apple Software Restore.
> Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/asr.8.html>.

- Pulihkan suatu citra menuju target volume penyimpanan tertentu:

`sudo asr restore --source {{jalan/menuju/berkas_citra.dmg}} --target {{jalan/menuju/berkas_volume_penyimpanan}}`

- Hapus paksa volume penyimpanan tujuan sebelum memulihkan isi citra:

`sudo asr restore --source {{jalan/menuju/berkas_citra.dmg}} --target {{jalan/menuju/berkas_volume_penyimpanan}} --erase`

- Longkapi proses verifikasi data citra setelah proses pemulihan selesai:

`sudo asr restore --source {{jalan/menuju/berkas_citra.dmg}} --target {{jalan/menuju/berkas_volume_penyimpanan}} --noverify`

- Salin seluruh isi suatu volume menuju volume penyimpanan yang lain tanpa membuat berkas tangkapan citra volume penyimpanan asal:

`sudo asr restore --source {{jalan/menuju/berkas_volume_penyimpanan_asal}} --target {{jalan/menuju/berkas_volume_penyimpanan_tujuan}}`
