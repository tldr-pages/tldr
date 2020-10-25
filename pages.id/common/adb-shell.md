# adb shell

> Android Debug Bridge Shell: Menjalankan perintah shell jarak jauh pada emulator Android atau perangkat Android terhubung.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Memulai shell interaktif jarak jauh di emulator/perangkat:

`adb shell`

- Mendapatkan semua properti dari emulator/perangkat:

`adb shell getprop`

- Mengembalikan semua izin runtime ke default:

`adb shell pm reset-permissions`

- Mencabut izin berbahaya dari sebuah aplikasi:

`adb shell pm revoke {{paket}} {{izin}}`

- Memicu sebuah peristiwa penting:

`adb shell input keyevent {{keycode}}`

- Mengosongkan data aplikasi pada emulator/perangkat:

`adb shell pm clear {{paket}}`

- Memulai aktivitas pada emulator/perangkat:

`adb shell am start -n {{paket}}/{{aktivitas}}`

- Memulai aktivitas beranda pada emulator/perangkat:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
