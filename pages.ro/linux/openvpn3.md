# openvpn3

> client OpenVPN 3 Linux.
> Mai multe informaţii: <https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux>

- Începeți o nouă sesiune VPN:

`openvpn3 session-start --config {{path/to/config.conf}}`

- Lista sesiunilor stabilite:

`openvpn3 sessions-list`

- Deconectați sesiunea stabilită în prezent a început cu configurația dată:

`openvpn3 session-manage --config {{path/to/config.conf}} --disconnect`

- Import configuraţie VPN:

`openvpn3 config-import --config {{path/to/config.conf}}`

- Lista configurațiilor importate:

`openvpn3 configs-list`
