# pacdiff

> Utilitário de manutenção para arquivos `.pacorig`, `.pacnew` e `.pacsave` criados pelo `pacman`.
> Mais informações: <https://manned.org/pacdiff>.

- Reveja arquivos que precisam manutenção em modo interativo:

`pacdiff`

- Usa sudo e sudoedit para remover e mesclar arquivos:

`pacdiff --sudo`

- Reveja arquivos precisando de manutenção, criando `.bak`ups do original se você `s(O)brescrever`:

`pacdiff --sudo --backup`

- Usa um editor específico para ver e mesclar arquivos de configuração (o padrão é `vim -d`):

`DIFFPROG={{editor}} pacdiff`

- Procura arquivos de configuração com `locate` ao invés de usar o banco de dados do `pacman`:

`pacdiff --locate`

- Exibe ajuda:

`pacdiff --help`
