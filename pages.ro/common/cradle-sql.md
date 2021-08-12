# cradle sql

> Gestionați bazele de date Cradle SQL.
> Mai multe informaţii: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>

- Reconstruiți schema bazei de date:

`cradle sql build`

- Reconstruiți schema bazei de date pentru un anumit pachet:

`cradle sql build {{package_name}}`

- Goliți întreaga bază de date:

`cradle sql flush`

- Goliți tabelele bazei de date pentru un anumit pachet:

`cradle sql flush {{package_name}}`

- Populați tabelele pentru toate pachetele:

`cradle sql populate`

- Populați tabelele pentru un anumit pachet:

`cradle sql populate {{package_name}}`
