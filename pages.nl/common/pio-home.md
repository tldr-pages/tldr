# pio home

> Lanceer de PlatformIO Home web server.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>.

- Open PlatformIO Home in de standaard web browser:

`pio home`

- Gebruik een specifieke HTTP poort (standaard 8008):

`pio home --port {{poort}}`

- Koppel aan een specifiek IP adres (standaard 127.0.0.1):

`pio home --host {{ip_adres}}`

- Open niet automatisch PlatformIO Home in de standaard web browser:

`pio home --no-open`

- Sluit de server af na n (in seconden) als er niemand verbonden is:

`pio home --shutdown-timeout {{n}}`

- Specificeer een unieke sessie identificatie om PlatformIO Home geïsoleerd te houden van andere instances en beschermd van toegang van derde partijen:

`pio home --session-id {{id}}`
