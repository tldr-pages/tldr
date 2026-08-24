# animdl

> Busque, assista e baixe anime.
> Veja também: `ani-cli`.
> Mais informações: <https://github.com/justfoolingaround/animdl#usage>.

- Baixa um determinado anime:

`animdl download "{{título_do_anime}}"`

- Baixa um determinado anime especificando um intervalo de episódios:

`animdl download "{{título_do_anime}}" {{[-r|--range]}} {{epsódio_inicial}}-{{episódio_final}}`

- Baixa um determinado anime especificando o diretório de download:

`animdl download "{{título_do_anime}}" {{[-d|--download-dir]}} {{caminho/para/diretório}}`

- Obtém a URL de transmissão para um determinado anime:

`animdl grab "{{título_do_anime}}"`

- Mostra o calendário de lançamento de animes para a próxima semana:

`animdl schedule`

- Busca um anime específico:

`animdl search "{{título_do_anime}}"`

- Assiste um anime específico via streaming:

`animdl stream "{{título_do_anime}}"`

- Assiste o último episódio de um anime via streaming:

`animdl stream "{{título_do_anime}}" {{[-s|--special]}} latest`
