# pacman --database

> Atua no banco de dados de pacotes do Arch Linux.
> Modifica certos atributos dos pacotes instalados.
> Veja também: `pacman`.
> Mais informações: <https://manned.org/pacman.8>.

- Marca um pacote como instalado implicitamente:

`sudo pacman -D --asdeps {{pacote}}`

- Marca um pacote como instalado explicitamente:

`sudo pacman -D --asexplicit {{pacote}}`

- Verifica se todas as dependências de pacotes estão instaladas:

`pacman -Dk`

- Verifica os repositórios para garantir que todas as dependências especificadas estejam disponíveis:

`pacman -Dkk`

- Exibe apenas mensagens de erro:

`pacman -Dkq`

- Exibe ajuda:

`pacman -Dh`
