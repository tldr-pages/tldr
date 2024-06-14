# apkleaks

> Pindai berkas APK (aplikasi Android) untuk mencari URI, alur pemanggilan (endpoint), dan konfigurasi rahasia.
> Catatan: APKLeaks menggunakan `jadx` untuk membongkar kode aplikasi Android.
> Informasi lebih lanjut: <https://github.com/dwisiswant0/apkleaks>.

- Pindai berkas ([f]ile) APK untuk mencari daftar endpoint dan kode konfigurasi rahasia:

`apkleaks --file {{jalan/menuju/berkas.apk}}`

- Pindai dan simpan luaran ([o]utput) ke dalam suatu berkas:

`apkleaks --file {{jalan/menuju/berkas.apk}} --output {{jalan/menuju/berkas_output.txt}}`

- Berikan [a]rgumen perintah tambahan untuk `jadx`:

`apkleaks --file {{jalan/menuju/berkas.apk}} --args "{{--threads-count 5 --deobf}}"`
