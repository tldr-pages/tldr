# flatpak

> Flatpak alkalmazások és futásidejű programok készítése, telepítése és futtatása. További információ: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Egy telepített alkalmazás futtatása:

`flatpak run {{name}}`

- Alkalmazás telepítése távoli forrásból:

`flatpak install {{remote}} {{name}}`

- Az összes telepített alkalmazás és futóidő listázása:

`flatpak list`

- Az összes telepített alkalmazás és futóidő frissítése:

`flatpak update`

- Távoli forrás hozzáadása:

`flatpak remote-add --if-not-exists {{remote_name}} {{remote_url}}`

- Telepített alkalmazás eltávolítása:

`flatpak remove {{name}}`

- Az összes nem használt alkalmazás eltávolítása:

`flatpak remove --unused`

- Információk megjelenítése a telepített alkalmazásról:

`flatpak info {{name}}`
