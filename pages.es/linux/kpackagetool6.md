# kpackagetool6

> KPackage Manager: instala, lista, elimina paquetes Plasma.
> Más información: <https://manned.org/kpackagetool6>.

- Lista todos los tipos de paquetes conocidos que se pueden instalar:

`kpackagetool6 --list-types`

- Instala el paquete desde un directorio:

`kpackagetool6 {{[-t|--type]}} {{tipo_paquete}} {{[-i|--install]}} {{ruta/al/directorio}}`

- Actualiza el paquete instalado desde un directorio:

`kpackagetool6 {{[-t|--type]}} {{tipo_paquete}} {{[-u|--upgrade]}} {{ruta/al/directorio}}`

- Lista los plasmoides instalados (`--global` para todos los usuarios):

`kpackagetool6 {{[-t|--type]}} Plasma/Applet {{[-l|--list]}} {{[-g|--global]}}`

- Elimina un plasmoide por su nombre:

`kpackagetool6 {{[-t|--type]}} Plasma/Applet {{[-r|--remove]}} "{{nombre}}"`
