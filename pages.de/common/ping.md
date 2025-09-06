# ping

> Sendet ICMP ECHO_REQUEST Pakete an andere Geräte im Netzwerk.
> Weitere Informationen: <https://manned.org/ping>.

- Sende Pings an ein Gerät im Netzwerk:

`ping {{ziel}}`

- Sende nur eine bestimmte Anzahl an Pings:

`ping -c {{anzahl}} {{ziel}}`

- Sende Pings und bestimme das Interval in Sekunden zwischen diesen (standardmäßig ist es eine Sekunde):

`ping -i {{sekunden}} {{ziel}}`

- Sende Pings ohne symbolische Namen nach Adressen aufzulösen:

`ping -n {{ziel}}`

- Sende Pings und signalisiere eine erfolgreiche Antwort durch ein Bell Signal (wenn das Terminal es unterstützt):

`ping -a {{ziel}}`

- Zeige auch eine Nachricht, wenn keine Antwort empfangen wurde:

`ping -O {{ziel}}`
