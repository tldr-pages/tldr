# kpackagetool6

> KPackage Manager: instala, lista, elimina paquetes Plasma.
> Más información: <https://manned.org/kpackagetool6>.

- Lista todos los tipos de paquetes conocidos que se pueden instalar:

`kpackagetool6 --list-types`

- Instala el paquete desde un directorio:

`kpackagetool6 --type {{tipo_paquete}} --install {{ruta/a/directorio}}`

- Actualiza el paquete instalado desde un directorio:

`kpackagetool6 --type {{tipo_paquete}} --upgrade {{ruta/a/directorio}}`

- Lista los plasmoides instalados (`--global` para todos los usuarios):

`kpackagetool6 --type Plasma/Applet --list --global`

- Elimina un plasmoide por su nombre:

`kpackagetool6 --type Plasma/Applet --remove "{{nombre}}"`
