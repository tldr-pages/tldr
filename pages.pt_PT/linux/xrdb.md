# xrdb

> Utilitário de base de dados de recursos para servidor X window em sistemas tipo Unix.
> Mais informações: <https://www.x.org/releases/X11R7.7/doc/man/man1/xrdb.1.xhtml>.

- Inicia `xrdb` em modo interactivo:

`xrdb`

- Carrega valores (p. ex. regras de estilo) de um ficheiro de recursos:

`xrdb -load {{~/.Xresources}}`

- Consulta base de dados de recursos e mostra estado actual dos recursos:

`xrdb -query`
