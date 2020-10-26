# choco pin

> Hefte ein Chocolatey-Paket bei einer bestimmten Version an.
> Angeheftete Pakete werden nicht weiter aktualisiert.
> Mehr Informationen: <https://chocolatey.org/docs/commands-pin>.

- Zeige eine Liste der angehefteten Pakete und ihrer Versionen an:

`choco pin list`

- Hefte ein Paket in der installierten Version an:

`choco pin add --name {{paket}}`

- Hefte ein Paket in einer bestimmten Version an:

`choco pin add --name {{paket}} --version {{version}}`

- Entferne die Anheftung für ein bestimmtes Paket:

`choco pin remove --name {{paket}}`
