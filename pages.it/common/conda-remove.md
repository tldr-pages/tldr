# conda remove

> Rimuovi pacchetti da ambiente.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/remove.html>.

- Rimuovi pacchetto ambiente attivo:

`conda remove scipy`

- Pacchetti da ambiente specifico:

`conda remove {{[-n|--name]}} {{ambiente}} {{pacchetto1 pacchetto2 ...}}`

- Elimina ambiente:

`conda remove {{[-n|--name]}} {{ambiente}} --all`

- Rimuovi pacchetti (mantieni ambiente):

`conda remove {{[-n|--name]}} {{ambiente}} --all --no-builds`
