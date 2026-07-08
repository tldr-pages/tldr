# ip route get

> Ottiene una singola route verso una destinazione e stampa il suo contenuto esattamente come lo vede il kernel.
> Maggiori informazioni: <https://manned.org/ip-route>.

- Stampa la route verso una destinazione:

`ip {{[r|route]}} {{[g|get]}} {{1.1.1.1}}`

- Stampa la route verso una destinazione da un indirizzo sorgente specifico:

`ip {{[r|route]}} {{[g|get]}} {{destination}} from {{source}}`

- Stampa la route verso una destinazione per pacchetti in arrivo su un'interfaccia specifica:

`ip {{[r|route]}} {{[g|get]}} {{destination}} iif {{ethX}}`

- Stampa la route verso una destinazione, forzando l'output attraverso un'interfaccia specifica:

`ip {{[r|route]}} {{[g|get]}} {{destination}} oif {{ethX}}`

- Stampa la route verso una destinazione con un Type of Service (ToS) specificato:

`ip {{[r|route]}} {{[g|get]}} {{destination}} tos {{0x10}}`

- Stampa la route verso una destinazione usando una specifica istanza VRF (Virtual Routing and Forwarding):

`ip {{[r|route]}} {{[g|get]}} {{destination}} vrf {{myvrf}}`
