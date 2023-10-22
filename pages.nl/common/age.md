# age

> Een eenvoudige, moderne en veilige tool voor het versleutelen van bestanden.
> Bekijk `age-keygen` hoe je sleutelparen kan genereren.
> Meer informatie: <https://github.com/FiloSottile/age>.

- Genereer een versleuteld bestand dat kan worden ontsleuteld met een wachtwoordzin:

`age --passphrase --output {{pad/naar/versleuteld_bestand}} {{pad/naar/niet-versleuteld_bestand}}`

- Versleutel een bestand met een of meer openbare sleutels die als letterlijke waarden worden ingevoerd (herhaal de `--recipient` flag om meerdere openbare sleutels op te geven):

`age --recipient {{openbare_sleutel}} --output {{pad/naar/versleuteld_bestand}} {{pad/naar/niet-versleuteld_bestand}}`

- Versleutel een bestand met een of meer openbare sleutels die zijn opgegeven in het bestand van een ontvanger:

`age --recipients-file {{pad/naar/ontvangers_bestand}} {{pad/naar/niet-versleuteld_bestand}} --output {{pad/naar/versleuteld_bestand}}`

- Decodeer een bestand met een wachtwoordzin:

`age --decrypt --output {{pad/naar/gedecodeerd_bestand}} {{pad/naar/versleuteld_bestand}}`

- Ontsleutel een bestand met een privésleutelbestand:

`age --decrypt --identity {{pad/naar/privé_sleutel_bestand}} --output {{pad/naar/gedecodeerd_bestand}} {{pad/naar/versleuteld_bestand}}`
