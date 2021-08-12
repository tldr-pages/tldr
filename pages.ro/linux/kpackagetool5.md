# kpackagetool5

> KPackage Manager: Instalează, listează, elimină pachetele Plasma.
> Mai multe informaţii: <https://techbase.kde.org/Development/Tutorials/Plasma5/QML2/GettingStarted#Kpackagetool5>

- Listează toate tipurile cunoscute de pachete care pot fi instalate:

`kpackagetool5 --list-types`

- Instalați pachetul dintr-un director:

`kpackagetool5 --type {{package_type}} --install {{path/to/directory}}`

- Actualizare pachet instalat dintr-un director:

`kpackagetool5 --type {{package_type}} --upgrade {{path/to/directory}}`

- Lista plasmoidelor instalate (—global pentru toți utilizatorii):

`kpackagetool5 --type Plasma/Applet --list --global`

- Eliminați un plasmoid după nume:

`kpackagetool5 --type Plasma/Applet --remove "{{name}}"`
