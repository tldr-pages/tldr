# batch

> Executar comandos num momento mais tarde quando a carga do sistema permitir.
> O serviço atd (ou atrun) deve correr para atuais execuções.
> Mais informações: <https://manned.org/batch>.

- Executa comandos da entrada padrão (premir `Ctrl + D` quando terminado):

`batch`

- Executa um comando da entrada padrão:

`echo "{{./criar_copia_bd.sh}}" | batch`

- Executa comandos de um dado ficheiro:

`batch -f {{caminho/para/ficheiro}}`
