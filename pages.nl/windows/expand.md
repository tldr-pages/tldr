# expand

> Pak Windows Cabinet bestanden uit.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/expand>.

- Pak een Cabinet bestand met één bestand naar de specifieke map:

`expand {{pad\naar\bestand.cab}} {{pad\naar\map}}`

- Toon een lijst van bestanden in een Cabinet bestand:

`expand {{pad\naar\bestand.cab}} {{pad\naar\map}} -d`

- Pak alle bestanden van een Cabinet bestand uit:

`expand {{pad\naar\bestand.cab}} {{pad\naar\map}} -f:*`

- Pak een specifiek bestand van een Cabinet bestand uit:

`expand {{pad\naar\bestand.cab}} {{pad\naar\map}} -f:{{pad\naar\bestand}}`

- Negeer de mapstructuur bij het uitpakken en voeg ze toe aan een enkele map:

`expand {{pad\naar\bestand.cab}} {{pad\naar\map}} -i`
