# chattr

> Altera os atributos de arquivos ou diretórios.

- Bloqueia um arquivo ou diretório para mudanças ou remoção, mesmo para um super usuário:

`chattr +i {{path/to/file_or_directory}}`

- Desbloqueia um arquivo ou diretório:

`chattr -i {{path/to/file_or_directory}}`

- Bloqueia diretório e todos os seus arquivos para mudanças ou remoção:

`chattr -R +i {{path/to/directory}}`
