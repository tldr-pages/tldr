# age

> Een eenvoudige, moderne en veilige tool voor het versleutelen van bestanden.
> Zie ook: `age-keygen` voor het genereren van sleutelparen.
> Meer informatie: <https://github.com/FiloSottile/age#usage>.

- Genereer een versleuteld bestand dat kan worden ontsleuteld met een wachtwoordzin:

`age {{[-p|--passphrase]}} {{[-o|--output]}} {{pad/naar/versleuteld_bestand}} {{pad/naar/niet-versleuteld_bestand}}`

- Versleutel een bestand met een of meer openbare sleutels die als letterlijke waarden worden ingevoerd (herhaal de `--recipient` flag om meerdere openbare sleutels op te geven):

`age {{[-r|--recipient]}} {{openbare_sleutel}} {{[-o|--output]}} {{pad/naar/versleuteld_bestand}} {{pad/naar/niet-versleuteld_bestand}}`

- Versleutel een bestand met een of meer openbare sleutels die zijn opgegeven in het bestand van een ontvanger:

`age {{[-R|--recipients-file]}} {{pad/naar/ontvangers_bestand}} {{[-o|--output]}} {{pad/naar/versleuteld_bestand}} {{pad/naar/niet-versleuteld_bestand}}`

- Decodeer een bestand met een wachtwoordzin:

`age {{[-d|--decrypt]}} {{[-o|--output]}} {{pad/naar/gedecodeerd_bestand}} {{pad/naar/versleuteld_bestand}}`

- Ontsleutel een bestand met een privésleutelbestand:

`age {{[-d|--decrypt]}} {{[-i|--identity]}} {{pad/naar/privé_sleutel_bestand}} {{[-o|--output]}} {{pad/naar/gedecodeerd_bestand}} {{pad/naar/versleuteld_bestand}}`
