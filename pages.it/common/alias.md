# alias

> Crea alias - parole sostituite da stringhe di comandi.
> Gli alias scadono con la sessione shell corrente a meno che non siano definiti nel file di configurazione della shell, es. `~/.bashrc` per Bash o `~/.zshrc` per Zsh.
> Vedi anche: `unalias`.
> Maggiori informazioni: <https://www.gnu.org/software/bash/manual/bash.html#index-alias>.

- Elenca tutti gli alias:

`alias`

- Crea un alias generico:

`alias {{parola}}="{{comando}}"`

- Visualizza il comando associato a un dato alias:

`alias {{parola}}`

- Rimuovi un comando alias:

`unalias {{parola}}`

- Rendi `rm` interattivo:

`alias {{rm}}="{{rm --interactive}}"`

- Crea `la` come scorciatoia per `ls --all`:

`alias {{la}}="{{ls --all}}"`
