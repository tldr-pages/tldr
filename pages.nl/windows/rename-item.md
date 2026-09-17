# Rename-Item

> Powershell commando om een item te hernoemen.
> Opmerking: `ren` en `rni` kunnen beiden gebruikt worden als een alias voor `Rename-Item`.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/rename-item>.

- Hernoem een bestand:

`Rename-Item -Path "{{pad\naar\bestand}}" -NewName "{{nieuwe_bestandsnaam}}"`

- Hernoem een map:

`Rename-Item -Path "{{pad\naar\bestand}}" -NewName "{{nieuwe_mapnaam}}"`

- Hernoem en verplaats een bestand:

`Rename-Item -Path "{{pad\naar\bestand}}" -NewName "{{pad\naar\nieuwe_bestandsnaam}}"`

- Hernoem een bestand geforceerd:

`Rename-Item -Path "{{pad\naar\bestand}}" -NewName "{{nieuwe_bestandsnaam}}" -Force`

- Vraag om bevestiging voordat een bestand wordt hernoemd:

`Rename-Item -Path "{{pad\naar\bestand}}" -NewName "{{nieuwe_bestandsnaam}}" {{[-Confirm|-cf]}}`
