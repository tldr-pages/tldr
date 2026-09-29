# archinstall

> Begeleidende Arch Linux installer.
> Meer informatie: <https://archinstall.archlinux.page/installing/guided.html>.

- Start de interactieve installatie:

`archinstall`

- Simuleer een installatie door de interactieve installer te doorlopen, en genereer een configuratiebestand zonder te installeren:

`archinstall --dry-run`

- Schakel geavanceerde instellingen in:

`archinstall --advanced`

- Installeer met de opgegeven configuratiebestanden:

`archinstall --config {{pad/naar/config.json}} --creds {{pad/naar/credentials.json}}`

- Installeer met configuratiebestanden van een externe server:

`archinstall --config-url {{https://example.com/config.json}} --creds-url {{https://example.com/credentials.json}}`

- Installeer met behulp van het opgegeven script:

`archinstall --script {{minimal|only_hd}}`
