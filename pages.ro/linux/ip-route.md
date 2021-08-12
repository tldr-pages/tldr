# ip route

> subcomandă de gestionare a tabelului de rutare IP.
> Mai multe informaţii: <https://manned.org/ip-route>

- Afișează tabelul de rutare:

`ip route {{show|list}}`

- Adăugați o rută implicită utilizând redirecționarea gateway-ului:

`sudo ip route add default via {{gateway_ip}}`

- Adaugă o rută implicită folosind `eth0`:

`sudo ip route add default dev {{eth0}}`

- Adaugă o rută statică:

`sudo ip route add {{destination_ip}} via {{gateway_ip}} dev {{eth0}}`

- Ștergeți o rută statică:

`sudo ip route del {{destination_ip}} dev {{eth0}}`

- Schimbarea sau înlocuirea unei rute statice:

`sudo ip route {{change|replace}} {{destination_ip}} via {{gateway_ip}} dev {{eth0}}`

- Arată ce rută va fi folosită de nucleu pentru a ajunge la o adresă IP:

`ip route get {{destination_ip}}`
