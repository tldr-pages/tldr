# named

> A DNS (Dynamic Name Service) kiszolgáló démon futtatása, amely az állomásneveket IP-címekké alakítja és fordítva. További információ: <https://manned.org/named>.

- Olvassa be az alapértelmezett konfigurációs fájlt `/etc/named.conf`, olvassa be az esetleges kezdeti adatokat és figyeljen a lekérdezésekre:

`named`

- Egyéni konfigurációs fájl beolvasása:

`named -c {{path/to/named.conf}}`

- Kizárólag IPv4 vagy IPv6 protokollt használjon, még akkor is, ha az állomásgép más protokollok használatára is képes:

`named {{-4|-6}}`

- A lekérdezések figyelése egy adott porton az alapértelmezett 53-as port helyett:

`named -p {{port}}`

- A kiszolgálót előtérben futtassa, és ne démonizáljon:

`named -f`
