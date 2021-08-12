# protonvpn-cli

> Client oficial pentru serviciul ProtonVPN din linia de comandă.
> Mai multe informaţii: <https://github.com/ProtonVPN/linux-cli>

- Conectați-vă la contul ProtonVPN:

`protonvpn-cli login {{username}}`

- Porniți un comutator de oprire la conectarea la ProtonVPN:

`protonvpn-cli killswitch --on`

- Conectați-vă la ProtonVPN interactiv:

`protonvpn-cli connect`

- Starea conexiunii afiseaza:

`protonvpn-cli status`

- Bloc malware folosind ProtonVPN NetShield:

`protonvpn-cli netshield --malware`

- Deconectați de la ProtonVPN:

`protonvpn-cli disconnect`

- Afișează configurația curentă ProtonVPN:

`protonvpn-cli config --list`

- Afișează ajutor pentru o subcomandă:

`protonvpn-cli {{subcommand}} --help`
