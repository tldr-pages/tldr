# file

> Bepaal bestandstype.
> Meer informatie: <https://manned.org/file>.

- Geef een beschrijving van het type van een bepaald bestand:

`file {{pad/naar/bestand}}`

- Kijk binnen een gezipt bestand en bepaal de bestandstype(s) erin:

`file {{[-z|--uncompress]}} {{pad/naar/bestand.zip}}`

- Sta toe dat `file` werkt met speciale bestanden of apparaatbestanden:

`file {{[-s|--special-files]}} {{pad/naar/bestand}}`

- Stop niet bij de eerste overeenkomende bestandstype; blijf doorgaan totdat het einde van het bestand is bereikt:

`file {{[-k|--keep-going]}} {{pad/naar/bestand}}`

- Bepaal de MIME-coderingstype van een bestand:

`file {{[-i|--mime]}} {{pad/naar/bestand}}`
