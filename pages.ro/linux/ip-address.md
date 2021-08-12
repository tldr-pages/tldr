# ip address

> subcomanda Gestionarea adreselor IP.

- Lista interfețelor de rețea și adresele IP asociate acestora:

`ip address`

- Filtrare pentru a afișa numai interfețele de rețea active:

`ip address show up`

- Afișați informații despre o anumită interfață de rețea:

`ip address show dev {{eth0}}`

- Adăugați o adresă IP la o interfață de rețea:

`ip address add {{ip_address}} dev {{eth0}}`

- Eliminați o adresă IP dintr-o interfață de rețea:

`ip address delete {{ip_address}} dev {{eth0}}`

- Ștergeți toate adresele IP dintr-un anumit domeniu de aplicare dintr-o interfață de rețea:

`ip address flush dev {{eth0}} scope {{global|host|link}}`
