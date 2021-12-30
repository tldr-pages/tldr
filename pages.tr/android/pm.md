# pm

> Android cihazındaki uygulamalar ile ilgili bilgi göster.
> Daha fazla bilgi için: <https://developer.android.com/studio/command-line/adb#pm>.

- İndirilen tüm uygulamaların sırala:

`pm list packages`

- İndirilen tüm sistem uygulamalarını sırala:

`pm list packages -s`

- İndirilen tüm üçüncü el uygulamaları sırala:

`pm list packages -3`

- Belirtilen anahtar kelimelere uyan uygulamaları sırala:

`pm list packages {{anahtar_kelimeler}}`

- Belirtilen uygulamanın APK'sine giden yolu görüntüle:

`pm path {{uygulama}}`
