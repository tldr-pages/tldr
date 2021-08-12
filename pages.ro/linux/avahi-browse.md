# avahi-browse

> Afișează serviciile și gazdele expuse în rețeaua locală prin MDNS/DNS-SD.
> Avahi este compatibil cu Bonjour (Zeroconf) găsit în dispozitivele Apple.
> Mai multe informaţii: <https://www.avahi.org/>

- Listați toate serviciile disponibile în rețeaua locală, împreună cu adresele și porturile acestora, ignorând cele locale:

`avahi-browse --all --resolve --ignore-local`

- Listează toate domeniile:

`avahi-browse --browse-domains`

- Limitați căutarea la un anumit domeniu:

`avahi-browse --all --domain={{domain}}`
