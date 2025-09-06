# chattr

> Altera os atributos de arquivos ou diretórios.
> Mais informações: <https://manned.org/chattr>.

- Bloqueia um arquivo ou diretório para mudanças ou remoção, mesmo para um super usuário:

`chattr +i {{caminho_do_arquivo_ou_diretorio}}`

- Desbloqueia um arquivo ou diretório:

`chattr -i {{caminho_do_arquivo_ou_diretorio}}`

- Bloqueia diretório e todos os seus arquivos para mudanças ou remoção:

`chattr -R +i {{caminho_do_diretorio}}`
