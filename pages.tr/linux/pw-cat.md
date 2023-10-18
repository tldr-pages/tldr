# pw-cat

> Ses dosyalarını çalıştırmak ve kayıt etmek için pipewire aracı.
> Daha fazla bilgi için: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Tüm erişilebilir oynatma hedeflerini sırala:

`pw-cat --playback --list-targets`

- Varsayılan hedef üzerinden bir WAV dosyası oynat:

`pw-cat --playback {{örnek/konum/dosya.wav}}`

- Tüm erişilebilir kayıt hedeflerini sırala:

`pw-cat --record --list-targets`

- Örnek bir kaydı farklı bir ses seviyesinde kayda al:

`pw-cat --record --volume={{0.1}} {{örnek/konum/dosya.wav}}`

- Örnek bir kaydı farklı bir örnek oran kullanarak kayda al:

`pw-cat --record --rate={{6000}} {{örnek/konum/dosya.wav}}`
