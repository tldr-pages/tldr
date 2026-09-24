# conda doctor

> Visualizza un report sullo stato di salute del tuo ambiente.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/doctor.html>.

- Visualizza il report per l'ambiente attualmente attivo:

`conda doctor`

- Specifica un ambiente per nome:

`conda doctor {{[-n|--name]}} {{nome_ambiente}}`

- Specifica un ambiente tramite il suo percorso:

`conda doctor {{[-p|--prefix]}} {{percorso/a/ambiente}}`

- Abilita l'output dettagliato (Nota: il flag `-v` può essere ripetuto per aumentare la verbosità):

`conda doctor {{[-v|--verbose]}}`
