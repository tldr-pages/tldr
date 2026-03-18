# conda activate

> Attiva un ambiente conda.  
> Vedi anche: `conda deactivate`.  
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/stable/dev-guide/deep-dives/activation.html>.

- Attiva un ambiente esistente chiamato `myenv`:

`conda activate myenv`

- Attiva un ambiente esistente situato in un percorso personalizzato:

`conda activate {{percorso/a/myenv}}`

- Sovrapponi l'ambiente `myenv` a un ambiente precedente rendendo accessibili librerie/comandi/variabili di entrambi:

`conda activate --stack myenv`

- Avvia un ambiente pulito `myenv` senza sovrapporlo, rendendo inaccessibili librerie/comandi/variabili dell'ambiente precedente:

`conda activate --no-stack myenv`

- Mostra l'aiuto:

`conda activate {{[-h|--help]}}`
