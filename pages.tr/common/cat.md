# cat

> Dosyaları yazdırın ve birleştirin.
> Daha fazla bilgi: <https://www.gnu.org/software/coreutils/cat>.

- Bir dosyanın içeriğini standart çıktıya yazdırın:

`cat {{dosya/yolu}}`

- Birkaç dosyayı bir çıktı dosyasında birleştirin:

`cat {{dosya/yolu1}} {{dosya/yolu2}} > {{cikti/dosyasi/yolu}}`

- Birkaç dosyayı bir çıktı dosyasına ekler:

`cat {{dosya/yolu1}} {{dosya/yolu2}} >> {{cikti/dosyasi/yolu}}`

- Tüm çıkış satırlarını numaralandırın:

`cat -n {{dosya/yolu}}`

- Yazdırılamayan ve boşluk karakterleri görüntüleyin (ASCII değilse `M-` önekiyle):

`cat -v -t -e {{dosya/yolu}}`
