# adb forward

> Teruskan akses soket menuju suatu perangkat atau emulator Android.
> Informasi lebih lanjut: <https://developer.android.com/tools/adb>.

- Teruskan akses suatu port TCP menuju emulator atau perangkat yang terhubung saat ini:

`adb forward tcp:{{port_lokal}} tcp:{{port_jarak_jauh}}`

- Teruskan akses suatu port TCP menuju suatu emulator atau perangkat secara spesifik (berdasarkan nomor induk / [s]erial perangkat):

`adb -s {{ID_perangkat}} forward tcp:{{port_lokal}} tcp:{{port_remote}}`

- Tampilkan daftar seluruh pengaturan terusan:

`adb forward --list`

- Hapus suatu aturan terusan:

`adb forward --remove tcp:{{port_lokal}}`

- Hapus seluruh pengaturan terusan:

`adb forward --remove-all`
