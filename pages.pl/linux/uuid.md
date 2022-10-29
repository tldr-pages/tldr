# uuid

> Twórz i dekoduj uniwersalne identyfikatory (UUID).
> Zobacz też `uuidgen`.
> Więcej informacji: <https://manned.org/uuid>.

- Stwórz UUIDv1 (oparte o zegar systemowy i - jeśli dostępne - adres sprzętowy):

`uuid`

- Stwórz UUIDv4 (losowy):

`uuid -v {{4}}`

- Stwórz wiele UUIDv4 na raz:

`uuid -v {{4}} -n {{ilość_uuid}}`

- Stwórz UUIDv4 w konkretnym formacie:

`uuid -v {{4}} -F {{BIN|STR|SIV}}`

- Stwórz UUIDv4 i zapisz do pliku:

`uuid -v {{4}} -o {{ścieżka/do/pliku}}`

- Stwórz UUIDv5 (oparty o podaną nazwę obiektu) w przestrzeni nazw:

`uuid -v {{5}} ns:{{DNS|URL|OID|X500}} {{nazwa_obiektu}}`

- Dekoduj podany UUID:

`uuid -d {{uuid}}`
