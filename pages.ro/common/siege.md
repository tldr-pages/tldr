# siege

> instrument de testare a încărcării HTTP și benchmarking.
> Mai multe informaţii: <https://www.joedog.org/siege-manual/>

- Testați un URL cu setări implicite:

`siege {{https://example.com}}`

- Testați o listă de adrese URL:

`siege --file {{path/to/url_list.txt}}`

- Lista de testare a adreselor URL într-o ordine aleatorie (Simulează traficul pe internet):

`siege --internet --file {{path/to/url_list.txt}}`

- Indicați o listă de adrese URL (fără a aștepta între solicitări):

`siege --benchmark --file {{path/to/url_list.txt}}`

- Setați cantitatea de conexiuni simultane:

`siege --concurrent={{50}} --file {{path/to/url_list.txt}}`

- Setați cât timp pentru asediu pentru a rula pentru:

`siege --time={{30s}} --file {{path/to/url_list.txt}}`
