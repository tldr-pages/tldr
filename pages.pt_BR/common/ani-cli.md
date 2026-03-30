# ani-cli

> Navegue e assista anime.
> Veja também: `animdl`.
> Mais informações: <https://manned.org/ani-cli>.

- Busca anime pelo nome:

`ani-cli "{{título_do_anime}}"`

- Baixa um episódio:

`ani-cli {{[-d|--download]}} "{{título_do_anime}}"`

- Baixa uma série de episódios:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "{{1 6}}" "{{título_do_anime}}"`

- Baixa todos os episódios:

`ani-cli {{[-d|--download]}} {{[-r|--range]}} "1 -1" "{{título_do_anime}}"`

- Usa o VLC como reprodutor de mídia:

`ani-cli {{[-v|--vlc]}} "{{título_do_anime}}"`

- Assiste um episódio específico:

`ani-cli {{[-e|--episode]}} {{número_do_episódio}} "{{título_do_anime}}"`

- Continua assistindo anime do histórico:

`ani-cli {{[-c|--continue]}}`

- Atualiza o `ani-cli`:

`ani-cli {{[-U|--update]}}`
