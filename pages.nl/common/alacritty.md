# alacritty

> Cross-platform, GPU-versnelde terminalemulator.
> Meer informatie: <https://github.com/alacritty/alacritty>.

- Open een nieuw Alacritty-venster:

`alacritty`

- Uitvoeren in een specifieke map:

`alacritty --working-directory {{pad/naar/map}}`

- Voer een opdracht uit in een nieuw Alacritty-venster:

`alacritty -e {{bevel}}`

- Geef een alternatief configuratiebestand op (standaard ingesteld op `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{pad/naar/config.toml}}`

- Uitvoeren met live config reload ingeschakeld (kan ook standaard worden ingeschakeld in `alacritty.toml`):

`alacritty --live-config-reload --config-file {{pad/naar/config.toml}}`
