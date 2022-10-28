# bat

> Dosyaları yazdırın ve birleştirin.
> Sözdizimi vurgulama ve Git entegrasyonuna sahip bir `cat` klonu.
> Daha fazla bilgi: <https://github.com/sharkdp/bat>.

- Bir dosyanın içeriğini standart çıktıya yazdırın:

`bat {{dosya}}`

- Birkaç dosyayı hedef dosyada birleştirin:

`bat {{dosya1}} {{dosya2}} > {{hedef_dosya}}`

- Birkaç dosyayı hedef dosyaya ekler:

`bat {{dosya1}} {{dosya2}} >> {{hedef_dosya}}`

- Tüm çıktı satırlarını numaralandırın:

`bat -n {{dosya}}`

- Bir JSON dosyasının sözdizimini vurgulayın:

`bat --language json {{dosya.json}}`

- Desteklenen tüm dilleri görüntüleyin:

`bat --list-languages`
