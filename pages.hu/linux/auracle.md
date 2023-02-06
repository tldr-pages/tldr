# auracle

> Parancssori eszköz, amely az Arch Linux felhasználói adattárával (AUR) való interakcióra szolgál. További információ: <https://github.com/falconindy/auracle>.

- Megjeleníti azokat az AUR csomagokat, amelyek megfelelnek egy reguláris kifejezésnek:

`auracle search '{{regular_expression}}'`

- Az AUR csomagok szóközzel elválasztott listájának csomaginformációinak megjelenítése:

`auracle info {{package1}} {{package2}}`

- A `PKGBUILD` fájl (build information) megjelenítése az AUR csomagok szóközzel elválasztott listájához:

`auracle show {{package1}} {{package2}}`

- A telepített AUR-csomagok frissítéseinek megjelenítése:

`auracle outdated`
