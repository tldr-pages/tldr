# conda package

> Crea pacchetti conda a basso livello.  
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/stable/commands/package.html>.

- Ottieni il pacchetto conda da un file:

`conda package {{[-w|--which]}} {{percorso/al/file}}`

- Rimuovi tutti i file non tracciati:

`conda package {{[-r|--reset]}}`

- Mostra tutti i file non tracciati:

`conda package {{[-u|--untracked]}}`

- Specifica il nome del pacchetto in fase di creazione:

`conda package --pkg-name {{nome}}`

- Specifica la versione del pacchetto in fase di creazione:

`conda package --pkg-version {{versione}}`

- Specifica il numero di build del pacchetto in fase di creazione:

`conda package --pkg-build {{numero_build}}`
