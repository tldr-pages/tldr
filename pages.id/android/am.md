# am

> Manajer aktivitas untuk Android.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb#am>.

- Memulai aktivitas tertentu:

`am start -n {{com.android.settings/.Settings}}`

- Memulai aktivitas dengan data yang ditentukan:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Memulai aktivitas dengan aksi dan kategori tertentu:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Mengubah sebuah Intent menjadi tautan URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
