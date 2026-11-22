# adb

> Android Hata Ayıklama Köprüsü (Android Debug Bridge): Bir Android öykünücü örneği veya bağlı Android cihazlarla iletişim kurun.
> `shell` gibi bazı alt komutların kendi kullanım belgeleri vardır.
> Daha fazla bilgi: <https://developer.android.com/tools/adb>.

- Adb sunucu sürecinin çalışıp çalışmadığını kontrol et ve başlat:

`adb start-server`

- Adb sunucu sürecini sonlandır:

`adb kill-server`

- Hedef öykünücü/cihaz örneğinde uzak bir kabuk başlat:

`adb shell`

- Bir Android uygulamasını öykünücüye/cihaza yükle:

`adb install -r {{dosya/yolu}}.apk`

- Hedef cihazdan bir dosya/dizin kopyala:

`adb pull {{cihazdaki_dosya_veya_dizin_yolu}} {{yerel_hedef_dizin_yolu}}`

- Hedef cihaza bir dosya/dizin kopyala:

`adb push {{yerel_dosya_veya_dizin_yolu}} {{cihazdaki_hedef_dizin_yolu}}`

- Bağlı tüm cihazları listele:

`adb devices`

- Birden fazla cihaz varsa komutların gönderileceği cihazı belirt:

`adb -s {{cihaz_kimliği}} {{shell}}`
