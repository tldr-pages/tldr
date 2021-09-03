# pm

> Menampilkan daftar pemasangan aplikasi di dalam sebuah perangkat Android.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb#pm>.

- Menampilkan daftar seluruh aplikasi yang terpasang:

`pm list packages`

- Menampilkan daftar seluruh aplikasi sistem yang terpasang:

`pm list packages -s`

- Menampilkan daftar seluruh aplikasi pihak ketiga yang terpasang:

`pm list packages -3`

- Menampilkan daftar aplikasi dengan kata kunci tertentu:

`pm list packages {{kata_kunci}}`

- Menampilkan jalan menuju file APK untuk sebuah aplikasi:

`pm path {{aplikasi}}`
