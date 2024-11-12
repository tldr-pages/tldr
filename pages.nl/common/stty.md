# stty

> Stel opties in voor een terminalapparaatinterface.
> Meer informatie: <https://www.gnu.org/software/coreutils/stty>.

- Toon alle instellingen voor de huidige terminal:

`stty --all`

- Stel het aantal rijen of kolommen in:

`stty {{rows|cols}} {{aantal}}`

- Verkrijg de daadwerkelijke overdrachtssnelheid van een apparaat:

`stty --file {{pad/naar/apparaat_bestand}} speed`

- Reset alle modi naar redelijke waarden voor de huidige terminal:

`stty sane`
