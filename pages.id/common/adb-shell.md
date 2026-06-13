# adb shell

> Android Debug Bridge Shell: Menjalankan perintah shell jarak jauh pada emulator Android atau perangkat Android terhubung.
> Informasi lebih lanjut: <https://developer.android.com/tools/adb>.

- Mulaikan shell interaktif jarak jauh di emulator/perangkat:

`adb shell`

- Dapatkan semua properti dari emulator/perangkat:

`adb shell getprop`

- Kembalikan semua izin runtime ke default:

`adb shell pm reset-permissions`

- Cabut izin berbahaya dari sebuah aplikasi:

`adb shell pm revoke {{paket}} {{izin}}`

- Picukan sebuah peristiwa penting:

`adb shell input keyevent {{keycode}}`

- Kosongkan data aplikasi pada emulator/perangkat:

`adb shell pm clear {{paket}}`

- Mulaikan aktivitas pada emulator/perangkat:

`adb shell am start -n {{paket}}/{{aktivitas}}`

- Mulaikan aktivitas beranda pada emulator/perangkat:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
