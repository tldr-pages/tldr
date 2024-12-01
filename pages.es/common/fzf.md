# fzf

> Buscador aproximado (fuzzy search) de la línea de comando.
> Parecido a `sk`.
> Más información: <https://github.com/junegunn/fzf>.

- Aplica `fzf` a todos los archivos en el directorio especificado:

`find {{ruta/al/directorio}} -type f | fzf`

- Aplica `fzf` a los procesos en ejecución:

`ps aux | fzf`

- Selecciona varios archivos con `Shift + Tab` y los escribe a un archivo:

`find {{ruta/al/directorio}} -type f | fzf --multi > {{ruta/al/archivo}}`

- Aplica `fzf` con una consulta especificada:

`fzf --query "{{consulta}}"`

- Aplica `fzf` en las entradas que comienzan con `programa` y finalizan con `go`, `rb`, o `py`:

`fzf --query "^programa go$ | rb$ | py$"`

- Aplica `fzf` en entradas que no coinciden con `pyc` y coinciden exactamente con `travis`:

`fzf --query "!pyc 'travis"`
