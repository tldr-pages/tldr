# conky

> Monitor de sistema ligero para X.
> Más información: <https://github.com/brndnmtthws/conky>.

- Ejecuta con la configuración por defecto:

`conky`

- Crea una nueva configuración por defecto:

`conky -C > ~/.conkyrc`

- Ejecuta conky con un archivo de configuración concreto:

`conky -c {{ruta/a/la/configuración}}`

- Ejecuta en segundo plano (*daemon*):

`conky -d`

- Alinea conky en el escritorio:

`conky -a {{{arriba,abajo,en_medio}_{izquierda,derecha,en_medio}}}`

- Pausa de 5 segundos al iniciar antes de ejecutarlo:

`conky -p {{5}}`
