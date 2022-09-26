# xrdb

> Utilitário de base de dados de recursos para servidor X window em sistemas tipo Unix.
> Mais informações: <https://www.x.org/releases/X11R7.7/doc/man/man1/xrdb.1.xhtml>.

- Iniciar `xrdb` em modo interactivo:

`xrdb`

- Carregar valores (p. ex. regras de estilo) de um ficheiro de recursos:

`xrdb -load {{~/.Xresources}}`

- Consultar base de dados de recursos e mostrar estado actual dos recursos:

`xrdb -query`
