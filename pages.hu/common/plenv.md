# plenv

> Váltás több Perl-verzió között. További információ: <https://github.com/tokuhirom/plenv>.

- Az aktuálisan kiválasztott Perl-verzió megjelenítése és annak kiválasztási módja:

`plenv version`

- Az összes elérhető telepített Perl verzió listázása:

`plenv versions`

- A globális Perl-verzió beállítása (ezt használják, hacsak nem egy helyi vagy shell-verzió élvez elsőbbséget):

`plenv global {{version}}`

- A helyi alkalmazásspecifikus Perl-verzió beállítása (az aktuális könyvtárban és az alatta lévő összes könyvtárban használatos):

`plenv local {{version}}`

- A shell-specifikus Perl verzió beállítása (csak az aktuális munkamenetben használatos):

`plenv shell {{version}}`

- Súgó megjelenítése:

`plenv`

- Súgó megjelenítése egy parancshoz:

`plenv help {{command}}`
