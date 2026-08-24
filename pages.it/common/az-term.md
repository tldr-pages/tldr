# az term

> Gestisce gli accordi marketplace con marketplaceordering.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/term>.

- Stampa i termini del marketplace:

`az term show --product "{{identificatore_prodotto}}" --plan "{{identificatore_piano}}" --publisher "{{identificatore_editore}}"`

- Accetta i termini del marketplace:

`az term accept --product "{{identificatore_prodotto}}" --plan "{{identificatore_piano}}" --publisher "{{identificatore_editore}}"`
