# node

> Sunucu tarafı JavaScript platformu (Node.js).
> Daha fazla bilgi için: <https://nodejs.org>.

- JavaScript dosyası çalıştır:

`node {{path/to/file}}`

- REPL (interactive shell) başlat:

`node`

- Bir içe aktarılan dosya değiştirildiği zaman belirtilen dosyayı yeniden başlat (Node.js sürüm 18.11+ gerektirir):

`node --watch {{path/to/file}}`

- JavaScript kodunu argüman olarak geçerek değerlendir:

`node -e "{{code}}"`

- Sonucu değerlendir ve yazdır, Node.js bağımlılıklarının sürümlerini yazdırmak için kullanışlıdır:

`node -p "process.versions"`

- Denetleyiciyi etkinleştirerek, kaynak kodu tamamen ayrıştırıldıktan sonra bir hata ayıklayıcı bağlanana kadar yürütmeyi duraklatır:

`node --no-lazy --inspect-brk {{path/to/file}}`
