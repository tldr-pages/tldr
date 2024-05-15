# adb logcat

> Dapatkan dan simpan log sistem pada perangkat Android.
> Informasi lebih lanjut: <https://developer.android.com/tools/logcat>.

- Tampilkan log sistem pada perangkat yang terhubung saat ini:

`adb logcat`

- Saring dan tampilkan log berdasarkan kriteria ekspresi reguler:

`adb logcat -e {{ekspresi_reguler}}`

- Saring dan tampilkan log menurut tingkat mode ([V]erbose, [D]ebug, [I]nfo, [W]arning, [E]rror, [F]atal, [S]ilent) serta tag pada pesan-pesan log:

`adb logcat {{tag}}:{{mode}} *:S`

- Tampilkan pesan-pesan log dari aplikasi berbasis React Native dalam mode [V]erbose, dan jangan tampilkan ([S]ilence) pesan lainnya:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- Tampilkan pesan-pesan log yang dikategorikan dalam tingkat mode [W]arning ke atas, tanpa menghiraukan jenis tag yang disaring:

`adb logcat *:W`

- Tampilkan pesan-pesan log dari proses tertentu (menurut kode PID proses tersebut):

`adb logcat --pid={{pid}}`

- Tampilkan pesan-pesan log dari aplikasi tertentu (menurut package identifier seperti `com.example.myapp`):

`adb logcat --pid=$(adb shell pidof -s {{nama_pengenal_aplikasi}})`

- Tampilkan log sistem secara warna-warni (biasanya digunakan untuk menyaring pesan-pesan log):

`adb logcat -v color`
