# touch

> Dosya oluştur ve erişim/değiştirilme zamanlarını ayarla.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/touch-invocation.html>.

- Belirtilen dosyaları oluştur veya zaten varsa zaman damgalarını güncelle:

`touch {{dosya/yolu1 dosya/yolu2 ...}}`

- Dosyanın erişim veya değiştirilme zamanını şimdiki zamana ayarla ve dosya yoksa oluşturma:

`touch {{[-c|--no-create]}} {{-a|-m}} {{dosya/yolu1 dosya/yolu2 ...}}`

- Dosyanın zamanını belirli bir değere ayarla ve dosya yoksa oluşturma:

`touch {{[-c|--no-create]}} -t {{YYYYMMDDHHMM.SS}} {{dosya/yolu1 dosya/yolu2 ...}}`

- Dosyaların zaman damgasını referans dosyasının zaman damgasına ayarla ve dosya yoksa oluşturma:

`touch {{[-c|--no-create]}} {{[-r|--reference]}} {{referans_dosyası/yolu}} {{dosya/yolu1 dosya/yolu2 ...}}`

- Zaman damgasını bir dizgiyi ayrıştırarak ayarla:

`touch {{[-d|--date]}} "{{last year|5 hours|next thursday|nov 14|...}}" {{dosya/yolu}}`

- Artan sayılarla birden fazla dosya oluştur:

`touch {{dosya/yolu{1..10}}}`

- Harf aralığıyla birden fazla dosya oluştur:

`touch {{dosya/yolu{a..z}}}`
