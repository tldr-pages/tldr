# dnf config-manager

> Gestisce le opzioni di configurazione e i repository DNF su sistemi basati su Fedora.
> Non predefinito in `dnf` ma supportato tramite `dnf-plugins-core`.
> Vedi anche: `dnf`.
> Maggiori informazioni: <https://dnf-plugins-core.readthedocs.io/en/latest/config_manager.html>.

- Aggiunge (e abilita) un repository da un URL:

`dnf config-manager --add-repo={{repository_url}}`

- Stampa i valori di configurazione correnti:

`dnf config-manager --dump`

- Abilita un repository specifico:

`dnf config-manager {{[--enable|--set-enabled]}} {{repository_id}}`

- Disabilita i repository specificati:

`dnf config-manager {{[--disable|--set-disabled]}} {{repository_id1 repository_id2 ...}}`

- Imposta un'opzione di configurazione per un repository:

`dnf config-manager --setopt={{option}}={{value}}`

- Mostra aiuto:

`dnf config-manager --help-cmd`
