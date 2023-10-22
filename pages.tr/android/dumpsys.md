# dumpsys

> Android sistem servisleri ile ilgili bilgi sağla.
> Bu komut yalnızca `adb shell` ile kullanılabilir.
> Daha fazla bilgi için: <https://developer.android.com/studio/command-line/dumpsys>.

- Tüm sistem servisleri için tanısal bir çıktı al:

`dumpsys`

- Belirtilen sistem servisi için tanısal bir çıktı al:

`dumpsys {{servis}}`

- `dumpsys` komutunun hakkında bilgi verebileceği tüm servisleri sırala:

`dumpsys -l`

- Bir servis için servise özel argümanları sırala:

`dumpsys {{servis}} -h`

- Tanı çıktısından belirtilen servisi çıkart:

`dumpsys --skip {{servis}}`

- Saniye bazında bir zaman aşımı süresi belirle (varsayılan 10 saniyedir):

`dumpsys -t {{saniye}}`
