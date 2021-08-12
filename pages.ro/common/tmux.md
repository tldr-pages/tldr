# tmux

> Multiplexor terminal. Acesta permite mai multe sesiuni cu ferestre, geamuri și multe altele.
> Mai multe informaţii: <https://github.com/tmux/tmux>

- Începeți o nouă sesiune:

`tmux`

- Începeți o nouă sesiune denumită:

`tmux new -s {{name}}`

- Lista sesiunilor existente:

`tmux ls`

- Atașați la cea mai recentă sesiune utilizată:

`tmux attach`

- Detașați de sesiunea curentă (în cadrul unei sesiuni tmux):

`Ctrl-B d`

- Creați o fereastră nouă (în interiorul unei sesiuni tmux):

`Ctrl-B c`

- Comutarea între sesiuni și ferestre (în interiorul unei sesiuni tmux):

`Ctrl-B w`

- Omoară o sesiune după nume:

`tmux kill-session -t {{name}}`
