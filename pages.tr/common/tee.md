# tee

> Standart girdiden (`stdin`) oku, `stdout`'a ve dosyalara (veya komutlara) yaz.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>.

- Standart girdiyi (`stdin`) belirtilen dosyalara ve ayrıca `stdout`'a kopyala:

`echo "örnek" | tee {{dosya/yolu}}`

- Verilen dosyaların üzerine yazma, sonuna ekle:

`echo "örnek" | tee {{[-a|--append]}} {{dosya/yolu}}`

- Standart girdiyi (`stdin`) terminale yazdır ve ayrıca işlenmesi için başka bir programa aktar:

`echo "örnek" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- Adı "örnek" olan bir dizin oluştur, "örnek" içindeki karakterleri say ve "örnek" metnini terminale yaz:

`echo "örnek" | tee >(xargs mkdir) >(wc {{[-c|--bytes]}})`
