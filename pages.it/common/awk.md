# awk

> Un versatile linguaggio di programmazione per elaborare file.
> Maggiori informazioni: <https://github.com/onetrueawk/awk>.

- Stampa la quinta colonna (field) in un file di linee separate da spazi:

`awk '{print $5}' {{nome_file}}`

- Stampa la seconda colonna delle linee contenenti "qualcosa":

`awk '/{{qualcosa}}/ {print $2}' {{nome_file}}`

- Stampa l'ultima colonna di ogni linea di un file, utilizzando la virgola (invece dello spazio) come separatore di colonne:

`awk -F ',' '{print $NF}' {{nome_file}}`

- Somma i valori nella prima colonna di un file e stampa il totale:

`awk '{s+=$1} END {print s}' {{nome_file}}`

- Somma i valori nella prima colonna e stampali seguiti dal totale:

`awk '{s+=$1; print $1} END {print "--------"; print s}' {{nome_file}}`

- Stampa una liena ogni tre iniziando dalla prima:

`awk 'NR%3==1' {{nome_file}}`
