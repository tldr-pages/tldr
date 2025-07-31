# snoop

> Sniffer de pacotes de rede.
> Equivalente ao `tcpdump`, usado em sistemas SunOS.
> Mais informações: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Capturar pacotes em uma interface de rede específica:

`snoop -d {{e1000g0}}`

- Salvar os pacotes capturados em um arquivo, sem exibir na tela:

`snoop -o {{nome_do_arquivo}}`

- Ler pacotes de um arquivo e exibir detalhes verbosos das camadas de protocolo:

`snoop -V -i {{nome_do_arquivo}}`

- Capturar pacotes vindos de um host e destinados a uma porta específica:

`snoop to port {{porta}} from host {{hostname}}`

- Capturar e exibir um dump hexadecimal de pacotes trocados entre dois IPs:

`snoop -x0 -p4 {{ip_1}} {{ip_2}}`
