# zerotier-idtool

> Maak en manipuleer ZeroTier-identiteiten.
> Zie ook: `zerotier-cli`, `zerotier-one`.
> Meer informatie: <https://github.com/zerotier/ZeroTierOne/blob/dev/doc/zerotier-idtool.1.md>.

- Genereer een nieuwe ZeroTier-identiteit en print het geheime deel naar `stdout`:

`zerotier-idtool generate`

- Genereer een nieuwe ZeroTier-identiteit en sla het geheime en publieke deel op in bestanden:

`zerotier-idtool generate {{pad/naar/identiteit.secret}} {{pad/naar/identiteit.public}}`

- Genereer een nieuwe ZeroTier-identiteit met een specifiek hexadecimaal vanity-voorvoegsel (kan lang duren):

`zerotier-idtool generate {{pad/naar/identiteit.secret}} {{pad/naar/identiteit.public}} {{vanity_voorvoegsel}}`

- Extraheer het publieke deel uit een geheime identiteit:

`zerotier-idtool getpublic {{pad/naar/identiteit.secret}}`

- Onderteken een bestand met een geheime identiteit:

`zerotier-idtool sign {{pad/naar/identiteit.secret}} {{pad/naar/bestand}}`

- Verifieer een ondertekend bestand met een publieke identiteit en een hexadecimale handtekening:

`zerotier-idtool verify {{pad/naar/identiteit.public}} {{pad/naar/bestand}} {{handtekening_hex}}`

- Valideer lokaal de sleutel en proof-of-work van een identiteit:

`zerotier-idtool validate {{pad/naar/identiteit.public}}`

- Toon de help:

`zerotier-idtool help`
