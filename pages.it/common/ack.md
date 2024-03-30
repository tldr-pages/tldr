# ack

> Un tool di ricerca simile a `grep`, ottimizzato per programmatori.
> Vedi anche: `rg`, che è molto più veloce.
> Maggiori informazioni: <https://beyondgrep.com/documentation>.

- Cerca ricorsivamente file contenenti una stringa o un'espressione regolare nella directory corrente:

`ack "{{pattern_di_ricerca}}"`

- Cerca un pattern in modalità case-insensitive:

`ack --ignore-case "{{pattern_di_ricerca}}"`

- Cerca righe di testo contenenti un pattern, mostrando solo il testo corrispondente e non il resto della riga:

`ack -o "{{pattern_di_ricerca}}"`

- Limita la ricerca ai file di un tipo specifico:

`ack --type={{ruby}} "{{pattern_di_ricerca}}"`

- Non cercare nei file di un tipo specifico:

`ack --type=no{{ruby}} "{{pattern_di_ricerca}}"`

- Conta il numero totale di corrispondenze trovate:

`ack --count --no-filename "{{pattern_di_ricerca}}"`

- Mostra i nomi dei file e il numero di corrispondenze per ogni singolo file:

`ack --count --files-with-matches "{{pattern_di_ricerca}}"`

- Mostra la lista di tutti i valori che possono essere usati con `--type`:

`ack --help-types`
