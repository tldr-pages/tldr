# flatpak mask

> Impedisce aggiornamenti e installazioni automatiche.
> Maggiori informazioni: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-mask>.

- Ignora gli aggiornamenti per un flatpak specifico:

`flatpak mask {{com.example.app}}`

- Annulla l'ignoranza degli aggiornamenti:

`flatpak mask --remove {{com.example.app}}`

- Elenca tutti i pattern attualmente mascherati:

`flatpak mask {{--system|--user}}`
