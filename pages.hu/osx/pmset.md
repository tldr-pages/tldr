# pmset

> A macOS energiagazdálkodási beállításainak konfigurálása, ahogyan azt a Rendszerbeállítások > Energiatakarékosság menüpontban is megteheti. A beállításokat módosító parancsoknak a `sudo` kezdőbetűvel kell kezdődniük. További információ: <https://ss64.com/osx/pmset.html>.

- Az aktuális energiagazdálkodási beállítások megjelenítése:

`pmset -g`

- Az aktuális energiaforrás és akkumulátor szintjének megjelenítése:

`pmset -g batt`

- A kijelző azonnali alvó üzemmódba helyezése:

`pmset displaysleepnow`

- A kijelzőt úgy állítsa be, hogy töltő áramellátása esetén soha ne aludjon el:

`sudo pmset -c displaysleep 0`

- A kijelzőt 15 perc után alvó üzemmódba állítani, ha akkumulátortöltővel működik:

`sudo pmset -b displaysleep 15`

- A számítógép automatikus ébredésének ütemezése minden hétköznap reggel 9 órára:

`sudo pmset repeat wake MTWRF 09:00:00`

- A rendszer alapértelmezett állapotának visszaállítása:

`sudo pmset -a displaysleep 10 disksleep 10 sleep 30 womp 1`
