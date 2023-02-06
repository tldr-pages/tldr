# zenity

> A parancssorból/shell szkriptekből származó párbeszédpanelek megjelenítése. Visszaadja a felhasználó által beírt értékeket vagy hiba esetén 1-et. További információ: <https://manned.org/zenity>.

- Az alapértelmezett kérdés párbeszédpanel megjelenítése:

`zenity --question`

- A "Hello!" szöveget megjelenítő információs párbeszédpanel megjelenítése:

`zenity --info --text="{{Hello!}}"`

- Név/jelszó űrlap megjelenítése és az adatok ";"-val elválasztva történő kiadása:

`zenity --forms --add-entry="{{Name}}" --add-password="{{Password}}" --separator="{{;}}"`

- Egy fájlkiválasztó űrlap megjelenítése, amelyben a felhasználó csak könyvtárakat választhat ki:

`zenity --file-selection --directory`

- Megjeleníteni egy előrehaladási sávot, amely másodpercenként frissíti az üzenetét, és megjeleníti a haladás százalékos értékét:

`{{(echo "#1"; sleep 1; echo "50"; echo "#2"; sleep 1; echo "100")}} | zenity --progress`
