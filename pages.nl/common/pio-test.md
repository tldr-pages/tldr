# pio test

> Voer lokale testen uit op een PlatformIO project.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>.

- Voer alle testen in alle omgevingen uit van het huidige PlatformIO project:

`pio test`

- Test alleen op specifieke omgevingen:

`pio test {{[-e|--environment]}} {{omgeving1}} {{[-e|--environment]}} {{omgeving2}}`

- Voer alleen testen uit die qua naam overeenkomen met een specifiek glob patroon:

`pio test {{[-f|--filter]}} "{{patroon}}"`

- Negeer testen die qua naam overeenkomen met een specifiek glob patroon:

`pio test {{[-i|--ignore]}} "{{patroon}}"`

- Specificeer een poort voor firmware uploading:

`pio test --upload-port {{upload_poort}}`

- Specificeer een aangepast configuratiebestand voor het uitvoeren van de testen:

`pio test {{[-c|--project-conf]}} {{pad/naar/platformio.ini}}`
