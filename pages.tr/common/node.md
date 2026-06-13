# node

> Sunucu tarafı JavaScript platformu (Node.js).
> Daha fazla bilgi için: <https://nodejs.org/docs/latest/api/cli.html#options>.

- JavaScript dosyası çalıştır:

`node {{dosya/yolu}}`

- REPL (interactive shell) başlat:

`node`

- Bir içe aktarılan dosya değiştirildiği zaman belirtilen dosyayı yeniden başlat (Node.js sürüm 18.11+ gerektirir):

`node --watch {{dosya/yolu}}`

- JavaScript kodunu argüman olarak geçerek değerlendir:

`node {{[-e|--eval]}} "{{kod}}"`

- Sonucu değerlendir ve yazdır, Node.js bağımlılıklarının sürümlerini yazdırmak için kullanışlıdır:

`node {{[-p|--print]}} "process.versions"`

- Denetleyiciyi etkinleştirerek, kaynak kodu tamamen ayrıştırıldıktan sonra bir hata ayıklayıcı bağlanana kadar yürütmeyi duraklatır:

`node --no-lazy --inspect-brk {{dosya/yolu}}`
