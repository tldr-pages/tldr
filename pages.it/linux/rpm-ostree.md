# rpm-ostree

> Un sistema ibrido immagine/pacchetto.
> Gestisce i deployment ostree, i layer di pacchetti, gli overlay del filesystem e la configurazione di boot.
> Maggiori informazioni: <https://coreos.github.io/rpm-ostree/administrator-handbook/>.

- Mostra i deployment rpm-ostree nell’ordine in cui appariranno nel bootloader:

`rpm-ostree status`

- Mostra i pacchetti obsoleti che possono essere aggiornati:

`rpm-ostree upgrade --preview`

- Prepara un nuovo deployment ostree con i pacchetti aggiornati e riavvia in esso:

`rpm-ostree upgrade {{[-r|--reboot]}}`

- Riavvia nel deployment ostree precedente:

`rpm-ostree rollback {{[-r|--reboot]}}`

- Installa un pacchetto in un nuovo deployment ostree e riavvia in esso:

`rpm-ostree install {{package}} {{[-r|--reboot]}}`
