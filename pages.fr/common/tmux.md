# tmux

> Multiplexeur de terminaux.
> Permet plusieurs sessions avec fenêtres, panneaux, et plus encore.
> Voir aussi : `zellij`, `screen`, `herdr`.
> Plus d'informations : <https://github.com/tmux/tmux>.

- Démarre une nouvelle session :

`tmux`

- Démarre une nouvelle session nommée :

`tmux {{[new|new-session]}} -s {{nom}}`

- Liste les sessions existantes :

`tmux {{[ls|list-sessions]}}`

- S'attache à la session utilisée la plus récemment :

`tmux {{[a|attach]}}`

- Se détache de la session actuelle (dans une session tmux) :

`<Ctrl b><d>`

- Crée une nouvelle fenêtre (dans une session tmux) :

`<Ctrl b><c>`

- Bascule entre les sessions et les fenêtres (dans une session tmux) :

`<Ctrl b><w>`

- Détruit une session nommée :

`tmux kill-session -t {{nom}}`
