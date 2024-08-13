# if

> Voert voorwaardelijke verwerking uit in batchscripts.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/if>.

- Voer de opgegeven commando's uit als de voorwaarde waar is:

`if {{voorwaarde}} ({{echo Voorwaarde is waar}})`

- Voer de opgegeven commando's uit als de voorwaarde onwaar is:

`if not {{voorwaarde}} ({{echo Voorwaarde is waar}})`

- Voer de eerste opgegeven commando's uit als de voorwaarde waar is, anders voer de tweede opgegeven commando's uit:

`if {{voorwaarde}} ({{echo Voorwaarde is waar}}) else ({{echo Voorwaarde is onwaar}})`

- Controleer of `%errorlevel%` groter dan of gelijk is aan de opgegeven exitcode:

`if errorlevel {{2}} ({{echo Voorwaarde is waar}})`

- Controleer of twee strings gelijk zijn:

`if %{{variabele}}% == {{string}} ({{echo Voorwaarde is waar}})`

- Controleer of twee strings gelijk zijn zonder naar hoofdletters te kijken:

`if /i %{{variabele}}% == {{string}} ({{echo Voorwaarde is waar}})`

- Controleer of een bestand bestaat:

`if exist {{pad\naar\bestand}} ({{echo Voorwaarde is waar}})`
