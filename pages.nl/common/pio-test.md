# pio test

> Voer lokale testen uit op een PlatformIO project.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>.

- Voer alle testen in alle omgevingen uit van het huidige PlatformIO project:

`pio test`

- Test alleen op specifieke omgevingen:

`pio test --environment {{omgeving1}} --environment {{omgeving2}}`

- Voer alleen testen uit die qua naam overeenkomen met een specifiek glob patroon:

`pio test --filter "{{patroon}}"`

- Negeer testen die qua naam overeenkomen met een specifiek glob patroon:

`pio test --ignore "{{patroon}}"`

- Specificeer een poort voor firmware uploading:

`pio test --upload-port {{upload_poort}}`

- Specificeer een aangepast configuratiebestand voor het uitvoeren van de testen:

`pio test --project-conf {{pad/naar/platformio.ini}}`
