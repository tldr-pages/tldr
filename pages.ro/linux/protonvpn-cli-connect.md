# protonvpn-cli connect

> Client oficial pentru a vă conecta la ProtonVPN din linia de comandă.
> Mai multe informaţii: <https://protonvpn.com/support/linux-vpn-setup/>

- Conectați-vă la ProtonVPN interactiv:

`protonvpn-cli connect`

- Conectează-te la ProtonVPN folosind cel mai rapid server disponibil:

`protonvpn-cli connect --fastest`

- Conectați-vă la ProtonVPN utilizând un anumit server cu un anumit protocol:

`protonvpn-cli connect {{server_name}} --protocol {{udp|tcp}}`

- Conectați-vă la ProtonVPN utilizând un server aleator cu un protocol specific:

`protonvpn-cli connect --random --protocol {{udp|tcp}}`

- Conectează-te la ProtonVPN folosind cel mai rapid server TOR-suport:

`protonvpn-cli connect --tor`

- Ajutor pentru afișare:

`protonvpn connect --help`
