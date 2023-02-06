# tlmgr gui

> A `tlmgr` grafikus felhasználói felületének elindítása.`tlmgr gui` függ a `perl-tk` csomagtól, amelyet kézzel kell telepíteni. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- A `tlmgr` grafikus felhasználói felületének elindítása:

`sudo tlmgr gui`

- Indítson el egy GUI-t a háttérszín megadásával:

`sudo tlmgr gui -background "{{#f39bc3}}"`

- GUI indítása az előtér színének megadásával:

`sudo tlmgr gui -foreground "{{#0ef3bd}}"`

- GUI indítása a betűtípus és a betűméret megadásával:

`sudo tlmgr gui -font "{{helvetica 18}}"`

- Egy adott geometria beállítását végző GUI elindítása:

`sudo tlmgr gui -geometry {{width}}x{{height}}-{{xpos}}+{{ypos}}`

- GUI indítása egy tetszőleges X-erőforrás karakterlánc átadásával:

`sudo tlmgr gui -xrm {{xresource}}`
