# sqsc

> Un client de linie de comandă AWS simplă coadă Service.
> Mai multe informaţii: <https://github.com/yongfei25/sqsc>

- Listează toate cozile:

`sqsc lq {{queue_prefix}}`

- Listează toate mesajele într-o coadă:

`sqsc ls {{queue_name}}`

- Copiați toate mesajele dintr-o coadă în alta:

`sqsc cp {{source_queue}} {{destination_queue}}`

- Mutați toate mesajele dintr-o coadă în alta:

`sqsc mv {{source_queue}} {{destination_queue}}`

- Descrieți o coadă de așteptare:

`sqsc describe {{queue_name}}`

- Interogare o coadă cu sintaxa SQL:

`sqsc query "SELECT body FROM {{queue_name}} WHERE body LIKE '%user%'"`

- Trageți toate mesajele dintr-o coadă într-o bază de date sqlite locală din directorul dvs. de lucru actual:

`sqsc pull {{queue_name}}`
