# aws configure

> Gestisce la configurazione per AWS CLI.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Configura AWS CLI in modo interattivo (crea una nuova configurazione o aggiorna quella predefinita):

`aws configure`

- Configura un profilo nominato per AWS CLI in modo interattivo (crea un nuovo profilo o aggiorna quello esistente):

`aws configure --profile {{nome_profilo}}`

- Visualizza il valore da una variabile di configurazione specifica:

`aws configure get {{nome}}`

- Visualizza il valore per una variabile di configurazione in un profilo specifico:

`aws configure get {{nome}} --profile {{nome_profilo}}`

- Imposta il valore di una variabile di configurazione specifica:

`aws configure set {{nome}} {{valore}}`

- Imposta il valore di una variabile di configurazione in un profilo specifico:

`aws configure set {{nome}} {{valore}} --profile {{nome_profilo}}`

- Elenca le voci di configurazione:

`aws configure list`

- Elenca le voci di configurazione per un profilo specifico:

`aws configure list --profile {{nome_profilo}}`
