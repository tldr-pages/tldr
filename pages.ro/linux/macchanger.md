# macchanger

> Utilitar de linie de comandă pentru manipularea adreselor MAC de interfață de rețea.

- Vizualizaţi adresele MAC curente şi permanente ale unei interfeţe:

`macchanger --show {{interface}}`

- Setați interfața la un MAC aleator:

`macchanger --random {{interface}}`

- Setați interfața la un anumit MAC:

`macchanger --mac {{XX:XX:XX:XX:XX:XX}} {{interface}}`

- Resetați interfața la MAC hardware permanent:

`macchanger --permanent {{interface}}`
