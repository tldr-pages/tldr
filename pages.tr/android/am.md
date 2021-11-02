# am

> Android aktivite yöneticisi.
> Daha fazla bilgi için: <https://developer.android.com/studio/command-line/adb#am>.

- Belirtilmiş bir aktiviteyi başlat:

`am start -n {{com.android.settings/.Settings}}`

- Bir aktivite başlatıp veriyi ona aktar:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Belirtilmiş bir eylem ve kategoriyi karşılayan bir aktivite başlat:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Bir kastı URI'a çevir:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
