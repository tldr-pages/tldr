# age

> Een eenvoudige, moderne en veilige tool voor het versleutelen van bestanden.
> Meer informatie: <https://github.com/FiloSottile/age>.

- Genereer een versleuteld bestand dat kan worden ontsleuteld met een wachtwoordzin:

`age --passphrase --output {{pad/naar/versleuteld_bestand}} {{pad/naar/niet-versleuteld_bestand}}`

- Genereer een sleutelpaar, sla de privésleutel op in een niet-versleuteld bestand en druk de openbare sleutel af naar `stdout`:

`age-keygen --output {{pad/naar/bestand}}`

- Versleutel een bestand met een of meer openbare sleutels die als letterlijke waarden worden ingevoerd:

`age --recipient {{openbare_sleutel_1}} --recipient {{openbare_sleutel_2}} {{pad/naar/niet-versleuteld_bestand}} --output {{pad/naar/versleuteld_bestand}}`

- Versleutel een bestand met een of meer openbare sleutels die zijn opgegeven in het bestand van een ontvanger:

`age --recipients-file {{pad/naar/ontvangers_bestand}} {{pad/naar/niet-versleuteld_bestand}} --output {{pad/naar/versleuteld_bestand}}`

- Decodeer een bestand met een wachtwoordzin:

`age --decrypt --output {{pad/naar/gedecodeerd_bestand}} {{pad/naar/versleuteld_bestand}}`

- Ontsleutel een bestand met een privésleutelbestand:

`age --decrypt --identity {{pad/naar/privé_sleutel_bestand}} --output {{pad/naar/gedecodeerd_bestand}} {{pad/naar/versleuteld_bestand}}`
