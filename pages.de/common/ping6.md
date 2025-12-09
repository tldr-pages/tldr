# ping6

> Sendet ICMP ECHO_REQUEST Pakete an andere Geräte im Netzwerk, welche mittels IPv6-Adressen identifiziert werden.
> Weitere Informationen: <https://manned.org/ping6>.

- Sende Pings an ein Gerät im Netzwerk:

`ping6 {{ziel}}`

- Sende nur eine bestimmte Anzahl an Pings:

`ping6 -c {{anzahl}} {{ziel}}`

- Sende Pings und bestimme das Interval in Sekunden zwischen diesen (standardmäßig ist es eine Sekunde):

`ping6 -i {{sekunden}} {{ziel}}`

- Sende Pings ohne symbolische Namen nach Adressen aufzulösen:

`ping6 -n {{ziel}}`

- Sende Pings und signalisiere eine erfolgreiche Antwort durch ein Bell Signal (wenn das Terminal es unterstützt):

`ping6 -a {{ziel}}`
