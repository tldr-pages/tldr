# batch

> Executar comandos num momento mais tarde quando a carga do sistema permitir.
> O serviço atd (ou atrun) deve correr para atuais execuções.

- Executar comandos do standard input (premir `Ctrl + D` quando terminado):

`batch`

- Executar um comando do standard input:

`echo "{{./make_db_backup.sh}}" | batch`

- Executar comandos de um dado ficheiro:

`batch -f {{caminho/para/ficheiro}}`
