# dnf versionlock

> Protegge i pacchetti da aggiornamenti a versioni più recenti.
> Non predefinito in `dnf` ma supportato tramite `dnf-plugins-core`.
> Maggiori informazioni: <https://dnf-plugins-core.readthedocs.io/en/latest/versionlock.html>.

- Elenca le voci correnti di versionlock:

`dnf versionlock`

- Aggiunge un versionlock per tutti i pacchetti disponibili che corrispondono alla specifica:

`dnf versionlock add {{pacchetto}}`

- Aggiunge un'esclusione (nel versionlock) per i pacchetti disponibili che corrispondono alla specifica:

`dnf versionlock exclude {{pacchetto}}`

- Rimuove le voci corrispondenti di versionlock:

`dnf versionlock delete {{pacchetto}}`

- Rimuove tutte le voci di versionlock:

`dnf versionlock clear`
