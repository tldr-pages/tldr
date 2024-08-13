# tldr

> Muestra páginas de ayuda simples para herramientas de línea de comandos del proyecto tldr-pages.
> Nota: las opciones `--language` y `--list` no son requeridas por la especificación del cliente, pero la mayoría de los mismos las implementan.
> Más información: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Imprime la página tldr para un comando específico (pista: ¡así es como has llegado hasta aquí!):

`tldr {{comando}}`

- Imprime la página tldr para un subcomando específico:

`tldr {{comando}} {{subcomando}}`

- Imprime la página tldr para un comando en el [L]enguaje dado (si está disponible, de lo contrario vuelve al inglés):

`tldr --language {{código_de_lenguaje}} {{comando}}`

- Imprime la página tldr para un comando de una [p]lataforma específica:

`tldr --platform {{android|common|freebsd|linux|osx|netbsd|openbsd|sunos|windows}} {{comando}}`

- Actualiza la caché local de páginas tldr:

`tldr --update`

- [l]ista todas las páginas para la plataforma actual y `common`:

`tldr --list`

- [l]ista todas las páginas de subcomandos disponibles para un comando:

`tldr --list | grep {{comando}} | column`
