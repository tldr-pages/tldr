# gnomon

> Utilitar pentru a adnota declarațiile de înregistrare în consolă cu marcaje temporale și pentru a găsi procese lente.
> Mai multe informaţii: <https://github.com/paypal/gnomon>

- Folositi tevi UNIX (sau DOS) pentru a tevi stdout de orice comanda prin gnomon:

`{{npm test}} | gnomon`

- Arată numărul de secunde de la începerea procesului:

`{{npm test}} | gnomon --type=elapsed-total`

- Arată un timestamp absolut în UTC:

`{{npm test}} | gnomon --type=absolute`

- Setați un prag înalt de 0,5 secunde pentru timpul scurs; depășind care marcajul temporal va fi colorat roșu aprins:

`{{npm test}} | gnomon --high {{0.5}}`

- Setați un prag mediu de 0,2 secunde (Timestamp va fi colorat galben strălucitor):

`{{npm test}} | gnomon --medium {{0.2}}`
