# autossh

> Esegue, monitora e riavvia connessioni SSH.
> Si riconnette automaticamente per tenere attivi tunnel di port forwarding. Accetta tutte le flag di ssh.
> Maggiori informazioni: <https://www.harding.motd.ca/autossh>.

- Apri una sessione SSH, riavviandola quando una porta monitorata smette di rispondere:

`autossh -M {{porta_monitorata}} "{{comando_ssh}}"`

- Apri una sessione ssh che forwarda una porta locale verso una remota, riavviandola se necessario:

`autossh -M {{porta_monitorata}} -L {{porta_locale}}:localhost:{{porta_remota}} {{utente}}@{{host}}`

- Forka prima di eseguire il comando ssh (si avvia in background) e non aprire una shell remota:

`autossh -f -M {{porta_monitorata}} -N "{{comando_ssh}}"`

- Esegui autossh in background, senza una porta da monitorare, utilizzando i keep-alive di SSH ogni 10 secondi per rilevare una disconnessione:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{comando_ssh}}"`

- Esegui autossh in background, senza una porta da monitorare, senza una shell remota, uscendo se il port forwarding fallisce:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{porta_locale}}:localhost:{{porta_remota}} {{utente}}@{{host}}`

- Esegui autossh in background con output di debug su un file e output verboso di ssh su un altro file:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{file_log}} autossh -f -M {{porta_monitorata}} -v -E {{file_log_ssh}} {{comando_ssh}}`
