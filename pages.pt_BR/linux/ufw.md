# ufw

> Firewall Descomplicado.
> Frontend para `iptables` com o objetivo de facilitar a configuração de um firewall.
> Mais informações: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Habilitar ufw:

`ufw enable`

- Desabilitar ufw:

`ufw disable`

- Mostrar regras ufw, juntamente com seus números:

`ufw status numbered`

- Permitir tráfego de entrada na porta 5432 nesse host com um que identifique o serviço:

`ufw allow {{5432}} comment "{{Service}}"`

- Permitir apenas tráfego TCP de 192.168.0.4 pra qualquer endereço deste host, na porta 22 :

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{any}} port {{22}}`

- Negar tráfego na porta 80 desse host :

`ufw deny {{80}}`

- Negar todo o tráfego UDP para portas no intervalo 8412:8500:

`ufw deny proto {{udp}} from {{any}} to {{any}} port {{8412:8500}}`

- Deletar uma regra particular. O número da regra pode ser recuperado com o `ufw status numbered` comando:

`ufw delete {{rule_number}}`
