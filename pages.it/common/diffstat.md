# diffstat

> Crea un istogramma dall'output del comando `diff`.

- Mostra i cambiamenti in un istogramma:

`diff {{file1}} {{file2}} | diffstat`

- Mostra inserimenti, cancellazioni e modifiche come una tabella:

`diff {{file1}} {{file2}} | diffstat -t`
