# awk

> Un limbaj versatil de programare pentru lucrul la fișiere.
> Mai multe informaţii: <https://github.com/onetrueawk/awk>

- Imprimați a cincea coloană (alias câmp) într-un fișier separat de spațiu:

`awk '{print $5}' {{filename}}`

- Imprimați a doua coloană a liniilor care conțin „foo” într-un fișier separat de spațiu:

`awk '/{{foo}}/ {print $2}' {{filename}}`

- Imprimați ultima coloană a fiecărei linii dintr-un fișier, utilizând o virgulă (în loc de spațiu) ca separator de câmp:

`awk -F ',' '{print $NF}' {{filename}}`

- Însumați valorile din prima coloană a unui fișier și imprimați totalul:

`awk '{s+=$1} END {print s}' {{filename}}`

- Tipăriți fiecare a treia linie începând de la prima linie:

`awk 'NR%3==1' {{filename}}`

- Tipăriți valori diferite în funcție de condiții:

`awk '{if ($1 == "foo") print "Exact match foo"; else if ($1 ~ "bar") print "Partial match bar"; else print "Baz"}' {{filename}}`

- Imprimați toate liniile în care valoarea coloanei 10 este egală cu valoarea specificată:

`awk '($10 == value)'`

- Imprimați toate liniile care valoarea coloanei 10 este între un min și un max:

`awk '($10 >= min_value && $10 <= max_value)'`
