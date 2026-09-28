# pactrans

> Installeer, verwijder en upgrade ALPM-pakketten.
> Zie ook: `pacinstall`, `pacremove`.
> Meer informatie: <https://github.com/andrewgregory/pacutils/blob/master/doc/pactrans.pod>.

- Installeer een pakket vanuit een repository:

`sudo pactrans --install {{pakket_naam}}`

- Verwijder een pakket:

`sudo pactrans --remove {{pakket_naam}}`

- Upgrade alle geïnstalleerde pakketten:

`sudo pactrans --sysupgrade`

- Installeer een pakketbestand:

`sudo pactrans --file {{pad/naar/pakket.pkg.tar.zst}}`

- Vervang een lokaal geïnstalleerd pakket door een pakket uit een repository:

`sudo pactrans local/{{pakket_om_te_verwijderen}} {{repository_naam}}/{{pakket_om_te_installeren}}`

- Toon wat de transactie zou doen zonder deze uit te voeren:

`pactrans --print-only --install {{pakket_naam}}`
