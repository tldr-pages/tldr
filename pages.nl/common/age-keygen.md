# age-keygen

> Genereer `age` sleutelparen.
> Zie ook: `age`, `age-inspect`.
> Meer informatie: <https://manned.org/age-keygen>.

- Genereer een sleutelpaar, sla de privésleutel op in een niet-versleuteld bestand en print de openbare sleutel naar `stdout`:

`age-keygen {{[-o|--output]}} {{pad/naar/bestand}}`

- Genereer een post-quantum sleutelpaar, sla het op in een niet-versleuteld bestand en print de publieke sleutel naar `stdout`:

`age-keygen -pq {{[-o|--output]}} {{pad/naar/bestand}}`

- Converteer een identiteit naar een ontvanger en print de publieke sleutel naar `stdout`:

`age-keygen -y {{pad/naar/bestand}}`
