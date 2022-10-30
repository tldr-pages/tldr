# pw-record

> pw-cat --playback komutu için kısayol aracı.
> Daha fazla bilgi için: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Tüm erişilebilir kayıt hedeflerini sırala:

`pw-record --list-targets`

- Varsayılan hedefi kullanarak örnek bir ses kaydı al:

`pw-record {{örnek/konum/dosya.wav}}`

- Farklı bir ses seviyesinde örnek ses kaydı al:

`pw-record --volume={{0.1}} {{örnek/konum/dosya.wav}}`

- Farklı bir kayıt oranı kullanarak örnek ses kaydı al:

`pw-record --rate={{6000}} {{örnek/konum/dosya.wav}}`
