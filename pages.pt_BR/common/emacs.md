# emacs

> O editor extensível, personalizável, autodocumentável, com exibição em tempo real.
> Veja também `emacsclient`.
> Mais informações: <https://www.gnu.org/software/emacs>.

- Inicia o Emacs e abra um arquivo:

`emacs {{caminho/para/arquivo}}`

- Abre um arquivo em uma linha especificada:

`emacs +{{numero_linha}} {{caminho/para/arquivo}}`

- Inicia um arquivo Emacs Lisp como script:

`emacs --script {{caminho/para/arquivo.el}}`

- Inicia o Emacs em modo console (sem uma janela X):

`emacs {{[-nw|--no-window-system]}}`

- Inicia um servidor Emacs em segundo plano (acessível através do `emacsclient`):

`emacs --daemon`

- Para um servidor Emacs em funcionamento e todas as suas instâncias, pedindo confirmação em arquivos não salvos:

`emacsclient --eval '(save-buffers-kill-emacs)'`

- Salva um arquivo em Emacs:

`<Ctrl x><Ctrl s>`

- Sai do Emacs:

`<Ctrl x><Ctrl c>`
