# dnf builddep

> Installa le dipendenze per compilare un dato pacchetto.
> Non predefinito in `dnf` ma supportato tramite `dnf-plugins-core`.
> Vedi anche: `dnf`.
> Maggiori informazioni: <https://dnf-plugins-core.readthedocs.io/en/latest/builddep.html>.

- Installa le dipendenze per un dato pacchetto:

`dnf builddep {{path/to/specification.spec}}`

- Installa le dipendenze per un dato pacchetto ma ignora quelle non disponibili:

`dnf builddep --skip-unavailable {{path/to/specification.spec}}`

- Definisce il macro RPM con una data espressione:

`dnf builddep {{[-D|--define]}} '{{expression}}'`

- Definisce un argomento per un percorso file `.spec`:

`dnf builddep --spec {{argument}}`

- Definisce un argomento per un percorso file `.rpm`:

`dnf builddep --srpm {{argument}}`

- Mostra aiuto:

`dnf builddep --help-cmd`
