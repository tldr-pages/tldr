# pw-play

> pw-cat --playback komutu için kısayol aracı.
> Daha fazla bilgi için: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Tüm erişilebilir oynatma hedeflerini sırala:

`pw-play --list-targets`

- Varsayılan hedef üzerinden bir WAV sesi oynat:

`pw-play {{örnek/konum/dosya.wav}}`

- WAV sesini farklı bir ses yüksekliğinde oynat:

`pw-play --volume={{0.1}} {{örnek/konum/dosya.wav}}`
