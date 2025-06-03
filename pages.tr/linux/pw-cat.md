# pw-cat

> Pipewire üzerinden ses dosyalarını çalın ve kaydedin.
> Daha fazla bilgi için: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Varsayılan hedef üzerinden bir WAV dosyası oynat:

`pw-cat {{[-p|--playback]}} {{örnek/konum/dosya.wav}}`

- Örnek bir kaydı farklı bir ses seviyesinde kayda al:

`pw-cat {{[-r|--record]}} --volume={{0.1}} {{örnek/konum/dosya.wav}}`

- Örnek bir kaydı farklı bir örnek oran kullanarak kayda al:

`pw-cat {{[-r|--record]}} --rate={{6000}} {{örnek/konum/dosya.wav}}`
