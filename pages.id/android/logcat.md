# logcat

> Tampilkan dan simpan log sistem.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/logcat>.

- Tampilkan log sistem:

`logcat`

- Simpan log sistem di dalam sebuah file:

`logcat -f {{path/to/file}}`

- Saring informasi log berdasarkan sintaks ekspresi reguler (regex) tertentu:

`logcat --regex {{regular_expression}}`

- Tampilkan log untuk nomor induk (PID) program yang sedang dijalankan:

`logcat --pid={{pid}}`

- Tampilkan log untuk (kemasan) aplikasi yang sedang dijalankan:

`logcat --pid=$(pidof -s {{nama_kemasan_aplikasi}})`
