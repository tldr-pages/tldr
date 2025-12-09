# Get-NodeVersions

> Toon geïnstalleerde en beschikbare Node.js versies voor `ps-nvm`.
> Onderdeel van `ps-nvm` en kan alleen uitgevoerd worden in PowerShell.
> Meer informatie: <https://github.com/aaronpowell/ps-nvm>.

- Toon alle geïnstalleerde Node.js versies:

`Get-NodeVersions`

- Toon alle beschikbare Node.js versies:

`Get-NodeVersions -Remote`

- Toon alle beschikbare Node.js 20.x versies:

`Get-NodeVersions -Remote -Filter ">=20.0.0 <21.0.0"`
