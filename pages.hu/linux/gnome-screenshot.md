# gnome-screenshot

> A képernyő, egy ablak vagy egy felhasználó által meghatározott terület rögzítése és a kép elmentése egy fájlba. További információ: <https://manned.org/gnome-screenshot>.

- Képernyőkép készítése és mentése az alapértelmezett helyre, általában a `~/Pictures`:

`gnome-screenshot`

- Képernyőkép készítése és mentése a megnevezett fájlhelyre:

`gnome-screenshot --file {{path/to/file}}`

- Képernyőkép készítése és mentése a vágólapra:

`gnome-screenshot --clipboard`

- Képernyőkép készítése a megadott számú másodperc után:

`gnome-screenshot --delay {{5}}`

- A GNOME képernyőfotó felhasználói felületének elindítása:

`gnome-screenshot --interactive`

- Képernyőkép készítése az aktuális ablakról és mentése a megadott fájlhelyre:

`gnome-screenshot --window --file {{path/to/file}}`

- Képernyőkép készítése a megadott számú másodperc után és mentése a vágólapra:

`gnome-screenshot --delay {{10}} --clipboard`

- A verzió megjelenítése:

`gnome-screenshot --version`
