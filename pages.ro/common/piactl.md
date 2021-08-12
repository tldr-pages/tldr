# piactl

> Instrumentul de linie de comandă pentru acces privat la Internet, un furnizor VPN comercial.
> Mai multe informaţii: <https://privateinternetaccess.com/helpdesk/kb/articles/pia-desktop-command-line-interface>

- Autentificare la Private Internet Access:

`piactl login {{path/to/login_file}}`

- Conectarea la acces privat la Internet:

`piactl connect`

- Deconectarea de la acces privat la Internet:

`piactl disconnect`

- Activați sau dezactivați daemonul Private Internet Access în fundal:

`piactl background {{enable|disable}}`

- Lista tuturor regiunilor VPN disponibile:

`piactl get regions`

- Afișează regiunea VPN curentă:

`piactl get region`

- Setați regiunea VPN:

`piactl set region {{region}}`

- Deconectați-vă de la accesul privat la Internet:

`piactl logout`
