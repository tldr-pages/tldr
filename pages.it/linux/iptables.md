# iptables

> Programma che permette di configurare tabelle, catene e regole fornite dal firewall del kernel Linux.
> Maggiori informazioni: <https://manned.org/iptables>.

- Visualizza catene, regole e contatori di pacchetti/byte per la tabella dei filtri:

`sudo iptables {{[-vnL --line-numbers|--verbose --numeric --list --line-numbers]}}`

- Imposta regola ad una catena:

`sudo iptables {{[-P|--policy]}} {{catena}} {{regola}}`

- Appendi regola ad una catena di policy per IP:

`sudo iptables {{[-A|--append]}} {{catena}} {{[-s|--source]}} {{ip}} {{[-j|--jump]}} {{regola}}`

- Appendi regola ad una catena di policy per IP considerando protocollo e porta:

`sudo iptables {{[-A|--append]}} {{catena}} {{[-s|--source]}} {{ip}} {{[-p|--protocol]}} {{protocollo}} --dport {{porta}} {{[-j|--jump]}} {{regola}}`

- Cancella regola da una catena:

`sudo iptables {{[-D|--delete]}} {{catena}} {{numero_di_linea_della_regola}}`

- Salva la configurazione di ip tables di una specifica tabella in un file:

`sudo iptables-save {{[-t|--table]}} {{nome tabella}} > {{percorso/del/file_iptables}}`

- Ripristina la configurazione di iptables da un file:

`sudo iptables-restore < {{percorso/del/file_iptables}}`
