# conda activate

> Attiva un ambiente conda.
> Vedi anche: `conda deactivate`.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/stable/dev-guide/deep-dives/activation.html>.

- Attiva ambiente esistente `myenv`:

`conda activate myenv`

- Attiva ambiente da percorso personalizzato:

`conda activate {{percorso/del/myenv}}`

- Stack `myenv` sopra ambiente precedente:

`conda activate --stack myenv`

- Avvia `myenv` pulito senza stack:

`conda activate --no-stack myenv`

- Aiuto:

`conda activate {{[-h|--help]}}`
