# tmux

> Multiplexeur de terminaux. Permet plusieurs sessions avec fenêtres, panneaux, et plus encore.
> Plus d'informations : <https://github.com/tmux/tmux>.

- Démarrer une nouvelle session :

`tmux`

- Démarrer une nouvelle session nommée :

`tmux new -s {{nom}}`

- Lister les sessions existantes :

`tmux ls`

- S'attacher à la session utilisée la plus récemment :

`tmux attach`

- Se détacher de la session actuelle (avec le préfixe Ctrl-B) :

`<Ctrl>-B d`

- Détruire une session nommée :

`tmux kill-session -t {{nom}}`
