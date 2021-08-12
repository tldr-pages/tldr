# named

> Executați daemonul serverului DNS (Dynamic Name Service) care convertește numele de gazdă la adrese IP și invers.
> Mai multe informaţii: <https://manned.org/named>

- Citiți fișierul de configurare implicit `/etc/named.conf`, citiți orice date inițiale și ascultați interogările:

`named`

- Citiți un fișier de configurare personalizat:

`named -c {{path/to/named.conf}}`

- Utilizați numai IPv4 sau IPv6, chiar dacă mașina gazdă este capabilă să utilizeze alte protocoale:

`named {{-4|-6}}`

- Ascultați interogările pe un anumit port în loc de portul implicit 53:

`named -p {{port}}`

- Rulați serverul în prim-plan și nu daemonize:

`named -f`
