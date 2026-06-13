# diffstat

> Crea un istogramma dall'output del comando `diff`.
> Maggiori informazioni: <https://manned.org/diffstat>.

- Mostra i cambiamenti in un istogramma:

`diff {{file1}} {{file2}} | diffstat`

- Mostra inserimenti, cancellazioni e modifiche come una tabella:

`diff {{file1}} {{file2}} | diffstat -t`
