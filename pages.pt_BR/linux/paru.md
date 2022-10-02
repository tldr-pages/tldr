# paru

> Um auxiliar do AUR e um wrapper do pacman.
> Mais informações: <https://github.com/Morganamilo/paru>.

- Pesquisar e instalar interativamente um pacote:

`paru {{nome_do_pacote_ou_termo_de_pesquisa}}`

- Sincronizar e atualizar todos os pacotes:

`paru`

- Atualizar pacotes do AUR:

`paru -Sua`

- Obter informações sobre um pacote:

`paru -Si {{nome_do_pacote}}`

- Fazer o download do `PKGBUILD` e outros arquivos de origem do pacote do AUR ou ABS:

`paru --getpkgbuild {{nome_do_pacote}}`

- Exibir o arquivo `PKGBUILD` de um pacote:

`paru --getpkgbuild --print {{nome_do_pacote}}`
