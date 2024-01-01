# bower

> Un manager di pacchetti ottimizzato per sviluppo web front-end.
> Un pacchetto può essere una abbreviazione utente/repo GitHub, un endpoint Git, un URL o un pacchetto registrato.
> Maggiori informazioni: <https://bower.io/>.

- Installa le dipendenze di un progetto, listate nel suo file `bower.json`:

`bower install`

- Installa pacchetti nella directory bower_components:

`bower install {{pacchetto}} {{pacchetto}}`

- Disinstalla pacchetti localmente rimuovendolo dalla directory bower_components:

`bower uninstall {{pacchetto}} {{pacchetto}}`

- Elenca pacchetti locali e possibili aggiornamenti:

`bower list`

- Mostra aiuto per un comando di bower:

`bower help {{comando}}`

- Crea un file bower.json per i tuoi pacchetti:

`bower init`

- Installa unoa specifica versione di una dipendenza ed aggiungila al file `bower.json`:

`bower install {{nome_locale}}={{pacchetto}}#{{versione}} --save`
