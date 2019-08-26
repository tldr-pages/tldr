# chattr

> Altera os atributos de arquivos ou diretórios.

- Bloquear um arquivo ou diretório para mudanças ou remoção, mesmo para um super usuário:

`chattr +i {{caminho_do_arquivo_ou_diretorio}}`

- Desbloquear um arquivo ou diretório:

`chattr -i {{caminho_do_arquivo_ou_diretorio}}`

- Bloquear diretório e todos os seus arquivos para mudanças ou remoção:

`chattr -R +i {{caminho_do_diretorio}}`
