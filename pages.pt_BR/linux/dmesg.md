# dmesg

> Escreve as mensagens do kernel na terminal.
> Mais informações: <https://manned.org/dmesg>.

- Exibe as mensagens do kernel:

`dmesg`

- Exibe as mensagens de erro do kernel:

`dmesg --level err`

- Exibe as mensagens do kernel e manter o terminal esperando por novas menagens, semelhante ao `tail -f` (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -w`

- Exibe a quantidade de memória física disponível no sistema:

`dmesg | grep -i memory`

- Exibe as mensagens do kernel divididas em páginas:

`dmesg | less`

- Exibe as menagens do kernel com data/hora (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -T`

- Exibe as mensagens do kernel em um formato de fácil leitura (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -H`

- Exibe as mensagens do kernel utilizando cores (disponível nas versões 3.5.0 e superiores do kernel):

`dmesg -L`
