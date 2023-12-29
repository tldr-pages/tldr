# pio ci

> Bouw PlatformIO projects met een arbitraire broncode structuur.
> Dit zal een tijdelijk project maken waar naartoe de broncode gekopieerd zal worden.
> Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_ci.html>.

- Bouw een PlatformIO project in de standaard systeem tijdelijke map en verwijder het naderhand:

`pio ci {{pad/naar/project}}`

- Bouw een PlatformIO project en specificeer specifieke bibliotheken:

`pio ci --lib {{pad/naar/bibliotheek_map}} {{pad/naar/project}}`

- Bouw een PlatformIO project en specificeer een specifiek board (`pio boards` toont ze allemaal):

`pio ci --board {{board}} {{pad/naar/project}}`

- Bouw een PlatformIO project in een specifieke map:

`pio ci --build-dir {{pad/naar/bouw_map}} {{pad/naar/project}}`

- Bouw een PlatformIO project en verwijder de bouwmap niet:

`pio ci --keep-build-dir {{pad/naar/project}}`

- Bouw een PlatformIO project met een specifiek configuratiebestand:

`pio ci --project-conf {{pad/naar/platformio.ini}}`
