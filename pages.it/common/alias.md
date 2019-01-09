# alias

> Crea alias -- parole che sono sostituite da stringhe di comandi.
> Gli alias vengono persi alla chiusura della shell corrente, a meno che non siano definiti nel file di configurazione della shell (ad esempio `~/.bashrc`).

- Crea un alias:

`alias {{parola}}="{{comando}}"`

- Mostra il comando associato ad un dato alias:

`alias {{parola}}`

- Rimuovi un alias:

`unalias {{parola}}`

- Elenca tutti gli alias correntemente in uso:

`alias -p`

- Rendi il comando rm interattivo:

`alias {{rm}}="{{rm -i}}"`

- Crea un alias `la` come scorciatoia per il comando `ls -a`:

`alias {{la}}="{{ls -a}}"`
