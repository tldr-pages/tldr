# sq

> Een moderne OpenPGP command-line tool.
> Zie ook: `gpg`.
> Meer informatie: <https://sequoia-pgp.gitlab.io/sequoia-sq/man/sq.1.html>.

- Versleutel een bestand met een wachtwoord (symmetrische versleuteling):

`sq encrypt --with-password --without-signature {{pad/naar/bestand}} --output {{pad/naar/bestand.pgp}}`

- Ontsleutel een met wachtwoord beveiligd bestand:

`sq decrypt {{pad/naar/bestand.pgp}} --output {{pad/naar/bestand}}`

- Inspecteer een OpenPGP-bestand om de metadata en structuur te bekijken:

`sq inspect {{pad/naar/bestand.pgp}}`

- Verifieer een bestand met een losstaande handtekening en een certificaatbestand:

`sq verify --signer-file {{pad/naar/ondertekenaar.asc}} --signature-file {{pad/naar/bestand.sig}} {{pad/naar/bestand}}`

- Verifieer een bestand met een ingesloten (leesbare) handtekening en een certificaatbestand:

`sq verify --signer-file {{pad/naar/ondertekenaar.asc}} --cleartext {{pad/naar/bestand}}`

- Genereer je eigen sleutel en sla deze op in de lokale sleutelopslag:

`sq key generate --own-key --name {{naam}} --email {{naam@example.com}}`

- Toon alle geheime sleutels of certificaten die beheerd worden door de lokale sleutelopslag:

`sq {{key|cert}} list`

- Toon de huidige configuratie en opslagpaden:

`sq config inspect paths`
