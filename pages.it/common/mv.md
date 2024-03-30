# mv

> Sposta o rinomina file e directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/mv>.

- Rinomina un file o una directory quando la destinazione non è una directory esistente:

`mv {{percorso/del/file}} {{percorso/di/destinazione}}`

- Sposta un file o una directory in una directory esistente:

`mv {{percorso/di/origine}} {{percorso/della/directory_esistente}}`

- Sposta più file in una directory esistente, mantenendo i nomi dei file invariati:

`mv {{percorso/di/origine1 percorso/di/origine2 ...}} {{percorso/della/directory_esistente}}`

- Non richiedere conferma prima di sovrascrivere i file esistenti:

`mv -f {{percorso/di/origine}} {{percorso/di/destinazione}}`

- Richiedi conferma prima di sovrascrivere i file esistenti, indipendentemente dalle autorizzazioni dei file:

`mv -i {{percorso/di/origine}} {{percorso/di/destinazione}}`

- Non sovrascrivere i file esistenti nella destinazione:

`mv -n {{percorso/di/origine}} {{percorso/di/destinazione}}`

- Sposta i file in modalità dettagliata, mostrando i file dopo che sono stati spostati:

`mv -v {{percorso/di/origine}} {{percorso/di/destinazione}}`
