# compgen

> Un comando integrado para autocompletar en Bash, que se invoca al presionar la tecla `<Tab>` dos veces.
> Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-compgen>.

- Lista todos los comandos que podría ejecutar:

`compgen -c`

- Lista todos los alias:

`compgen -a`

- Lista todas las funciones que podría ejecutar:

`compgen -A function`

- Muestra palabras reservadas de la interfaz de comandos (shell):

`compgen -k`

- Muestra todos los comandos/alias disponibles comenzando con 'ls':

`compgen -ac {{ls}}`
