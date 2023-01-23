# distrobox-create

> Distrobox konténerek létrehozása egy bemeneti névvel és képpel. A létrehozott konténer szorosan integrálódik a hosztba, lehetővé téve a felhasználó HOME könyvtárának, a külső tárolóknak, külső usb eszközöknek és grafikus alkalmazásoknak (X11/Wayland), valamint hangnak a megosztását. További információ: <https://distrobox.privatedns.org>.

- Hozzon létre egy disztroboxot az Alpine image segítségével:

`distrobox-create {{container_name}} --image alpine`

- Egy disztrobox klónozása:

`distrobox-create --clone {{container_name}} {{cloned_container_name}}`
