# playerctl

> Medya oynatıcılarını MPRIS aracılığıyla kumanda edin.
> Daha fazla bilgi için: <https://github.com/altdesktop/playerctl#using-the-cli>.

- Oynatmayı aç/kapat:

`playerctl play-pause`

- Bir sonraki medyaya geçin:

`playerctl next`

- Bir önceki medyaya geçin:

`playerctl previous`

- Tüm oynatıcıları listeleyin:

`playerctl {{[-l|--list-all]}}`

- Belirtilen oynatıcıya komut verin:

`playerctl {{[-p|--player]}} {{oynatıcı_ismi}} {{play-pause|next|previous|...}}`

- Tüm oynatıcılara komut verin:

`playerctl {{[-a|--all-players]}} {{play-pause|next|previous|...}}`

- Mevcut medyanın meta verisini görüntüleyin:

`playerctl metadata {{[-f|--format]}} "{{Şuanda oynatılıyor: \{\{artist\}\} - \{\{album\}\} - \{\{title\}\}}}"`
