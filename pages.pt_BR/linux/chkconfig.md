# chkconfig

> Gerencia o runlevel dos serviços no CentOS 6.
> Mais informações: <https://manned.org/chkconfig>.

- Exibir os serviços com os respectivos runlevels:

`chkconfig --list`

- Exibir o runlevel de um serviço:

`chkconfig --list {{ntpd}}`

- Habilitar o início de um serviço durante o processo de boot:

`chkconfig {{sshd}} on`

- Habilitar o início do serviço durante o processo de boot para os runlevels 2, 3, 4 e 5:

`chkconfig --level {{2345}} {{sshd}} on`

- Desabilitar a inicialização de um determinado serviço durante o processo de boot:

`chkconfig {{ntpd}} off`

- Desabilitar a inicialização de um determinado serviço durante o processo de boot para o runlevel 3:

`chkconfig --level {{3}} {{ntpd}} off`
