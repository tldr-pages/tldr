# archinstall

> Begeleidende Arch Linux installatie.
> Meer informatie: <https://archinstall.archlinux.page/installing/guided.html>.

- Start de interactieve installatie:

`archinstall`

- Start de interactieve installer en genereer een configuratiebestand in plaats van te installeren:

`archinstall --dry-run`

- Schakel geavanceerde instellingen in:

`archinstall --advanced`

- Installeer met de opgegeven configuratiebestanden:

`archinstall --config {{pad/naar/config.json}} --creds {{pad/naar/credentials.json}}`

- Installeer met een configuratiebestand van een externe server:

`archinstall --config-url {{https://example.com/config.json}} --creds-url {{https://example.com/credentials.json}}`

- Installeer met behulp van het opgegeven script:

`archinstall --script {{minimal|only_hd}}`
