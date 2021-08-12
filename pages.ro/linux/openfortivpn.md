# openfortivpn

> Un client VPN, pentru solutia PPP+SSL VPN proprietara Fortinet.
> Mai multe informaţii: <https://github.com/adrienverge/openfortivpn>

- Conectați-vă la un VPN cu un nume de utilizator și o parolă:

`openfortivpn --username={{username}} --password={{password}}`

- Conectați-vă la un VPN utilizând un fișier de configurare specific (implicit la `/etc/openfortivpn/config`):

`sudo openfortivpn --config={{path/to/config}}`

- Conectați-vă la un VPN specificând gazda și portul:

`openfortivpn {{host}}:{{port}}`

- Încredere într-un gateway dat prin transmiterea sumei sha256 a certificatului său:

`openfortivpn --trusted-cert={{sha256_sum}}`
