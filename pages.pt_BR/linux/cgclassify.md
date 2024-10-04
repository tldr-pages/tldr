# cgclassify

> Move tarefas em execução para `cgroups`.
> Mais informações: <https://manned.org/cgclassify>.

- Move o processo com um PID específico para o grupo de controle estudante na hierarquia CPU:

`cgclassify -g {{cpu:estudante}} {{1234}}`

- Move o processo com um PID específico para grupos de controle baseados no arquivo de configuração `/etc/cgrules.conf`:

`cgclassify {{1234}}`

- Move o processo com um PID específico para o grupo de controle estudante na hierarquia CPU. Note: o daemon do serviço `cgred` não altera `cgroups` do PID específico e seus filhos (com base em `/etc/cgrules.conf`):

`cgclassify --sticky -g {{cpu:/estudante}} {{1234}}`
