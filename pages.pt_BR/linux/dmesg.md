# dmesg

> Escreve as mensagens do kernel na terminal.
> Mais informações: <https://manned.org/dmesg>.

- Exibe as mensagens do kernel:

`sudo dmesg`

- Exibe as mensagens de erro do kernel:

`sudo dmesg --level err`

- Exibe as mensagens do kernel e manter o terminal esperando por novas menagens, semelhante ao `tail -f` (disponível nas versões 3.5.0 e superiores do kernel):

`sudo dmesg -w`

- Exibe a quantidade de memória física disponível no sistema:

`sudo dmesg | grep -i memory`

- Exibe as mensagens do kernel divididas em páginas:

`sudo dmesg | less`

- Exibe as menagens do kernel com data/hora (disponível nas versões 3.5.0 e superiores do kernel):

`sudo dmesg -T`

- Exibe as mensagens do kernel em um formato de fácil leitura (disponível nas versões 3.5.0 e superiores do kernel):

`sudo dmesg -H`

- Exibe as mensagens do kernel utilizando cores (disponível nas versões 3.5.0 e superiores do kernel):

`sudo dmesg -L`
