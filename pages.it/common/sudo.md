# sudo

> Esegue un singolo comando come superuser o come un altro utente.
> Maggiori informazioni: <https://www.sudo.ws/sudo.html>.

- Esegui un comando come superuser:

`sudo {{less /var/log/syslog}}`

- Modifica un file come superuser con il tuo editor di default:

`sudo -e {{/etc/fstab}}`

- Esegui un comando come un altro utente e/o gruppo:

`sudo -u {{utente}} -g {{gruppo}} {{id -a}}`

- Ripeti l'ultimo comando prefissandolo con "sudo" (funziona solo in Bash, Zsh, ecc):

`sudo !!`

- Fai partire la shell di default con i privilegi da superuser:

`sudo -i`
