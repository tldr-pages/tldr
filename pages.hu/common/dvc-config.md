# dvc config

> Alacsony szintű parancs a dvc tárolók egyéni konfigurációs opcióinak kezelésére. Ezek a konfigurációk lehetnek projekt, helyi, globális vagy rendszerszintűek. További információ: <https://dvc.org/doc/command-reference/config>.

- Az alapértelmezett távoli rendszer nevének lekérdezése:

`dvc config core.remote`

- A projekt alapértelmezett távirányítójának beállítása:

`dvc config core.remote {{remote_name}}`

- A projekt alapértelmezett távoli beállításának feloldása:

`dvc config --unset core.remote`

- Egy megadott kulcs konfigurációs értékének lekérdezése az aktuális projekthez:

`dvc config {{key}}`

- Egy kulcs konfigurációs értékének beállítása projektszinten:

`dvc config {{key}} {{value}}`

- Egy adott kulcs projekt szintű konfigurációs értékének visszaállítása:

`dvc config --unset {{key}}`

- Helyi, globális vagy rendszerszintű konfigurációs érték beállítása:

`dvc config --local/global/system {{key}} {{value}}`
