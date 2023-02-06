# finger

> Felhasználói információk kereső program. További információ: <https://manned.org/finger>.

- Az aktuálisan bejelentkezett felhasználókról szóló információk megjelenítése:

`finger`

- Információk megjelenítése egy adott felhasználóról:

`finger {{username}}`

- A felhasználó bejelentkezési nevének, valódi nevének, terminálnevének és egyéb információinak megjelenítése:

`finger -s`

- Többsoros kimeneti formátum előállítása, amely ugyanazt az információt jeleníti meg, mint a `-s`, valamint a felhasználó otthoni könyvtárát, otthoni telefonszámát, bejelentkezési héját, levelezési állapotát stb:

`finger -l`

- Megakadályozza a felhasználói nevekkel való egyezést, és csak a bejelentkezési neveket használja:

`finger -m`
