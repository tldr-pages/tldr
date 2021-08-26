# cmd

> Manajer layanan (daemon) untuk Android.
> Informasi lebih lanjut: <https://cs.android.com/android/platform/superproject/+/master:frameworks/native/cmds/cmd/>.

- Melihat daftar layanan yang sedang berjalan:

`cmd -l`

- Memanggil suatu layanan tertentu:

`cmd {{alarm}}`

- Memanggil layanan dengan argumen tertentu:

`cmd {{vibrator}} {{vibrate 300}}`
