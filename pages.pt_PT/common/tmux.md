# tmux

> Multiplexador do terminal. Permite várias sessões com janelas, painéis e muito mais.
> Mais informações: <https://github.com/tmux/tmux>.

- Iniciar uma nova sessão:

`tmux`

- Iniciar uma sessão com nome:

`tmux new-session -s {{nome}}`

- Listar sessões existentes:

`tmux ls`

- Entrar na última sessão utilizada:

`tmux attach-session`

- Entrar numa sessão com nome:

`tmux attach-session -t {{nome}}`

- Sair da sessão atual (com o prefixo Ctrl-B):

`Ctrl-B d`

- Eliminar uma sessão com nome:

`tmux kill-session -t {{nome}}`

- Eliminar a sessão atual (com o prefixo Ctrl-B):

`Ctrl-B :kill-session<Enter>`
