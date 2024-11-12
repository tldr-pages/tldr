# pacman --database

> Atua no banco de dados de pacotes do Arch Linux.
> Modifica certos atributos dos pacotes instalados.
> Veja também: `pacman`.
> Mais informações: <https://manned.org/pacman.8>.

- Marca um pacote como instalado implicitamente:

`sudo pacman --database --asdeps {{pacote}}`

- Marca um pacote como instalado explicitamente:

`sudo pacman --database --asexplicit {{pacote}}`

- Verifica se todas as dependências de pacotes estão instaladas:

`pacman --database --check`

- Verifica os repositórios para garantir que todas as dependências especificadas estejam disponíveis:

`pacman --database --check --check`

- Exibe apenas mensagens de erro:

`pacman --database --check --quiet`

- Exibe ajuda:

`pacman --database --help`
