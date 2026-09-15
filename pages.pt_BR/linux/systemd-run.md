# systemd-run

> Executa programas em unidades temporárias de scope, service, ou unidades ativadas por path, socket ou timer.
> Mais informações: <https://www.freedesktop.org/software/systemd/man/latest/systemd-run.html>.

- Inicia um serviço temporário:

`sudo systemd-run {{comando}} {{argumento1 argumento2 ...}}`

- Inicia um serviço temporário sob o gerenciador de serviços do usuário atual (sem privilégios):

`systemd-run --user {{comando}} {{argumento1 argumento2 ...}}`

- Inicia um serviço temporário com nome e descrição da unidade customizados:

`sudo systemd-run {{[-u|--unit]}} {{nome}} --description {{texto}} {{comando}} {{argumento1 argumento2 ...}}`

- Inicia um serviço temporário que não será limpo após terminar com uma variável de ambiente customizada:

`sudo systemd-run {{[-r|--remain-after-exit]}} --set-env={{nome}}={{valor}} {{comando}} {{argumento1 argumento2 ...}}`

- Inicia um timer temporário que executa periodicamente seu serviço temporário (veja `man systemd.time` para o formato de eventos do calendário):

`sudo systemd-run --on-calendar={{evento_do_calendário}} {{comando}} {{argumento1 argumento2 ...}}`

- Compartilha o terminal com o programa (permitindo entrada/saída interativas) e garante que os detalhes da execução permaneçam após a saída:

`systemd-run {{[-r|--remain-after-exit]}} --pty {{comando}}`

- Define propriedades (ex.: CPUQuota, MemoryMax) do processo e aguarda sua finalização:

`systemd-run {{[-p|--property]}} MemoryMax={{memória_em_bytes}} {{[-p|--property]}} CPUQuota={{porcentagem_de_cpu}}% --wait {{comando}}`

- Usa o programa em uma pipeline do shell:

`{{comando1}} | systemd-run {{[-P|--pipe]}} {{comando2}} | {{comando3}}`
