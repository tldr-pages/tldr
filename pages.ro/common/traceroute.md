# traceroute

> Imprimați traseul pachetelor de traseu către gazda de rețea.

- Traceroute la o gazdă:

`traceroute {{host}}`

- Dezactivați adresa IP și maparea numelui gazdei:

`traceroute -n {{host}}`

- Specificați timpul de așteptare pentru răspuns:

`traceroute -w {{0.5}} {{host}}`

- Specificați numărul de interogări pe hamei:

`traceroute -q {{5}} {{host}}`

- Specificați dimensiunea în octeți a pachetului de sondare:

`traceroute {{host}} {{42}}`
