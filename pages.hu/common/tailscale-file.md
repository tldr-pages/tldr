# tailscale file

> Fájlok küldése a Tailscale hálózaton csatlakoztatott eszközök között. Jelenleg nem támogatja a fájlok küldését más felhasználók eszközeire, még ugyanazon a Tailscale hálózaton belül sem. További információ: <https://tailscale.com/kb/1106/taildrop/>.

- Fájl küldése egy adott csomópontra:

`sudo tailscale file cp {{path/to/file}} {{hostname|ip}}:`

- Az aktuális csomópontra küldött fájlok tárolása egy adott könyvtárba:

`sudo tailscale file get {{path/to/directory}}`
