# openvpn3

> Клиент OpenVPN 3 для Linux.
> Больше информации: <https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux>.

- Запустить новую VPN-сессию:

`openvpn3 session-start {{[-c|--config]}} {{путь/к/конфигурации.conf}}`

- Показать список установленных сессий:

`openvpn3 sessions-list`

- Отключить текущую сессию, запущенную с указанной конфигурацией:

`openvpn3 session-manage {{[-c|--config]}} {{путь/к/конфигурации.conf}} {{[-D|--disconnect]}}`

- Импортировать конфигурацию VPN:

`openvpn3 config-import {{[-c|--config]}} {{путь/к/конфигурации.conf}}`

- Показать список импортированных конфигураций:

`openvpn3 configs-list`
