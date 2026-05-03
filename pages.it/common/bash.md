# bash

> Bourne-Again SHell, interprete di comandi da linea di comando compatibile con `sh`.
> Vedi anche: `zsh`, `!`.
> Maggiori informazioni: <https://www.gnu.org/software/bash/manual/bash.html#Invoking-Bash>.

- Avvia una sessione shell interattiva:

`bash`

- Avvia una sessione shell interattiva senza caricare i file di configurazione di avvio:

`bash --norc`

- Esegue comandi specifici:

`bash -c "{{echo 'bash è eseguito'}}"`

- Esegue uno script specifico:

`bash {{percorso/allo/script.sh}}`

- Esegue uno script specifico stampando ogni comando prima dell'esecuzione:

`bash -x {{percorso/allo/script.sh}}`

- Esegue uno script specifico e si ferma al primo [e]rrore:

`bash -e {{percorso/allo/script.sh}}`

- Esegue comandi specifici da `stdin`:

`{{echo "echo 'bash è eseguito'"}} | bash`

- Avvia una sessione shell ristretta:

`bash {{[-r|--restricted]}}`
