# tail

> Bir dosyanın son kısmını göster.
> Ayrıca bakınız: `head`.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Bir dosyanın son 10 satırını göster:

`tail {{yol/dosya}}`

- Birden fazla dosyanın son 10 satırını göster:

`tail {{yol/dosya1 yol/dosya2 ...}}`

- Bir dosyanın son 5 satırını göster:

`tail {{[-5|--lines 5]}} {{yol/dosya}}`

- Bir dosyayı belirli bir satır numarasından itibaren yazdır:

`tail {{[-n|--lines]}} +{{sayı}} {{yol/dosya}}`

- Verilen dosyanın sonundan belirli sayıda bayt yazdır:

`tail {{[-c|--bytes]}} {{sayı}} {{yol/dosya}}`

- Verilen dosyanın son satırlarını yazdır ve `<Ctrl c>` tuşlarına basılana kadar okumaya devam et:

`tail {{[-f|--follow]}} {{yol/dosya}}`

- Dosya erişilemez olsa bile `<Ctrl c>` tuşlarına basılana kadar okumaya devam et:

`tail {{[-F|--retry --follow]}} {{yol/dosya}}`

- Bir dosyanın son `sayı` satırını göster ve `saniye` saniyede bir yenile:

`tail {{[-n|--lines]}} {{sayı}} {{[-s|--sleep-interval]}} {{saniye}} {{[-f|--follow]}} {{yol/dosya}}`
