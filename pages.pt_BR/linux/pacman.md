# pacman

> Utilitário de Arch Linux para gerenciamento de pacotes.
> Veja também: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Mais informações: <https://man.archlinux.org/man/pacman.8>.

- Sincroniza e atualiza todos os pacotes:

`sudo pacman -Syu`

- Instala um novo pacote:

`sudo pacman -S {{nome_do_pacote}}`

- Remove um pacote e suas dependências:

`sudo pacman -Rs {{nome_do_pacote}}`

- Procura no banco de dados de pacotes por uma expressão regular ou palavra-chave:

`pacman -Ss "{{padrao_buscado}}"`

- Lista pacotes instalados e versões:

`pacman -Q`

- Lista apenas os pacotes explicitamente instalados e versões:

`pacman -Qe`

- Lista pacotes órfãos (instalado como dependência mas não requerido por qualquer pacote):

`pacman -Qtdq`

- Esvazia completamente o cache do pacman:

`sudo pacman -Scc`
