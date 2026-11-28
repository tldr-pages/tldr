# bat

> Dosyaları yazdır ve birleştir.
> Sözdizimi vurgulama ve Git entegrasyonuna sahip bir `cat` klonu.
> Ayrıca bakınız: `cat`.
> Daha fazla bilgi için: <https://manned.org/bat>.

- Bir veya daha fazla dosyanın içeriğini biçimlendirerek `stdout`'a yazdır:

`bat {{yol/dosya1 yol/dosya2 ...}}`

- Birkaç dosyayı hedef dosyada birleştir:

`bat {{yol/dosya1 yol/dosya2 ...}} >{{yol/hedef_dosya}}`

- Süslemeleri kaldır ve sayfalamayı devre dışı bırak:

`bat {{[-pp|--style plain --pager never]}} {{yol/dosya}}`

- Belirli bir satırı veya satır aralığını farklı bir arka plan rengiyle vurgula:

`bat {{[-H|--highlight-line]}} {{10|5:10|:10|10:|10:+5}} {{yol/dosya}}`

- Boşluk, sekme veya yeni satır gibi yazdırılamayan karakterleri göster:

`bat {{[-A|--show-all]}} {{yol/dosya}}`

- Çıktıda satır numaraları dışındaki tüm süslemeleri kaldır:

`bat {{[-n|--number]}} {{yol/dosya}}`

- Dili açıkça belirterek bir JSON dosyasının sözdizimini vurgula:

`bat {{[-l|--language]}} json {{yol/dosya.json}}`

- Desteklenen tüm dilleri görüntüle:

`bat {{[-L|--list-languages]}}`
