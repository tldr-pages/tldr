# kpackagetool5

> KPackage Manager: További információ: <https://techbase.kde.org/Development/Tutorials/Plasma5/QML2/GettingStarted#Kpackagetool5>.

- Listázza az összes ismert telepíthető csomagtípust:

`kpackagetool5 --list-types`

- Telepítse a csomagot egy könyvtárból:

`kpackagetool5 --type {{package_type}} --install {{path/to/directory}}`

- A telepített csomag frissítése egy könyvtárból:

`kpackagetool5 --type {{package_type}} --upgrade {{path/to/directory}}`

- A telepített plazmák listázása (--global minden felhasználó számára):

`kpackagetool5 --type Plasma/Applet --list --global`

- Plazmoid eltávolítása név szerint:

`kpackagetool5 --type Plasma/Applet --remove "{{name}}"`
