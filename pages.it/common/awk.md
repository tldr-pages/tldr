# awk

> Un versatile linguaggio di programmazione per elaborare file.
> Nota: Diverse implementazioni di AWK spesso fanno di questo un collegamento simbolico del loro binario.
> Vedi anche: `gawk`.
> Maggiori informazioni: <https://github.com/onetrueawk/awk>.

- Stampa la quinta colonna (field) in un file separato da spazi:

`awk '{print $5}' {{percorso/del/file}}`

- Stampa la seconda colonna delle linee contenenti "{{foo}}" in un file separato da spazi:

`awk '/{{foo}}/ {print $2}' {{percorso/del/file}}`

- Stampa l'ultima colonna di ogni linea di un file, usando la virgola come separatore di campi:

`awk -F ',' '{print $NF}' {{percorso/del/file}}`

- Somma i valori nella prima colonna di un file e stampa il totale:

`awk '{s+=$1} END {print s}' {{percorso/del/file}}`

- Stampa una linea ogni tre iniziando dalla prima:

`awk 'NR%3==1' {{percorso/del/file}}`

- Stampa valori diversi in base a condizioni:

`awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' {{percorso/del/file}}`

- Stampa tutte le linee dove il valore della decima colonna è tra un minimo e un massimo:

`awk '($10 >= {{min_value}} && $10 <= {{max_value}})'`

- Stampa una tabella degli utenti con UID >=1000 con intestazione e output formattato, usando i due punti come separatore (`%-20s` significa: 20 caratteri stringa allineati a sinistra, `%6s` significa: 6 caratteri stringa allineati a destra):

`awk 'BEGIN {FS=":";printf "%-20s %6s %25s\n", "Name", "UID", "Shell"} $4 >= 1000 {printf "%-20s %6d %25s\n", $1, $4, $7}' /etc/passwd`
