# tail

> Bir dosyanın son kısmını göster.
> Ayrıca bakınız: `head`.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Bir dosyanın son 10 satırını göster:

`tail {{dosya/yolu}}`

- Birden fazla dosyanın son 10 satırını göster:

`tail {{dosya/yolu1 dosya/yolu2 ...}}`

- Bir dosyanın son 5 satırını göster:

`tail {{[-5|--lines 5]}} {{dosya/yolu}}`

- Bir dosyayı belirli bir satır numarasından itibaren yazdır:

`tail {{[-n|--lines]}} +{{sayı}} {{dosya/yolu}}`

- Verilen dosyanın sonundan belirli sayıda bayt yazdır:

`tail {{[-c|--bytes]}} {{sayı}} {{dosya/yolu}}`

- Verilen dosyanın son satırlarını yazdır ve `<Ctrl c>` tuşlarına basılana kadar okumaya devam et:

`tail {{[-f|--follow]}} {{dosya/yolu}}`

- Dosya erişilemez olsa bile `<Ctrl c>` tuşlarına basılana kadar okumaya devam et:

`tail {{[-F|--retry --follow]}} {{dosya/yolu}}`

- Bir dosyanın son `sayı` satırını göster ve `saniye` saniyede bir yenile:

`tail {{[-n|--lines]}} {{sayı}} {{[-s|--sleep-interval]}} {{saniye}} {{[-f|--follow]}} {{dosya/yolu}}`
