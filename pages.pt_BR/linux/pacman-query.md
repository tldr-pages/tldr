# pacman --query

> Utilitário de Arch Linux para gerenciamento de pacotes.
> Veja também: `pacman`.
> Mais informações: <https://manned.org/pacman.8>.

- Lista pacotes instalados e suas versões:

`pacman --query`

- Lista apenas pacotes e versões que foram instalados explicitamente:

`pacman --query --explicit`

- Procura qual pacote possui um arquivo:

`pacman --query --owns {{arquivo}}`

- Exibe informações sobre um pacote instalado:

`pacman --query --info {{pacote}}`

- Lista arquivos fornecidos por um pacote:

`pacman --query --list {{pacote}}`

- Lista pacotes órfãos (instalados como dependências, mas que nenhum pacote instalado necessita):

`pacman --query --unrequired --deps --quiet`

- Lista pacotes instalados não encontrados nos repositórios:

`pacman --query --foreign`

- Lista pacotes desatualizados:

`pacman --query --upgrades`
