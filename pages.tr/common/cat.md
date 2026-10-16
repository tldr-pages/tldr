# cat

> Dosyaları yazdır ve birleştir.
> Daha fazla bilgi için: <https://manned.org/cat.1posix>.

- Bir dosyanın içeriğini `stdout`'a yazdır:

`cat {{dosya/yolu}}`

- Birkaç dosyayı bir çıktı dosyasında birleştir:

`cat {{dosya/yolu1 dosya/yolu2 ...}} > {{çıktı/dosyası/yolu}}`

- Birkaç dosyayı bir çıktı dosyasına ekle:

`cat {{dosya/yolu1 dosya/yolu2 ...}} >> {{çıktı/dosyası/yolu}}`

- Bir dosyanın içeriğini arabelleğe almadan bir çıktı dosyasına kopyala:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- `stdin`'i bir dosyaya yaz:

`cat - > {{dosya/yolu}}`
