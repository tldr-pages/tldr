# accelerate

> Libreria che permette di eseguire lo stesso codice PyTorch su qualsiasi configurazione distribuita.
> Maggiori informazioni: <https://huggingface.co/docs/accelerate/index>.

- Stampa le informazioni sull'ambiente:

`accelerate env`

- Crea interattivamente un file di configurazione:

`accelerate config`

- Stampa il costo stimato in memoria GPU per eseguire un modello Hugging Face con diversi tipi di dati:

`accelerate estimate-memory {{nome/modello}}`

- Testa un file di configurazione Accelerate:

`accelerate test --config_file {{percorso/del/config.yaml}}`

- Esegui un modello su CPU con Accelerate:

`accelerate launch {{percorso/del/script.py}} {{--cpu}}`

- Esegui un modello su multi-GPU con Accelerate, con 2 macchine:

`accelerate launch {{percorso/del/script.py}} --multi_gpu --num_machines 2`
