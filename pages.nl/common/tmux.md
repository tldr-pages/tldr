# tmux

> Terminal multiplexer.
> Het maakt meerdere sessies met vensters, panes en meer mogelijk.
> Zie ook: `zellij`, `screen`.
> Meer informatie: <https://github.com/tmux/tmux>.

- Start een nieuwe sessie:

`tmux`

- Start een nieuwe benoemde [s]essie:

`tmux {{[new|new-session]}} -s {{naam}}`

- Toon bestaande sessies:

`tmux {{[ls|list-sessions]}}`

- Koppel aan de meest recent gebruikte sessie:

`tmux {{[a|attach]}}`

- Koppel los van de huidige sessie (binnen een tmux sessie):

`<Ctrl b><d>`

- Creëer een nieuwe venster (binnen een tmux sessie):

`<Ctrl b><c>`

- Wissel tussen sessies en vensters (binnen een tmux sessie):

`<Ctrl b><w>`

- Sluit een sessie op basis van de doelnaam ([t]):

`tmux kill-session -t {{naam}}`
