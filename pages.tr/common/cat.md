# cat

> Dosyaları yazdır ve birleştir.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/cat>.

- Bir dosyanın içeriğini standart çıktıya yazdır:

`cat {{dosya/yolu}}`

- Birkaç dosyayı bir çıktı dosyasında birleştir:

`cat {{dosya/yolu1}} {{dosya/yolu2}} > {{çıktı/dosyası/yolu}}`

- Birkaç dosyayı bir çıktı dosyasına ekle:

`cat {{dosya/yolu1}} {{dosya/yolu2}} >> {{çıktı/dosyası/yolu}}`

- Tüm çıkış satırlarını numaralandır:

`cat -n {{dosya/yolu}}`

- Yazdırılamayan ve boşluk karakterleri görüntüle (ASCII değilse `M-` önekiyle):

`cat -v -t -e {{dosya/yolu}}`
