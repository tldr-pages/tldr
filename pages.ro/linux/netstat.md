# netstat

> Afișează informații legate de rețea, cum ar fi conexiuni deschise, porturi open socket etc.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/netstat.8.html>

- Lista tuturor porturilor:

`netstat --all`

- Listează toate porturile de ascultare:

`netstat --listening`

- Listă de ascultare porturi TCP:

`netstat --tcp`

- Afișează numele PID și ale programului:

`netstat --program`

- Lista informațiilor în mod continuu:

`netstat --continuous`

- Listează rutele și nu rezolvă adresele IP la numele de gazdă:

`netstat --route --numeric`

- Listă de ascultare TCP și UDP porturi (+ utilizator și proces dacă sunteți root):

`netstat --listening --program --numeric --tcp --udp --extend`
