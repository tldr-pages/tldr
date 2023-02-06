# peludna-prognoza

> A horvát városok pollenmérési adatainak lekérése a terminálról a Pliva allergiák adatai API segítségével. További információ: <https://github.com/vladimyr/peludna-prognoza>.

- Indítson interaktív keresést egy városra, és kérjen le adatokat:

`peludna-prognoza`

- Adatok lekérése egy városhoz:

`peludna-prognoza "{{city}}"`

- Az adatok megjelenítése gépileg olvasható formátumban:

`peludna-prognoza "{{city}}" --{{json|xml}}`

- Egy város pollenmérési oldalának megjelenítése az alapértelmezett webböngészőben a <https://plivazdravlje.hr> címen:

`peludna-prognoza "{{city}}" --web`
