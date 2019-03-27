# dmesg

> Escreve as mensagens do kernel na saída padrão.

- Exibe as mensagens do kernel:

`dmesg`

- Exibe as mensagens de erro do kernel:

`dmesg --level err`

- Exibe as mensagens do kernel e mantém o terminal esperando por novas menagens, semelhante ao `tail -f` (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -w`

- Exibe quanta memória física está disponível no sistema:

`dmesg | grep -i memory`

- Exibe as mensagens do kernel divididas em páginas:

`dmesg | less`

- Exibe as menagens do kernel com data/hora (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -T`

- Exibe as mensagens do kernel em um formato de fácil leitura (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -H`

- Torna a saída colorida (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -L`
