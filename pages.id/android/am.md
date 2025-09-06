# am

> Manajer aktivitas untuk Android.
> Informasi lebih lanjut: <https://developer.android.com/tools/adb#am>.

- Mulaikan aktivitas tertentu:

`am start -n {{com.android.settings/.Settings}}`

- Mulaikan aktivitas dengan data yang ditentukan:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Mulaikan aktivitas dengan aksi dan kategori tertentu:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Ubah sebuah Intent menjadi tautan URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
