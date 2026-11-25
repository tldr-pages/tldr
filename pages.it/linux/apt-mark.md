# apt-mark

> Servizio per cambiare lo stato di un pacchetto installato.
> Maggiori informazioni: <https://manned.org/apt-mark>.

- Contrassegna un pacchetto come installato automaticamente:

`sudo apt-mark auto {{pacchetto}}`

- Mantiene un pacchetto alla sua versione attuale e ne previene l'aggiornamento:

`sudo apt-mark hold {{pacchetto}}`

- Consente ad un pacchetto di essere nuovamente aggiornato:

`sudo apt-mark unhold {{pacchetto}}`

- Mostra i pacchetti installati manualmente:

`apt-mark showmanual`

- Visualizza i pacchetti mantenuti alla versione attuale che non sono stati aggiornati:

`apt-mark showhold`
