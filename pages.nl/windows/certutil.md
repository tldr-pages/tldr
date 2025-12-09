# certutil

> Een tool om certificaatinformatie te beheren en configureren.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/certutil>.

- Dump de configuratie-informatie of bestanden:

`certutil {{bestandsnaam}}`

- Encodeer een bestand in hexadecimaal:

`certutil -encodehex {{pad\naar\invoer_bestand}} {{pad\naar\uitvoer_bestand}}`

- Encodeer een bestand naar Base64:

`certutil -encode {{pad\naar\invoer_bestand}} {{pad\naar\uitvoer_bestand}}`

- Decodeer een Base64-gecodeerd bestand:

`certutil -decode {{pad\naar\invoer_bestand}} {{pad\naar\uitvoer_bestand}}`

- Genereer en toon een cryptografische hash over een bestand:

`certutil -hashfile {{pad\naar\invoer_bestand}} {{md2|md4|md5|sha1|sha256|sha384|sha512}}`
