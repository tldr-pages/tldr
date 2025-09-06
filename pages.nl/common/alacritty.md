# alacritty

> Cross-platform, GPU-versnelde terminalemulator.
> Meer informatie: <https://manned.org/alacritty>.

- Open een nieuw Alacritty-venster:

`alacritty`

- Start de Alacritty daemon (zonder een venster te maken):

`alacritty --daemon`

- Maak een nieuw venster met behulp van het reeds lopende Alacritty proces:

`alacritty msg create-window`

- Voer in een specifieke map uit (werkt ook met `alacritty msg create-window`):

`alacritty --working-directory {{pad/naar/map}}`

- Voer een commando uit in een nieuw Alacritty-venster (werkt ook met `alacritty msg create-window`):

`alacritty {{[-e|--command]}} {{commando}}`

- Geef een alternatief configuratiebestand op (standaard ingesteld op `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{pad/naar/config.toml}}`
