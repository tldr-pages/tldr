# logcat

> Menampilkan dan menyimpan log sistem.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/logcat>.

- Menampilkan log sistem:

`logcat`

- Menyimpan log sistem di dalam sebuah file:

`logcat -f {{path/to/file}}`

- Menyaring informasi log berdasarkan sintaks ekspresi reguler (regex) tertentu:

`logcat --regex {{regular_expression}}`
