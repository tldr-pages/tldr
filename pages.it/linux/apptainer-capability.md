# apptainer capability

> Gestisce le capacità Linux per utenti e gruppi.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_capability.html>.

- Mostra tutte le capacità Linux disponibili:

`apptainer capability avail`

- Mostra le descrizioni per capacità specifiche:

`apptainer capability avail {{cap_chown,cap_net_raw,...}}`

- Elenca le capacità per tutti gli utenti e gruppi:

`apptainer capability list`

- Elenca le capacità per un utente o gruppo specifico:

`apptainer capability list {{nome_utente|nome_gruppo}}`

- Aggiunge capacità a un utente:

`sudo apptainer capability add {{[-u|--user]}} {{nome_utente}} {{cap_net_raw,cap_chown,...}}`

- Aggiunge capacità a un gruppo:

`sudo apptainer capability add {{[-g|--group]}} {{nome_gruppo}} {{cap_net_raw,cap_chown,...}}`

- Rimuove capacità da un utente:

`sudo apptainer capability drop {{[-u|--user]}} {{nome_utente}} {{cap_net_raw,cap_chown,...}}`

- Rimuove tutte le capacità da un utente:

`sudo apptainer capability drop {{[-u|--user]}} {{nome_utente}} all`
