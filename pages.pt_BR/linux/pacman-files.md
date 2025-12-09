# pacman --files

> Utilitário de Arch Linux para gerenciamento de pacotes.
> Veja também: `pacman`, `pkgfile`.
> Mais informações: <https://manned.org/pacman.8>.

- Atualiza o banco de dados de pacotes:

`sudo pacman --files --refresh`

- Procura o pacote que possui um arquivo específico:

`pacman --files {{nome_arquivo}}`

- Encontra o pacote que possui um arquivo específico, usando uma expressão regular:

`pacman --files --regex '{{expressao_regular}}'`

- Lista apenas os nomes de pacotes:

`pacman --files --quiet {{nome_arquivo}}`

- Lista os arquivos de um pacote específico:

`pacman --files --list {{pacote}}`

- Exibe ajuda:

`pacman --files --help`
