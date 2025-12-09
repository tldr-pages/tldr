# choco install

> Installeer een of meerdere pakketen met Chocolatey.
> Meer informatie: <https://chocolatey.org/docs/commands-install>.

- Installeer een of meerdere spatie-gescheiden pakketten:

`choco install {{pakket1 pakket2 ...}}`

- Installeer pakketten van een aangepast configuratiebestand:

`choco install {{pad\naar\pakketten_bestand.config}}`

- Installeer een specifiek `nuspec` of `nupkg` bestand:

`choco install {{pad\naar\bestand}}`

- Installeer een specifieke versie van een pakket:

`choco install {{pakket}} --version {{versie}}`

- Sta het toe om meerdere versies van een pakket te installeren:

`choco install {{pakket}} --allow-multiple`

- Bevestig alle prompts automatisch:

`choco install {{pakket}} --yes`

- Specificieer een aangepaste bron om pakketten van te ontvangen:

`choco install {{pakket}} --source {{source_url|alias}}`

- Geef een gebruikersnaam en wachtwoord voor authenticatie op:

`choco install {{pakket}} --user {{gebruikersnaam}} --password {{wachtwoord}}`
