# pio org

> Gestionați organizațiile PlatForMio și proprietarii acestora.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/org/>

- Creați o nouă organizație:

`pio org create {{organization_name}}`

- Ștergeți o organizație:

`pio org destroy {{organization_name}}`

- Adăugați un utilizator la o organizație:

`pio org add {{organization_name}} {{username}}`

- Eliminarea unui utilizator dintr-o organizație:

`pio org remove {{organization_name}} {{username}}`

- Listează toate organizațiile în care utilizatorul curent este membru și proprietarii acestora:

`pio org list`

- Actualizați numele, adresa de e-mail sau numele afișat al unei organizații:

`pio org update --orgname {{new_organization_name}} --email {{new_email}} --displayname {{new_display_name}} {{organization_name}}`
