# tmux

> Multiplexador do terminal. Permite várias sessões com janelas, painéis e muito mais.
> Mais informações: <https://github.com/tmux/tmux>.

- Inicia uma nova sessão:

`tmux`

- Inicia uma sessão com nome:

`tmux new-session -s {{nome}}`

- Lista sessões existentes:

`tmux ls`

- Entra na última sessão utilizada:

`tmux attach-session`

- Entra numa sessão com nome:

`tmux attach-session -t {{nome}}`

- Sai da sessão atual (com o prefixo Ctrl-B):

`<Ctrl>-B d`

- Elimina uma sessão com nome:

`tmux kill-session -t {{nome}}`

- Elimina a sessão atual (com o prefixo Ctrl-B):

`<Ctrl>-B :kill-session<Enter>`
