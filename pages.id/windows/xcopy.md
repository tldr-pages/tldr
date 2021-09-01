# xcopy

> Membuat salinan file dan direktori.
> Informasi lebih lanjut: <https://docs.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Membuat salinan file atau direktori ke lokasi lain:

`xcopy {{jalan/menuju/file_atau_direktori_sumber}} {{jalan/menuju/file_atau_direktori_tujuan}}`

- Melihat daftar file yang akan disalin sebelum proses salinan dimulai:

`xcopy {{jalan/menuju/file_atau_direktori_sumber}} {{jalan/menuju/file_atau_direktori_tujuan}} /p`

- Membuat salinan struktur direktori saja (tanpa file di dalamnya):

`xcopy {{jalan/menuju/file_atau_direktori_sumber}} {{jalan/menuju/file_atau_direktori_tujuan}} /t`

- Membuat salinan direktori termasuk direktori-direktori kosong (tanpa file):

`xcopy {{jalan/menuju/file_atau_direktori_sumber}} {{jalan/menuju/file_atau_direktori_tujuan}} /e`

- Membuat salinan file atau direktori dengan daftar hak akses pengguna (ACL) yang sama:

`xcopy {{jalan/menuju/file_atau_direktori_sumber}} {{jalan/menuju/file_atau_direktori_tujuan}} /o`

- Mempersilakan proses penyalinan file atau direktori saat koneksi jaringan komputer terputus:

`xcopy {{jalan/menuju/file_atau_direktori_sumber}} {{jalan/menuju/file_atau_direktori_tujuan}} /z`

- Mempersilakan `xcopy` untuk tetap mengganti file yang sudah ada di lokasi tujuan dengan file yang berada di lokasi sumber:

`xcopy {{jalan/menuju/file_atau_direktori_sumber}} {{jalan/menuju/file_atau_direktori_tujuan}} /y`

- Menampilkan cara penggunaan secara lengkap:

`xcopy /?`
