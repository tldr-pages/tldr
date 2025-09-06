# playerctl

> Medya oynatıcılarını MPRIS aracılığıyla kumanda edin.
> Daha fazla bilgi için: <https://github.com/altdesktop/playerctl>.

- Oynatmayı aç/kapat:

`playerctl play-pause`

- Bir sonraki medyaya geçin:

`playerctl next`

- Bir önceki medyaya geçin:

`playerctl previous`

- Tüm oynatıcıları listeleyin:

`playerctl --list-all`

- Belirtilen oynatıcıya komut verin:

`playerctl --player {{oynatıcı_ismi}} {{play-pause|next|previous|...}}`

- Tüm oynatıcılara komut verin:

`playerctl --all-players {{play-pause|next|previous|...}}`

- Mevcut medyanın meta verisini görüntüleyin:

`playerctl metadata --format "{{Şuanda oynatılıyor: \{\{artist\}\} - \{\{album\}\} - \{\{title\}\}}}"`
