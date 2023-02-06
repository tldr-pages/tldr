# pidof

> Egy folyamat azonosítójának lekérdezése a neve alapján. További információ: <https://manned.org/pidof>.

- Listázza ki az adott névvel rendelkező összes folyamat azonosítóját:

`pidof {{bash}}`

- Egyetlen folyamat azonosítójának listázása adott névvel:

`pidof -s {{bash}}`

- Folyamatazonosítók listázása a megadott nevű szkriptekkel együtt:

`pidof -x {{script.py}}`

- Az összes megadott nevű folyamat megállítása:

`kill $(pidof {{name}})`
