# iptables

> Programma che permette di configurare tabelle, catene e regole fornite dal firewall del kernel Linux.
> Maggiori informazioni: <https://www.netfilter.org/projects/iptables/>.

- Visualizza catene, regole e contatori di pacchetti/byte per la tabella dei filtri:

`sudo iptables -vnL`

- Imposta regola ad una catena:

`sudo iptables -P {{catena}} {{regola}}`

- Appendi regola ad una catena di policy per IP:

`sudo iptables -A {{catena}} -s {{ip}} -j {{regola}}`

- Appendi regola ad una catena di policy per IP considerando protocollo e porta:

`sudo iptables -A {{catena}} -s {{ip}} -p {{protocollo}} --dport {{porta}} -j {{regola}}`

- Cancella regola da una catena:

`sudo iptables -D {{catena}} {{numero_di_linea_della_regola}}`

- Salva la configurazione di ip tables di una specifica tabella in un file:

`sudo iptables-save -t {{nome tabella}} > {{percorso/al/file_iptables}}`

- Ripristina la configurazione di iptables da un file:

`sudo iptables-restore < {{percorso/al/file_iptables}}`
