# auracle

> Instrumentul de linie de comandă utilizat pentru a interacționa cu Depozitul de utilizatori al Arch Linux, denumit în mod obișnuit AUR.
> Mai multe informaţii: <https://github.com/falconindy/auracle>

- Afișează pachete AUR care se potrivesc cu o expresie regulată:

`auracle search '{{regular_expression}}'`

- Afișează informații despre pachet pentru o listă spațială de pachete AUR:

`auracle info {{package1}} {{package2}}`

- Afișează fișierul `PKGBUILD `(informații despre compilare) pentru o listă separată de spațiu a pachetelor AUR:

`auracle show {{package1}} {{package2}}`

- Afișează actualizări pentru pachetele AUR instalate:

`auracle outdated`
