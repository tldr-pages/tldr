# apt-mark

> Servizio per cambiare lo stato di un pacchetto installato.
> Maggiori informazioni: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Contrassegna un pacchetto come installato automaticamente:

`sudo apt-mark auto {{nome_del_pacchetto}}`

- Mantiene un pacchetto alla sua versione attuale e ne previene l'aggiornamento:

`sudo apt-mark hold {{nome_del_pacchetto}}`

- Consente ad un pacchetto di essere nuovamente aggiornato:

`sudo apt-mark unhold {{nome_del_pacchetto}}`

- Mostra i pacchetti installati manualmente:

`apt-mark showmanual`

- Visualizza i pacchetti mantenuti alla versione attuale che non sono stati aggiornati:

`apt-mark showhold`
