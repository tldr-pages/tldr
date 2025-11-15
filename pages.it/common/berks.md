# berks

> Gestore di dipendenze per Chef cookbooks.
> Maggiori informazioni: <https://docs.chef.io/berkshelf.html>.

- Installa dipendenze cookbook in una repo locale:

`berks install`

- Aggiorna uno specifico cookbook e le sue dipendenze:

`berks update {{cookbook}}`

- Carica un cookbook sul server di Chef:

`berks upload {{cookbook}}`

- Mostra le dipendenze di un cookbook:

`berks contingent {{cookbook}}`
