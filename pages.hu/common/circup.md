# circup

> A CircuitPython könyvtár frissítője. További információ: <https://github.com/adafruit/circup>.

- Interaktívan frissítheti a modulokat egy eszközön:

`circup update`

- Új könyvtár telepítése:

`circup install {{library_name}}`

- Könyvtár keresése:

`circup show {{partial_name}}`

- A csatlakoztatott eszközön lévő összes könyvtár listázása `requirements.txt` formátumban:

`circup freeze`

- A csatlakoztatott eszközön lévő összes könyvtár mentése az aktuális könyvtárba:

`circup freeze -r`
