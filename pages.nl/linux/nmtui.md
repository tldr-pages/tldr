# nmtui

> Tekstgebruikersinterface voor controle over NetworkManager.
> Gebruik pijltoetsen om te navigeren en gebruik Enter om een optie te selecteren.
> Meer informatie: <https://networkmanager.dev/docs/api/latest/nmtui.html>.

- Open de gebruikersinterface:

`nmtui`

- Toon een lijst met alle beschikbare verbindingen, met de optie om deze te activeren danwel te deactiveren:

`nmtui connect`

- Verbind met een gegeven netwerk:

`nmtui connect {{naam|uuid|apparaat|SSID}}`

- Pas aan/Voeg toe/Verwijder een gegeven netwerk:

`nmtui edit {{naam|id}}`

- Stel de systeemhostnaam in:

`nmtui hostname`
