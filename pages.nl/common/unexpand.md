# unexpand

> Converteer spaties naar tabs.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/unexpand-invocation.html>.

- Converteer spaties in elk bestand naar tabs en schrijf naar `stdout`:

`unexpand {{pad/naar/bestand}}`

- Converteer spaties naar tabs en lees van `stdin`:

`unexpand`

- Converteer alle spaties, in plaats van alleen de voorloopspaties:

`unexpand {{[-a|--all]}} {{pad/naar/bestand}}`

- Converteer alleen leidende reeksen van spaties (overschrijft -a):

`unexpand --first-only {{pad/naar/bestand}}`

- Plaats tabs een bepaald aantal tekens uit elkaar, niet 8 (activeert -a):

`unexpand {{[-t|--tabs]}} {{nummer}} {{pad/naar/bestand}}`
