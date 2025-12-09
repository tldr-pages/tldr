# bash-it

> Una collezione di comandi e script Bash contribuiti dalla community per Bash 3.2+.
> Maggiori informazioni: <https://bash-it.readthedocs.io/en/latest/>.

- Aggiorna Bash-it all’ultima versione stabile/sviluppo:

`bash-it update {{stable|dev}}`

- Ricarica il profilo di Bash (impostare `BASH_IT_AUTOMATIC_RELOAD_AFTER_CONFIG_CHANGE` a un valore non vuoto per un ricaricamento automatico):

`bash-it reload`

- Riavvia Bash:

`bash-it restart`

- Ricarica il profilo di Bash con log di errori e avvisi abilitati:

`bash-it doctor`

- Ricarica il profilo di Bash con log di errori/avvisi/completo abilitati:

`bash-it doctor {{errors|warnings|all}}`

- Cerca alias/plugin/completamenti di Bash-it:

`bash-it search {{alias|plugin|completion}}`

- Cerca alias/plugin/completamenti di Bash-it ed abilita/disabilita tutti gli elementi trovati:

`bash-it search --{{enable|disable}} {{alias|plugin|completion}}`
