# dmenu

> Menú dinámico.
> Crea un menú a partir de una entrada de texto con cada elemento, en una nueva línea.
> Más información: <https://manned.org/dmenu>.

- Muestra un menú a partir de la salida del comando 'ls':

`{{ls}} | dmenu`

- Muestra un menú con artículos personalizados separados por una nueva línea (`\n`):

`echo -e "{{rojo}}\n{{verde}}\n{{azul}}" | dmenu`

- Deja que el usuario elija entre varios elementos y guarda el seleccionado en un archivo:

`echo -e "{{rojo}}\n{{verde}}\n{{azul}}" | dmenu > {{color.txt}}`

- Lanza dmenu en un monitor específico:

`ls | dmenu -m {{1}}`

- Muestra dmenu en la parte inferior de la pantalla:

`ls | dmenu -b`
