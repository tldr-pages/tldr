# stty

> Stel opties in voor een terminalapparaatinterface.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- Toon de huidige terminal grootte:

`stty size`

- Toon alle instellingen voor de huidige terminal:

`stty {{[-a|--all]}}`

- Stel het aantal rijen of kolommen in:

`stty {{rows|cols}} {{aantal}}`

- Verkrijg de daadwerkelijke overdrachtssnelheid van een apparaat:

`stty {{[-F|--file]}} {{pad/naar/apparaat_bestand}} speed`

- Reset alle modi naar redelijke waarden voor de huidige terminal:

`stty sane`

- Wissel tussen rauwe en normale modus:

`stty {{raw|cooked}}`

- Zet karakter echoing uit of aan:

`stty {{-echo|echo}}`

- Toon de help:

`stty --help`
