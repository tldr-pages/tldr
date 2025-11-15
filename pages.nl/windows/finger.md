# finger

> Geeft informatie over gebruikers op een opgegeven systeem.
> Het externe systeem moet de Finger-service draaien.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/finger>.

- Toon informatie over een specifieke gebruiker:

`finger {{gebruiker}}@{{host}}`

- Toon informatie over alle gebruikers op de opgegeven host:

`finger @{{host}}`

- Toon informatie in een langere indeling:

`finger {{gebruiker}}@{{host}} -l`

- Toon de helpinformatie:

`finger /?`
