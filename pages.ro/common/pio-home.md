# pio home

> Lansați serverul web PlatForMio Home.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>

- Deschideți PlatForMio Home în browserul web implicit:

`pio home`

- Utilizați un anumit port HTTP (implicit la 8008):

`pio home --port {{port}}`

- Legați la o anumită adresă IP (valori implicite la 127.0.0.1):

`pio home --host {{ip_address}}`

- Nu deschideți automat PlatForMio Home în browserul web implicit:

`pio home --no-open`

- Oprirea automată a serverului la timeout (în secunde) atunci când nu există clienți sunt conectați:

`pio home --shutdown-timeout {{time}}`

- Specificați un identificator unic de sesiune pentru a menține PlatForMio Home izolat de alte instanțe și protejat de accesul terților:

`pio home --session-id {{id}}`
