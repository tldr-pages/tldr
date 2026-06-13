# Remove-NodeVersion

> Deïnstalleer Node.js runtime versies voor `ps-nvm`.
> Onderdeel van `ps-nvm` en kan alleen uitgevoerd worden in PowerShell.
> Meer informatie: <https://github.com/aaronpowell/ps-nvm>.

- Deïnstalleer een gegeven Node.js versie:

`Remove-NodeVersion {{node_versie}}`

- Deïnstalleer meerdere Node.js versies:

`Remove-NodeVersion {{node_versie1 , node_versie2 , ...}}`

- Deïnstalleer alle huidige geïnstalleerde versie van Node.js 20.x:

`Get-NodeVersions -Filter ">=20.0.0 <21.0.0" | Remove-NodeVersion`

- Deïnstalleer alle huidige geïnstalleerde versies van Node.js:

`Get-NodeVersions | Remove-NodeVersion`
