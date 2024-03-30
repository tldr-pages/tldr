# paru

> Um auxiliar do AUR e um wrapper do pacman.
> Mais informações: <https://github.com/Morganamilo/paru>.

- Pesquisa e instala interativamente um pacote:

`paru {{nome_do_pacote_ou_termo_de_pesquisa}}`

- Sincroniza e atualiza todos os pacotes:

`paru`

- Atualiza pacotes do AUR:

`paru -Sua`

- Obtém informações sobre um pacote:

`paru -Si {{nome_do_pacote}}`

- Faz o download do `PKGBUILD` e outros arquivos de origem do pacote do AUR ou ABS:

`paru --getpkgbuild {{nome_do_pacote}}`

- Exibe o arquivo `PKGBUILD` de um pacote:

`paru --getpkgbuild --print {{nome_do_pacote}}`
