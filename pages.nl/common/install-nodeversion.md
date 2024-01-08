# Install-NodeVersion

> Installeer Node.js runtime versies voor `ps-nvm`.
> Onderdeel van `ps-nvm` en kan alleen uitgevoerd worden in PowerShell.
> Meer informatie: <https://github.com/aaronpowell/ps-nvm>.

- Installeer een specifieke Node.js versie:

`Install-NodeVersion {{node_versie}}`

- Installeer meerdere Node.js versies:

`Install-NodeVersion {{node_versie1 , node_versie2 , ...}}`

- Installeer de laatst beschikbare versie van Node.js 20:

`Install-NodeVersion ^20`

- Installeer de x86 (x86 32-bit) / x64 (x86 64-bit) / arm64 (ARM 64-bit) versie van Node.js:

`Install-NodeVersion {{node_versie}} -Architecture {{x86|x64|arm64}}`

- Gebruik een HTTP proxy voor het downloaden van Node.js:

`Install-NodeVersion {{node-version}} -Proxy {{http://example.com}}`
