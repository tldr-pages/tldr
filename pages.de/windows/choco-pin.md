# choco pin

> Hefte ein Chocolatey-Paket bei einer bestimmten Version an.
> Angeheftete Pakete werden nicht weiter aktualisiert.
> Weitere Informationen: <https://docs.chocolatey.org/en-us/choco/commands/pin/>.

- Zeige eine Liste der angehefteten Pakete und ihrer Versionen an:

`choco pin list`

- Hefte ein Paket in der installierten Version an:

`choco pin add {{[-n|--name]}} {{paket}}`

- Hefte ein Paket in einer bestimmten Version an:

`choco pin add {{[-n|--name]}} {{paket}} --version {{version}}`

- Entferne die Anheftung für ein bestimmtes Paket:

`choco pin remove {{[-n|--name]}} {{paket}}`
