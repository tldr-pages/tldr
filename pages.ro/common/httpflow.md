# httpflow

> Un utilitar de linie de comandă pentru a captura și a dump fluxuri HTTP.
> Mai multe informaţii: <https://github.com/six-ddc/httpflow>

- Capturarea traficului pe toate interfețele:

`httpflow -i {{any}}`

- Utilizați o captură în stil bpf pentru a filtra rezultatele:

`httpflow {{host httpbin.org or host baidu.com}}`

- Utilizați o expresie regulată pentru a filtra solicitările de adrese URL:

`httpflow -u '{{regular_expression}}'`

- Citiți pachetele din fișierul binar format pcap:

`httpflow -r {{out.cap}}`

- Scrieți ieșirea într-un director:

`httpflow -w {{path/to/directory}}`
