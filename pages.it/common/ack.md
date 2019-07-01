# ack

> Un tool di ricerca simile a `grep`, ottimizzato per programmatori.
> Maggiori informazioni: <https://beyondgrep.com/documentation/>.

- Trova file contenenti "foo":

`ack {{foo}}`

- Trova file Ruby contenenti una specifica parola chiave:

`ack --ruby {{each_with_object}}`

- Conta il numero di file contenenti "foo":

`ack -ch {{foo}}`

- Mostra i nomi dei file contenenti "foo" insieme al numero di occorrenze del termine all'interno di essi:

`ack -cl {{foo}}`
