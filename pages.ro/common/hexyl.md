# hexyl

> Un vizualizator hexagon simplu pentru terminal. Utilizează rezultatul colorat pentru a distinge diferite categorii de octeți.
> Mai multe informaţii: <https://github.com/sharkdp/hexyl>

- Imprimați reprezentarea hexazecimal a unui fișier:

`hexyl {{path/to/file}}`

- Imprimați reprezentarea hexazecimală a primilor n octeți ai unui fișier:

`hexyl -n {{n}} {{path/to/file}}`

- Imprimați octeți 512 până la 1024 dintr-un fișier:

`hexyl -r {{512}}:{{1024}} {{path/to/file}}`

- Imprimați 512 octeți începând de la octet 1024th:

`hexyl -r {{1024}}:+{{512}} {{path/to/file}}`
