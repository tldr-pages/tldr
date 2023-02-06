# socat

> Többcélú relé (SOcket CAT). További információ: <http://www.dest-unreach.org/socat/>.

- Figyel egy portra, vár egy bejövő kapcsolatra, és adatokat továbbít az STDIO-ra:

`socat - TCP-LISTEN:8080,fork`

- Létrehoz egy kapcsolatot egy állomáshoz és egy porthoz, az adatok STDIO-ban történő átvitele a csatlakoztatott állomáshoz:

`socat - TCP4:www.example.com:80`

- Egy helyi port bejövő adatainak továbbítása egy másik állomás és port felé:

`socat TCP-LISTEN:80,fork TCP4:www.example.com:80`
