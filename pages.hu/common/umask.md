# umask

> A felhasználó által az újonnan létrehozott fájlok számára elrejtett (azaz korlátozott) olvasási/írási/végrehajtási engedélyek kezelése. További információ: <https://manned.org/umask>.

- Az aktuális maszk megjelenítése oktális jelölésben:

`umask`

- Az aktuális maszk megjelenítése szimbolikus (ember által olvasható) módban:

`umask -S`

- A maszk szimbolikus módosítása, hogy minden felhasználó számára engedélyezze az olvasási engedélyt (a maszk többi bitje változatlan marad):

`umask {{a+r}}`

- A maszk beállítása (oktális jelöléssel) úgy, hogy a fájl tulajdonosa számára ne korlátozza a jogosultságokat, mindenki más számára pedig korlátozza az összes jogosultságot:

`umask {{077}}`
