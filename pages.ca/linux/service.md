# service

> Gestiona els serveis mitjançant l'execució de scripts init.
> S'ha d'ometre la ruta completa del script (s'assumeix `/etc/init.d`).

- Llista el nom i l'estat de tots els serveis:

`service --status-all`

- Inicia/Para/Reinicia/Recarrega servei (_start_/_stop_ hauria d'estar sempre disponible):

`service {{nom_del_servei}} {{start|stop|restart|reload}}`

- Fa un reinici complet (executa el script dues vegades amb _start_ i _stop_):

`service {{nom_del_servei}} --full-restart`

- Mostra l'estat actual d'un servei:

`service {{nom_del_servei}} status`
