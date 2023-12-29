# emacs

> O editor extensível, personalizável, autodocumentável, com exibição em tempo real.
> Veja também `emacsclient`.
> Mais informações: <https://www.gnu.org/software/emacs>.

- Inicia o Emacs e abra um arquivo:

`emacs {{caminho/para/arquivo}}`

- Abre um arquivo em uma linha especificada:

`emacs +{{numero_linha}} {{caminho/para/arquivo}}`

- Inicia o Emacs em modo console (sem uma janela X):

`emacs --no-window-system`

- Inicia um servidor Emacs em segundo plano (acessível através do `emacsclient`):

`emacs --daemon`

- Para um servidor Emacs em funcionamento e todas as suas instâncias, pedindo confirmação em arquivos não salvos:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Salva um arquivo em Emacs:

`<Ctrl> + X, <Ctrl> + S`

- Deixa o Emacs:

`<Ctrl> + X, <Ctrl> + C`
