# pacman --query

> Utilitário de Arch Linux para gerenciamento de pacotes.
> Veja também: `pacman`.
> Mais informações: <https://manned.org/pacman.8>.

- Lista pacotes instalados e suas versões:

`pacman -Q`

- Lista apenas pacotes e versões que foram instalados explicitamente:

`pacman -Qe`

- Procura qual pacote possui um arquivo:

`pacman -Qo {{arquivo}}`

- Exibe informações sobre um pacote instalado:

`pacman -Qi {{pacote}}`

- Lista arquivos fornecidos por um pacote:

`pacman -Ql {{pacote}}`

- Lista pacotes órfãos (instalados como dependências, mas que nenhum pacote instalado necessita):

`pacman -Qdtq`

- Lista pacotes instalados não encontrados nos repositórios:

`pacman -Qm`

- Lista pacotes desatualizados:

`pacman -Qu`
