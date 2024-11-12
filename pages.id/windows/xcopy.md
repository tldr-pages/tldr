# xcopy

> Salin berkas dan direktori.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Salin berkas atau direktori ke lokasi lain:

`xcopy {{jalan/menuju/berkas_atau_direktori_sumber}} {{jalan/menuju/berkas_atau_direktori_tujuan}}`

- Lihat daftar berkas yang akan disalin sebelum proses salinan dimulai:

`xcopy {{jalan/menuju/berkas_atau_direktori_sumber}} {{jalan/menuju/berkas_atau_direktori_tujuan}} /p`

- Hanya buat salinan struktur direktori saja (tanpa memasukkan berkas apapun ke dalamnya):

`xcopy {{jalan/menuju/berkas_atau_direktori_sumber}} {{jalan/menuju/berkas_atau_direktori_tujuan}} /t`

- Salin termasuk direktori-direktori tanpa isi berkas:

`xcopy {{jalan/menuju/berkas_atau_direktori_sumber}} {{jalan/menuju/berkas_atau_direktori_tujuan}} /e`

- Salin berkas dan direktori termasuk informasi hak akses pengguna (ACL) masing-masing:

`xcopy {{jalan/menuju/berkas_atau_direktori_sumber}} {{jalan/menuju/berkas_atau_direktori_tujuan}} /o`

- Izinkan proses penyalinan berkas atau direktori untuk berlangsung saat koneksi jaringan komputer terputus:

`xcopy {{jalan/menuju/berkas_atau_direktori_sumber}} {{jalan/menuju/berkas_atau_direktori_tujuan}} /z`

- Izinkan `xcopy` untuk tetap mengganti berkas yang sudah ada di lokasi tujuan dengan berkas yang berada di lokasi sumber (override):

`xcopy {{jalan/menuju/berkas_atau_direktori_sumber}} {{jalan/menuju/berkas_atau_direktori_tujuan}} /y`

- Tampilkan informasi bantuan:

`xcopy /?`
