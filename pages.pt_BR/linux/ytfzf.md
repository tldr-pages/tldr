# ytfzf

> Encontre e baixe vídeos e músicas. Escrito em shell POSIX.
> Veja também: `youtube-dl`, `yt-dlp`, `instaloader`.
> Mais informações: <https://manned.org/ytfzf>.

- Busca por vídeos no YouTube com previsualizações de capa:

`ytfzf {{[-t|--show-thumbnails]}} {{padrão_de_pesquisa}}`

- Toca somente o áudio do primeiro item em loop:

`ytfzf {{[-m|--audio-only]}} {{[-a|--auto-select]}} {{[-l|--loop]}} {{padrão_de_pesquisa}}`

- Baixa um vídeo do histórico:

`ytfzf {{[-d|--download]}} --choose-from-history`

- Toca todas as músicas encontradas na busca:

`ytfzf {{[-m|--audio-only]}} {{[-A|--select-all]}} {{padrão_de_pesquisa}}`

- Vê os vídeos em alta num menu externo:

`ytfzf --trending --ext-menu {{padrão_de_pesquisa}}`

- Busca no PeerTube ao invés do YouTube:

`ytfzf --peertube {{padrão_de_pesquisa}}`
