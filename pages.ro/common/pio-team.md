# pio team

> Gestionați echipele PlatForMio.
> Mai multe informaţii: <https://docs.platformio.org/en/latest/core/userguide/team/>

- Creați o nouă echipă cu descrierea specificată:

`pio team create --description {{description}} {{organization_name}}:{{team_name}}`

- Şterge o echipă:

`pio team destroy {{organization_name}}:{{team_name}}`

- Adaugă un utilizator nou la o echipă:

`pio team add {{organization_name}}:{{team_name}} {{username}}`

- Eliminați un utilizator dintr-o echipă:

`pio team remove {{organization_name}}:{{team_name}} {{username}}`

- Listează toate echipele din care face parte utilizatorul și membrii lor:

`pio team list`

- Listează toate echipele dintr-o organizație:

`pio team list {{organization_name}}`

- Redenumeşte o echipă:

`pio team update --name {{new_team_name}} {{organization_name}}:{{team_name}}`

- Modificați descrierea unei echipe:

`pio team update --description {{new_description}} {{organization_name}}:{{team_name}}`
