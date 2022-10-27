# batch

> Executar comandos num momento mais tarde quando a carga do sistema permitir.
> O serviço atd (ou atrun) deve correr para atuais execuções.
> Mais informações: <https://manned.org/batch>.

- Executar comandos da entrada padrão (premir `Ctrl + D` quando terminado):

`batch`

- Executar um comando da entrada padrão:

`echo "{{./criar_copia_bd.sh}}" | batch`

- Executar comandos de um dado ficheiro:

`batch -f {{caminho/para/ficheiro}}`
