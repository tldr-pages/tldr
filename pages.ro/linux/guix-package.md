# guix package

> Instalați, actualizați și eliminați pachetele Guix sau reveniți la configurațiile anterioare.
> Mai multe informaţii: <https://guix.gnu.org/manual/html_node/Invoking-guix-package.html>

- Instalați un pachet nou:

`guix package -i {{package_name}}`

- Elimină un pachet:

`guix package -r {{package_name}}`

- Căutați în baza de date a pachetelor o expresie regulată:

`guix package -s "{{search_pattern}}"`

- Lista pachetelor instalate:

`guix package -I`

- Lista generațiilor:

`guix package -l`

- Reveniți la generația anterioară:

`guix package --roll-back`
