# tmux

> Multiplexador do terminal. Permite várias sessões com janelas, painéis e muito mais.
> Mais informações: <https://github.com/tmux/tmux>.

- Iniciar uma nova sessão:

`tmux`

- Iniciar uma sessão nomeada:

`tmux new-session -s {{name}}`

- Listar sessões existentes:

`tmux ls`

- Entrar na última sessão utilizada:

`tmux attach-session`

- Entrar numa sessão nomeada:

`tmux attach-session -t {{name}}`

- Sair da sessão atual (com o prefixo Ctrl-B):

`Ctrl-B d`

- Eliminar uma sessão nomeada:

`tmux kill-session -t {{name}}`

- Eliminar a sessão atual (com o prefixo Ctrl-B):

`Ctrl-B :kill-session<Enter>`
