# herdr

> Terminal workspace manager voor AI coding agents.
> Opmerking: de indeling is Sessie > Workspace > Tab > Pane.
> Zie ook: `tmux`, `zellij`, `screen`.
> Meer informatie: <https://herdr.dev/docs/cli-reference/>.

- Start een nieuwe sessie of maak verbinding met de standaardsessie:

`herdr`

- Toon de lokale client- en serverstatus:

`herdr status`

- Genereer de standaardconfiguratie en print deze naar `stdout`:

`herdr --default-config`

- Ontkoppel van de huidige sessie (binnen een herdr-sessie):

`<Ctrl b><q>`

- Toon de sneltoetsen (binnen een herdr-sessie):

`<Ctrl b><?>`

- Maak een nieuwe workspace aan (binnen een herdr-sessie):

`<Ctrl b><Shift n>`

- Maak een nieuwe tab aan (binnen een herdr-sessie):

`<Ctrl b><c>`

- Split het paneel verticaal/horizontaal (binnen een herdr-sessie):

`<Ctrl b>{{<v>|<->}}`
