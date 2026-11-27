# node

> Sunucu tarafı JavaScript platformu (Node.js).
> Daha fazla bilgi için: <https://nodejs.org/docs/latest/api/cli.html#options>.

- JavaScript dosyası çalıştır:

`node {{yol/dosya}}`

- REPL (interactive shell) başlat:

`node`

- Bir içe aktarılan dosya değiştirildiği zaman belirtilen dosyayı yeniden başlat (Node.js sürüm 18.11+ gerektirir):

`node --watch {{yol/dosya}}`

- JavaScript kodunu argüman olarak geçerek değerlendir:

`node {{[-e|--eval]}} "{{kod}}"`

- Sonucu değerlendir ve yazdır, Node.js bağımlılıklarının sürümlerini yazdırmak için kullanışlıdır:

`node {{[-p|--print]}} "process.versions"`

- Denetleyiciyi etkinleştirerek, kaynak kodu tamamen ayrıştırıldıktan sonra bir hata ayıklayıcı bağlanana kadar yürütmeyi duraklatır:

`node --no-lazy --inspect-brk {{yol/dosya}}`
