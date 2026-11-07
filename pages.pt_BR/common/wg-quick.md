# wg-quick

> Configura rapidamente túneis WireGuard com base em arquivos de configuração.
> Mais informações: <https://manned.org/wg-quick>.

- Ativa um túnel VPN com base em `/etc/wireguard/interface.conf`:

`sudo wg-quick up {{interface}}`

- Desativa e remove um túnel VPN:

`sudo wg-quick down {{interface}}`

- Salva a configuração atual de um túnel em `/etc/wireguard/interface.conf`:

`sudo wg-quick save {{interface}}`

- Exibe a configuração de um túnel removendo as opções específicas do `wg-quick`:

`sudo wg-quick strip {{interface}}`
