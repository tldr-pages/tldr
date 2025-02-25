# alacritty

> Cross-platform, GPU-versnelde terminalemulator.
> Meer informatie: <https://github.com/alacritty/alacritty>.

- Open een nieuw Alacritty-venster:

`alacritty`

- Start de Alacritty daemon (zonder een venster te maken):

`alacritty --daemon`

- Maak een nieuw venster met behulp van het reeds lopende Alacritty proces:

`alacritty msg create-window`

- Uitvoeren in een specifieke map:

`alacritty --working-directory {{pad/naar/map}}`

- Vo[e]r een commando uit in een nieuw Alacritty-venster:

`alacritty -e {{commando}}`

- Geef een alternatief configuratiebestand op (standaard ingesteld op `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{pad/naar/config.toml}}`

- Uitvoeren met live config reload ingeschakeld (kan ook standaard worden ingeschakeld in `alacritty.toml`):

`alacritty --live-config-reload --config-file {{pad/naar/config.toml}}`
