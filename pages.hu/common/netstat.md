# netstat

> Megjeleníti a hálózattal kapcsolatos információkat, például a nyitott kapcsolatokat, nyitott foglalatportokat stb. További információk: <https://man7.org/linux/man-pages/man8/netstat.8.html>.

- Listázza az összes portot:

`netstat --all`

- Az összes figyelő port listázása:

`netstat --listening`

- List listening TCP portok listája:

`netstat --tcp`

- PID és programnevek megjelenítése:

`netstat --program`

- Folyamatosan listázza az információkat:

`netstat --continuous`

- Útvonalak listázása és az IP-címek hostnévre való feloldása:

`netstat --route --numeric`

- A figyelő TCP és UDP portok listázása (+ felhasználó és folyamat, ha Ön a root):

`netstat --listening --program --numeric --tcp --udp --extend`
