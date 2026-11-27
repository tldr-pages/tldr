# cat

> Dosyaları yazdır ve birleştir.
> Daha fazla bilgi için: <https://manned.org/cat.1posix>.

- Bir dosyanın içeriğini `stdout`'a yazdır:

`cat {{yol/dosya}}`

- Birkaç dosyayı bir çıktı dosyasında birleştir:

`cat {{yol/dosya1 yol/dosya2 ...}} >{{yol/çıktı_dosyası}}`

- Birkaç dosyayı bir çıktı dosyasına ekle:

`cat {{yol/dosya1 yol/dosya2 ...}} >>{{yol/çıktı_dosyası}}`

- Bir dosyanın içeriğini arabelleğe almadan bir çıktı dosyasına kopyala:

`cat -u {{/dev/tty12}} >{{/dev/tty13}}`

- `stdin`'i bir dosyaya yaz:

`cat - >{{yol/dosya}}`
