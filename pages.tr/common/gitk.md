# gitk

> Görsel Git depo tarayıcısı.
> Daha fazla bilgi için: <https://git-scm.com/docs/gitk>.

- Mevcut Git deposu için depo tarayıcısını göster:

`gitk`

- Belirtilmiş dosya veya dizin için depo tarayıcısını göster:

`gitk {{path/to/file_or_directory}}`

- 1 hafta önceden beri yapılan commit'leri göster:

`gitk --since="{{1 week ago}}"`

- 1/1/2016 tarihinden önceki commit'leri göster:

`gitk --until="{{1/1/2016}}"`

- Tüm dallarda en fazla 100 değişiklik göster:

` gitk --max-count={{100}} --all`
