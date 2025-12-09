# Set-NodeVersion

> Stel de standaard Node.js versie in voor `ps-nvm`.
> Onderdeel van `ps-nvm` en kan alleen uitgevoerd worden in PowerShell.
> Meer informatie: <https://github.com/aaronpowell/ps-nvm>.

- Gebruik een specifieke versie van Node.js in de huidige PowerShell sessie:

`Set-NodeVersion {{versie}}`

- Gebruik de laatst geïnstalleerde Node.js versie van 20.x:

`Set-NodeVersion ^20`

- Stel de standaard Node.js versie in voor de huidige gebruiker (geldt alleen voor toekomstige PowerShell sessies):

`Set-NodeVersion {{versie}} -Persist User`

- Stel de standaard Node.js versie in voor alle gebruikers (dient uitgevoerd te worden als Administrator/root en geldt alleen voor toekomstige PowerShell sessies):

`Set-NodeVersion {{versie}} -Persist Machine`
