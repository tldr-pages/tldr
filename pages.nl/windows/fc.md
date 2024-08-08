# fc

> Vergelijk de verschillen tussen twee bestanden of sets van bestanden.
> Gebruik wildcards (*) om sets van bestanden te vergelijken.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/fc>.

- Vergelijk 2 opgegeven bestanden:

`fc {{pad\naar\bestand1}} {{pad\naar\bestand2}}`

- Voer een hoofdletterongevoelige vergelijking uit:

`fc /c {{pad\naar\bestand1}} {{pad\naar\bestand2}}`

- Vergelijk bestanden als Unicode-tekst:

`fc /u {{pad\naar\bestand1}} {{pad\naar\bestand2}}`

- Vergelijk bestanden als ASCII-tekst:

`fc /l {{pad\naar\bestand1}} {{pad\naar\bestand2}}`

- Vergelijk bestanden als binair:

`fc /b {{pad\naar\bestand1}} {{pad\naar\bestand2}}`

- Schakel tab-naar-spatie uitbreiding uit:

`fc /t {{pad\naar\bestand1}} {{pad\naar\bestand2}}`

- Comprimeer witruimte (tabs en spaties) voor vergelijkingen:

`fc /w {{pad\naar\bestand1}} {{pad\naar\bestand2}}`
