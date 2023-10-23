# pw-record

> Pipewire aracılığıyla ses dosyalarını kaydedin.
> pw-cat --record için kısaltma.
> Daha fazla bilgi için: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Varsayılan hedefi kullanarak örnek bir ses kaydı al:

`pw-record {{örnek/konum/dosya.wav}}`

- Farklı bir ses seviyesinde örnek ses kaydı al:

`pw-record --volume={{0.1}} {{örnek/konum/dosya.wav}}`

- Farklı bir kayıt oranı kullanarak örnek ses kaydı al:

`pw-record --rate={{6000}} {{örnek/konum/dosya.wav}}`
