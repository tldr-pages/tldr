# iptables
> Programma che permette di configurare tabelle, catene e regole fornite dal firewall del kernel Linux.
> Maggiori informazioni: <https://www.netfilter.org/projects/iptables/>.

- Visualizza catene, regole e contatori di pacchetti/byte per la tabella dei filtri:

`sudo iptables -vnL`

- Imposta regola ad una catena

`sudo iptables -P {{chain}} {{rule}}`

- Appendi regola ad una catena di policy per IP

`sudo iptables -A {{chain}} -s {{ip}} -j {{rule}}`

- Appeni regola ad una catena di policy per IP considerando protocollo e porta

`sudo iptables -A {{chain}} -s {{ip}} -p {{protocol}} --dport {{port}} -j {{rule}}`

- Cancella regola da una catena

`sudo iptables -D {{chain}} {{rule_line_number}}`

- Salva la configurazione di ip tables di una specifica tabella in un file

`sudo iptables-save -t {{tablename}} > {{path/to/iptables_file}}`

- Ripristina la configurazione di iptables da un file

`sudo iptables-restore < {{path/to/iptables_file}}`
